"""Offline wire contracts for every documented operation, plus real response-shape regressions."""

import inspect
import json
import re
from pathlib import Path
from typing import Any, cast, get_type_hints

import httpx
import pytest
from pydantic import BaseModel, JsonValue, ValidationError

from iranian_marketplaces_sdk import (
    AuthenticationError,
    DigikalaAsync,
    DigikalaSync,
    NetworkError,
    RateLimitError,
    ResponseValidationError,
    ServerError,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data.api import (
    auth,
    categories,
    orders,
    packages,
    plp,
    products,
    seller_shipping,
    variants,
    webhooks,
)
from iranian_marketplaces_sdk.marketplaces.digikala.operations import OPERATIONS, Operation
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import RawResponse, Upload
from tests.conftest import Recorder, async_client, sync_client

SPEC = json.loads((Path(__file__).resolve().parent / "fixtures/digikala_openapi.json").read_text())
SCOPED_OPERATIONS = [operation for operation in OPERATIONS if "." in operation.call]


def sample(schema: dict[str, Any], root: dict[str, Any]) -> Any:
    """Build minimal validated input; field names and wire contracts are checked against Swagger."""
    if "$ref" in schema:
        node = root
        for segment in schema["$ref"].removeprefix("#/").split("/"):
            node = node[segment]
        return sample(node, root)
    for union in ("anyOf", "oneOf"):
        if union in schema:
            return sample(next(s for s in schema[union] if s.get("type") != "null"), root)
    if "enum" in schema:
        return schema["enum"][0]
    if "const" in schema:
        return schema["const"]
    match schema.get("type"):
        case "object":
            return {
                key: sample(value, root)
                for key, value in schema.get("properties", {}).items()
                if key in schema.get("required", [])
            }
        case "array":
            return [sample(schema.get("items", {}), root)]
        case "integer":
            return 17
        case "number":
            return 17.5
        case "boolean":
            return True
        case "string":
            return "sample"
        case _:
            return None


def arguments(call: Any) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, parameter in inspect.signature(call).parameters.items():
        if name == "file":
            result[name] = Upload("image.png", b"example", "image/png")
        elif name in {"body", "query"}:
            annotation = get_type_hints(call)[name]
            model = annotation.__args__[0] if hasattr(annotation, "__args__") else annotation
            schema = model.model_json_schema()
            # Exercise every query alias, including optional filters, on every operation.
            values = (
                {k: sample(v, schema) for k, v in schema.get("properties", {}).items()}
                if name == "query"
                else sample(schema, schema)
            )
            result[name] = model.model_validate(values)
        elif parameter.annotation == "list[int]":
            result[name] = [17, 23]
        elif parameter.annotation == "str":
            result[name] = "sample"
        else:
            result[name] = 17
    return result


def assert_contract(operation: Operation, rec: Recorder, kwargs: dict[str, Any]) -> None:
    request = rec.request
    assert request.method == operation.method
    assert request.url.host == "seller.digikala.com"
    expected_path = operation.path
    for wire in re.findall(r"\{(.*?)\}", expected_path):
        python_name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", wire).lower()
        value = kwargs[python_name]
        value = (
            ",".join(map(str, cast(list[int], value))) if isinstance(value, list) else str(value)
        )
        expected_path = expected_path.replace("{" + wire + "}", value)
    assert request.url.path == expected_path
    assert request.headers["authorization"] == "Bearer test-access"
    documented = SPEC["paths"][operation.path][operation.method.lower()]
    query_parameters = {p["name"]: p for p in documented["parameters"] if p["in"] == "query"}
    if "query" in kwargs:
        query: dict[str, JsonValue] = kwargs["query"].to_params()
        assert set(query) <= query_parameters.keys()
        assert set(request.url.params) == set(query)
        for name, value in query.items():
            if isinstance(value, list):
                desc = str(query_parameters[name].get("description", "")).lower()
                separator = "_" if "underscore" in desc else ","
                expected = separator.join(map(str, value))
            elif isinstance(value, bool):
                expected = str(value).lower()
            else:
                expected = str(value)
            assert request.url.params[name] == expected
    else:
        assert not request.url.params
    if "body" in kwargs:
        body_schema = documented["requestBody"]["content"]["application/json"]["schema"]
        body = rec.body
        assert set(body) <= body_schema["properties"].keys()
        assert set(body_schema.get("required") or []) <= body.keys()
    if "file" in kwargs:
        assert request.headers["content-type"].startswith("multipart/form-data; boundary=")
        assert b'filename="image.png"' in request.content
        assert b"example" in request.content
    else:
        assert request.headers["content-type"] == "application/json"


def test_catalog_covers_pinned_swagger_exactly() -> None:
    documented = {
        (method.upper(), path) for path, methods in SPEC["paths"].items() for method in methods
    }
    assert len(OPERATIONS) == len(documented) == 274
    assert {(operation.method, operation.path) for operation in OPERATIONS} == documented
    assert len({operation.call for operation in OPERATIONS}) == 274


@pytest.mark.parametrize("operation", SCOPED_OPERATIONS, ids=lambda op: op.call)
def test_sync_wire_contract(operation: Operation) -> None:
    rec = Recorder({}, status_code=500)
    with DigikalaSync("test-access", client=sync_client(rec)) as client:
        resource, name = operation.call.split(".")
        call = getattr(getattr(client, resource), name)
        kwargs = arguments(call)
        with pytest.raises(ServerError):
            call(**kwargs)
    assert_contract(operation, rec, kwargs)


@pytest.mark.parametrize("operation", SCOPED_OPERATIONS, ids=lambda op: op.call)
async def test_async_wire_contract(operation: Operation) -> None:
    rec = Recorder({}, status_code=500)
    async with DigikalaAsync("test-access", client=async_client(rec)) as client:
        resource, name = operation.call.split(".")
        call = getattr(getattr(client, resource), name)
        kwargs = arguments(call)
        with pytest.raises(ServerError):
            await call(**kwargs)
    assert_contract(operation, rec, kwargs)


def test_required_inputs_and_unknown_keys_fail_before_network() -> None:
    with pytest.raises(ValidationError):
        orders.CancelRequest.model_validate({})
    with pytest.raises(ValidationError):
        variants.UpdateRequest.model_validate({"seller_stok": 10})
    with pytest.raises(ValidationError):
        packages.WarehouseCapacitiesQuery.model_validate({})
    with pytest.raises(ValidationError):
        webhooks.SubscribeRequest.model_validate({"event_types": ["nonexistent-event"]})


def test_partial_updates_and_camel_case_payloads() -> None:
    rec = Recorder({"status": "ok", "data": {}})
    with DigikalaSync("token", client=sync_client(rec)) as client:
        client.variants.update(8, body=variants.UpdateRequest(seller_stock=7))
    assert rec.body == {"seller_stock": 7}
    body = plp.ImportExcelRequest(
        title="Sample",
        platform="site_all",
        start_at="2026-09-16",
        end_at="2026-09-17",
        is_ad_plp=False,
        file_id=123,
    )
    assert body.to_payload() == {
        "title": "Sample",
        "platform": "site_all",
        "startAt": "2026-09-16",
        "endAt": "2026-09-17",
        "isAdPLP": False,
        "fileId": 123,
    }


def test_list_separators_are_specific_to_the_endpoint() -> None:
    rec = Recorder({"status": "ok", "data": {}})
    with DigikalaSync("token", client=sync_client(rec)) as client:
        client.variants.list(
            query=variants.ListQuery(search_ids=[11, 22], search_category_ids=[3, 4])
        )
        client.seller_shipping.list(
            query=seller_shipping.ListQuery(search_ids=[11, 22], search_type="self_shipping")
        )
    assert rec.requests[0].url.params["search[ids]"] == "11_22"
    assert rec.requests[0].url.params["search[category_ids]"] == "3,4"
    assert rec.requests[1].url.params["search[ids]"] == "11,22"


def test_nested_response_and_php_empty_objects() -> None:
    rec = Recorder(
        {
            "status": "ok",
            "data": {
                "items": [{"id": 12, "title": "Category", "future_key": True}],
                "meta_data": [],
                "sort_data": [],
            },
        }
    )
    with DigikalaSync("token", client=sync_client(rec)) as client:
        response = client.categories.tree()
    assert isinstance(response, categories.TreeResponse)
    assert response.data.items is not None
    assert response.data.items[0].id == 12
    assert response.data.items[0].model_extra == {"future_key": True}
    assert response.data.meta_data == {}


def test_live_datetime_shape_regression() -> None:
    result = variants.ListResponse.model_validate(
        {
            "status": "ok",
            "data": {
                "items": [
                    {
                        "id": 12,
                        "created_at": {
                            "date": "2026-09-15",
                            "timezone_type": 3,
                            "timezone": "Asia/Tehran",
                        },
                    }
                ]
            },
        }
    )
    assert result.data.items is not None
    assert isinstance(result.data.items[0].created_at, BaseModel)
    detail = variants.GetResponse.model_validate(
        {
            "status": "ok",
            "data": {
                "id": 12,
                "created_at": {
                    "date": "2026-09-15",
                    "timezone_type": 3,
                    "timezone": "Asia/Tehran",
                },
            },
        }
    )
    assert isinstance(detail.data.created_at, BaseModel)


def test_live_webhook_event_map_regression() -> None:
    result = webhooks.EventTypesResponse.model_validate(
        {
            "status": "ok",
            "data": {
                "all_event_types": {"commission_change": "Commission change"},
                "allowed_event_types": ["commission_change"],
                "active_event_types": [],
            },
        }
    )
    assert result.data.all_event_types == {"commission_change": "Commission change"}


@pytest.mark.parametrize(
    "payload", [{"bad": "envelope"}, {"status": "ok", "data": {"items": "bad"}}]
)
def test_invalid_response_is_not_silently_accepted(payload: Any) -> None:
    rec = Recorder(payload)
    with (
        DigikalaSync("token", client=sync_client(rec)) as client,
        pytest.raises(ResponseValidationError) as exc,
    ):
        client.categories.tree()
    assert exc.value.raw == payload


@pytest.mark.parametrize(
    "content_type,content",
    [
        ("application/pdf", b"%PDF-1.7\xff\x00"),
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", b"PK\x03\x04\xff"),
        ("application/json", b'{"status":"ok","data":{"job_id":123}}'),
        ("application/octet-stream", b""),
    ],
)
async def test_undocumented_responses_preserve_bytes_sync_and_async(
    content_type: str, content: bytes
) -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=content, headers={"content-type": content_type})

    with DigikalaSync(
        "token", client=httpx.Client(transport=httpx.MockTransport(respond))
    ) as client:
        sync = client.smart_discount.sample_excel()
    async with DigikalaAsync(
        "token", client=httpx.AsyncClient(transport=httpx.MockTransport(respond))
    ) as async_sdk:
        asynchronous = await async_sdk.smart_discount.sample_excel()
    for result in [sync, asynchronous]:
        assert isinstance(result, RawResponse)
        assert result.content == content
        assert result.headers["content-type"] == content_type
        if content_type == "application/json":
            assert result.json() == {"status": "ok", "data": {"job_id": 123}}


async def test_uploaded_binary_is_preserved_and_stream_is_not_closed() -> None:
    from io import BytesIO

    stream = BytesIO(b"\x89PNG\r\n\x00\xff")
    rec = Recorder({"status": "ok", "data": {"isValid": True, "data": {"id": "file-1"}}})
    async with DigikalaAsync("token", client=async_client(rec)) as client:
        result = await client.products.upload_image(file=Upload("sample.png", stream, "image/png"))
    assert result.data.is_valid is True
    assert not stream.closed
    assert b"\x89PNG\r\n\x00\xff" in rec.request.content
    assert rec.request.headers["content-type"].startswith("multipart/form-data; boundary=")


def test_upload_overrides_injected_json_content_type() -> None:
    rec = Recorder({"status": "ok", "data": {}})
    transport = httpx.Client(
        headers={"Content-Type": "application/json"}, transport=httpx.MockTransport(rec.handle)
    )
    with DigikalaSync("token", client=transport) as client:
        client.products.upload_image(file=Upload("image.png", b"image", "image/png"))
    content_type = rec.request.headers["content-type"]
    boundary = content_type.split("boundary=", 1)[1].encode()
    assert rec.request.content.startswith(b"--" + boundary + b"\r\n")
    assert rec.request.content.endswith(b"--" + boundary + b"--\r\n")


def test_optional_body_can_be_omitted() -> None:
    rec = Recorder({"status": "ok", "data": {}})
    with DigikalaSync("token", client=sync_client(rec)) as client:
        client.webhooks.subscribe()
    assert rec.request.content == b""


def test_string_path_parameter_cannot_insert_query_or_path() -> None:
    rec = Recorder({"status": "ok", "data": {}})
    with DigikalaSync("token", client=sync_client(rec)) as client:
        client.products.search_categories("phone/tablet?x=1#fragment")
    assert b"phone%2Ftablet%3Fx%3D1%23fragment" in rec.request.url.raw_path
    assert not rec.request.url.query
    assert not rec.request.url.fragment


@pytest.mark.parametrize(
    "status,error", [(401, AuthenticationError), (403, AuthenticationError), (429, RateLimitError)]
)
async def test_resource_errors_are_shared_and_requests_are_not_retried(
    status: int, error: type[Exception]
) -> None:
    rec = Recorder({"status": "error"}, status_code=status)
    async with DigikalaAsync("token", client=async_client(rec)) as client:
        with pytest.raises(error):
            await client.orders.statistics()
    assert len(rec.requests) == 1


def test_network_error_is_mapped() -> None:
    def fail(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("timeout", request=request)

    with (
        DigikalaSync("token", client=httpx.Client(transport=httpx.MockTransport(fail))) as client,
        pytest.raises(NetworkError),
    ):
        client.categories.tree()


def test_credentials_are_not_exposed_in_repr() -> None:
    with DigikalaSync("secret-access", "secret-refresh") as client:
        assert "secret" not in repr(client.config)


def test_public_models_export_correct_types() -> None:
    assert auth.ListScopesResponse.model_validate({"status": "ok", "data": {"meta_data": []}})
    assert products.ListSellerQuery(size=1).to_params() == {"size": 1}


async def test_existing_resource_uses_refreshed_token_in_both_engines() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.url.path.endswith("/refresh-token"):
            expiry = {"date": "2026-09-20", "timezone_type": 3, "timezone": "Asia/Tehran"}
            return httpx.Response(
                200,
                json={
                    "status": "ok",
                    "data": {
                        "access_token": "new-access",
                        "refresh_token": "new-refresh",
                        "access_token_expires_at": expiry,
                        "refresh_token_expires_at": expiry,
                    },
                },
            )
        return httpx.Response(200, json={"status": "ok", "data": {"items": []}})

    with DigikalaSync(
        "old-access", "old-refresh", client=httpx.Client(transport=httpx.MockTransport(respond))
    ) as sync:
        resource = sync.categories
        assert sync.categories is resource
        sync.refresh_token()
        resource.tree()
    async with DigikalaAsync(
        "old-access",
        "old-refresh",
        client=httpx.AsyncClient(transport=httpx.MockTransport(respond)),
    ) as asynchronous:
        async_resource = asynchronous.categories
        await asynchronous.refresh_token()
        await async_resource.tree()
    assert [request.headers["authorization"] for request in requests] == [
        "Bearer old-access",
        "Bearer new-access",
        "Bearer old-access",
        "Bearer new-access",
    ]
