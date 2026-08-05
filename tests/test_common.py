"""The shared layer: model bases, error mapping, and the query helpers."""

import httpx
import pytest

from iranian_marketplaces_sdk import (
    AuthenticationError,
    ConfigurationError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ResponseValidationError,
    ServerError,
)
from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema, ResponseSchema, parse
from iranian_marketplaces_sdk.common.http import SyncTransport, build_api_error
from iranian_marketplaces_sdk.common.utils import (
    bracket_params,
    drop_none,
    join_values,
    rename_keys,
    require_text,
)


class Sample(ResponseSchema):
    id: int
    name: str
    note: str | None = None


class SampleRequest(RequestSchema):
    a: int
    b: int | None = None
    c: str | None = None


class SampleQuery(QuerySchema):
    page: int | None = None
    ids: list[int] | None = None


def test_response_keeps_unknown_fields() -> None:
    """An upstream addition must reach the caller, not break the call."""
    parsed = Sample.model_validate({"id": 1, "name": "x", "brand_new_field": 42})
    assert parsed.id == 1
    assert parsed.model_extra == {"brand_new_field": 42}
    assert parsed.model_dump()["brand_new_field"] == 42


def test_response_missing_required_field_raises_with_raw_body() -> None:
    raw = {"id": 1}
    with pytest.raises(ResponseValidationError) as exc:
        parse(Sample, raw)
    assert exc.value.model == "Sample"
    assert exc.value.raw is raw
    assert exc.value.errors


def test_request_sends_only_what_was_set() -> None:
    """Partial updates stay partial: an untouched field is not sent as null."""
    assert SampleRequest(a=1).to_payload() == {"a": 1}
    assert SampleRequest(a=1, b=2).to_payload() == {"a": 1, "b": 2}


def test_request_keeps_an_explicit_none() -> None:
    """Some endpoints need a literal null; setting it deliberately must survive."""
    assert SampleRequest(a=1, c=None).to_payload() == {"a": 1, "c": None}


def test_request_rejects_unknown_field() -> None:
    with pytest.raises(ValueError):
        SampleRequest(a=1, typoed=2)  # type: ignore[call-arg]


def test_query_drops_none_but_keeps_lists() -> None:
    assert SampleQuery(page=2, ids=None).to_params() == {"page": 2}
    assert SampleQuery(ids=[1, 2]).to_params() == {"ids": [1, 2]}


def test_join_values() -> None:
    assert join_values([1, 2, 3]) == "1,2,3"
    assert join_values([1, 2, 3], "_") == "1_2_3"
    assert join_values("already-a-string") == "already-a-string"
    assert join_values(7) == 7


def test_small_query_helpers() -> None:
    assert drop_none({"a": 1, "b": None}) == {"a": 1}
    assert bracket_params("search", {"active": True}) == {"search[active]": True}
    assert rename_keys({"stock_gte": 1, "page": 2}, {"stock_gte": "stock[gte]"}) == {
        "stock[gte]": 1,
        "page": 2,
    }


def test_require_text() -> None:
    assert require_text("  token  ", field="token", marketplace="x") == "token"
    with pytest.raises(ConfigurationError):
        require_text("   ", field="token", marketplace="x")


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (401, AuthenticationError),
        (403, AuthenticationError),
        (404, NotFoundError),
        (429, RateLimitError),
        (500, ServerError),
        (400, None),
    ],
)
def test_error_mapping(status: int, expected: type[Exception] | None) -> None:
    request = httpx.Request("GET", "https://example.test/thing")
    response = httpx.Response(status, json={"detail": "no"}, request=request)
    error = build_api_error(response)
    assert error.status_code == status
    assert error.response_body == {"detail": "no"}
    if expected is not None:
        assert isinstance(error, expected)


def test_rate_limit_error_reads_retry_after() -> None:
    request = httpx.Request("GET", "https://example.test/thing")
    response = httpx.Response(429, headers={"Retry-After": "12"}, request=request)
    error = build_api_error(response)
    assert isinstance(error, RateLimitError)
    assert error.retry_after == 12.0


def test_retry_after_http_date_is_reported_as_unknown() -> None:
    """The HTTP-date form is not parsed — better an honest ``None`` than a wrong number."""
    request = httpx.Request("GET", "https://example.test/thing")
    response = httpx.Response(
        429, headers={"Retry-After": "Wed, 21 Oct 2015 07:28:00 GMT"}, request=request
    )
    error = build_api_error(response)
    assert isinstance(error, RateLimitError)
    assert error.retry_after is None


def test_transport_failure_becomes_network_error() -> None:
    def explode(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("no route", request=request)

    transport = SyncTransport(
        "https://example.test", client=httpx.Client(transport=httpx.MockTransport(explode))
    )
    with pytest.raises(NetworkError):
        transport.get("/thing")


def test_empty_body_decodes_to_none() -> None:
    """A 204/202 with no body is a success, not a parse failure."""
    transport = SyncTransport(
        "https://example.test",
        client=httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(204))),
    )
    assert transport.get("/thing") is None
