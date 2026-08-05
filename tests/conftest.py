"""Test fixtures: a recording HTTP transport, so every test runs offline.

Nothing here touches a real marketplace. :class:`Recorder` stands in for one — it answers with a
canned body and keeps the request it was given, which is what lets a test assert on the exact URL,
query string and body the SDK produced.
"""

import json
from collections.abc import Callable
from typing import Any

import httpx
import pytest


class Recorder:
    """A canned marketplace. Answers with ``payload`` and remembers what it was asked."""

    def __init__(self, payload: Any, *, status_code: int = 200) -> None:
        self.payload = payload
        self.status_code = status_code
        self.requests: list[httpx.Request] = []

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return httpx.Response(self.status_code, json=self.payload)

    @property
    def request(self) -> httpx.Request:
        """The single request made, asserting there was exactly one."""
        assert len(self.requests) == 1, f"expected 1 request, got {len(self.requests)}"
        return self.requests[0]

    @property
    def body(self) -> Any:
        """The decoded JSON body of the single request made."""
        return json.loads(self.request.content)

    @property
    def params(self) -> dict[str, str]:
        """The query parameters of the single request made, as sent."""
        return dict(self.request.url.params)


@pytest.fixture
def recorder() -> Callable[..., Recorder]:
    """Build a :class:`Recorder` — ``recorder(payload)`` or ``recorder(payload, status_code=…)``."""
    return Recorder


def sync_client(rec: Recorder) -> httpx.Client:
    """An ``httpx.Client`` wired to a recorder instead of the network."""
    return httpx.Client(transport=httpx.MockTransport(rec.handle))


def async_client(rec: Recorder) -> httpx.AsyncClient:
    """An ``httpx.AsyncClient`` wired to a recorder instead of the network."""
    return httpx.AsyncClient(transport=httpx.MockTransport(rec.handle))
