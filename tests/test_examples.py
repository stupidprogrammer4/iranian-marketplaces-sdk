"""Examples must be safe to import and reject missing credentials before making requests."""

import importlib
import inspect
from typing import Never

import httpx
import pytest

from examples.digikala import pagination, prepare_update
from iranian_marketplaces_sdk import DigikalaSync

LIVE_EXAMPLES = [
    f"examples.{marketplace}.{mode}_usage"
    for marketplace in ("digikala", "snapp", "basalam", "tapsi")
    for mode in ("sync", "async")
] + ["examples.digikala.pagination"]
CREDENTIAL_NAMES = (
    "DIGIKALA_ACCESS_TOKEN",
    "DIGIKALA_REFRESH_TOKEN",
    "SNAPP_UNIQUE_CODE",
    "SNAPP_ACCESS_TOKEN",
    "SNAPP_SELLER_ID",
    "BASALAM_VENDOR_ID",
    "BASALAM_ACCESS_TOKEN",
    "TAPSI_TOKEN",
)


def deny_network(*args: object, **kwargs: object) -> Never:
    raise AssertionError("This example must not reach the network")


@pytest.mark.parametrize("module_name", [*LIVE_EXAMPLES, "examples.digikala.prepare_update"])
def test_import_requires_no_credentials_or_network(
    module_name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    for name in CREDENTIAL_NAMES:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(httpx.Client, "request", deny_network)
    monkeypatch.setattr(httpx.AsyncClient, "request", deny_network)
    importlib.reload(importlib.import_module(module_name))


@pytest.mark.parametrize("module_name", LIVE_EXAMPLES)
async def test_missing_credentials_stop_before_network(
    module_name: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    for name in CREDENTIAL_NAMES:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(httpx.Client, "request", deny_network)
    monkeypatch.setattr(httpx.AsyncClient, "request", deny_network)
    module = importlib.import_module(module_name)
    with pytest.raises(SystemExit, match=r"Set .* before running this example"):
        if inspect.iscoroutinefunction(module.main):
            await module.main()
        else:
            module.main()


def test_prepare_update_runs_offline(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr(httpx.Client, "request", deny_network)
    prepare_update.main()
    assert capsys.readouterr().out.strip() == '{"seller_stock": 7}'


@pytest.mark.parametrize("total_pages,expected", [(2, 2), (100, 3), (None, 1)])
def test_pagination_respects_server_metadata_and_request_limit(
    total_pages: int | None, expected: int, monkeypatch: pytest.MonkeyPatch
) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "status": "ok",
                "data": {
                    "items": [{"id": 123, "title": "Example"}],
                    "pager": {"total_pages": total_pages},
                },
            },
        )

    def make_client(access_token: str) -> DigikalaSync:
        return DigikalaSync(
            access_token, client=httpx.Client(transport=httpx.MockTransport(respond))
        )

    monkeypatch.setenv("DIGIKALA_ACCESS_TOKEN", "example-access")
    monkeypatch.setattr(pagination, "DigikalaSync", make_client)
    pagination.main()
    assert len(requests) == expected
    assert [request.url.params["page"] for request in requests] == [
        str(page) for page in range(1, expected + 1)
    ]
