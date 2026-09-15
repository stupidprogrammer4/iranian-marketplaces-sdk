"""Shared request building for all Digikala resource groups."""

from dataclasses import dataclass
from secrets import token_hex
from typing import BinaryIO
from urllib.parse import quote

import httpx
from pydantic import BaseModel, JsonValue, TypeAdapter

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema, parse
from iranian_marketplaces_sdk.common.exceptions import ConfigurationError
from iranian_marketplaces_sdk.common.http import AsyncTransport, SyncTransport, UploadFiles
from iranian_marketplaces_sdk.marketplaces.digikala.helpers import JSON_HEADERS

_JSON_ADAPTER: TypeAdapter[JsonValue] = TypeAdapter(JsonValue)


def request_headers(file: "Upload | None") -> dict[str, str]:
    if file is None:
        return JSON_HEADERS
    # Explicit boundary also overrides a JSON Content-Type inherited from an injected client.
    # httpx uses this boundary when encoding its multipart stream.
    return {"Content-Type": f"multipart/form-data; boundary={token_hex(16)}"}


@dataclass(frozen=True)
class Upload:
    """A multipart file. Open binary streams remain owned by the caller."""

    filename: str
    content: bytes | BinaryIO
    content_type: str = "application/octet-stream"

    def as_files(self) -> UploadFiles:
        return {"file": (self.filename, self.content, self.content_type)}


@dataclass(frozen=True)
class RawResponse:
    """An undocumented response: preserve JSON, empty bodies, PDF and Excel bytes alike.

    ``content`` is never decoded as text implicitly. Use ``json()`` only for JSON responses;
    it raises ValueError for other content. No file is saved or remote download URL followed.
    """

    status_code: int
    headers: httpx.Headers
    content: bytes

    def json(self) -> JsonValue:
        return _JSON_ADAPTER.validate_json(self.content)


def path_value(value: str | int | list[int]) -> str:
    """Encode exactly one path segment, preventing slash/query/fragment injection."""
    text = ",".join(map(str, value)) if isinstance(value, list) else str(value)
    if not text or text in {".", ".."}:
        raise ConfigurationError("a Digikala path parameter must be a non-empty segment")
    return quote(text, safe="")


def query_params(query: QuerySchema | None, *, separators: dict[str, str]) -> dict[str, JsonValue]:
    """Serialize each query according to its endpoint; only variants.ids uses underscores."""
    if query is None:
        return {}
    params: dict[str, JsonValue] = {}
    raw: dict[str, JsonValue] = query.to_params()
    for key, value in raw.items():
        if isinstance(value, list):
            params[key] = separators.get(key, ",").join(str(item) for item in value)
        else:
            params[key] = value
    return params


def parse_response[T: BaseModel](model: type[T], response: httpx.Response) -> T:
    """Convert invalid JSON through the same response-validation error as invalid schemas."""
    try:
        raw = response.json() if response.content else None
    except (ValueError, UnicodeDecodeError):
        raw = response.text
    return parse(model, raw)


class SyncResource:
    """A resource shares its parent client's session and refreshed authorization header."""

    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def _request(
        self,
        method: str,
        path: str,
        *,
        query: QuerySchema | None = None,
        separators: dict[str, str] | None = None,
        body: RequestSchema | None = None,
        file: Upload | None = None,
    ) -> httpx.Response:
        return self._transport.request_response(
            method,
            path,
            params=query_params(query, separators=separators or {}),
            json=body.to_payload() if body is not None else None,
            headers=request_headers(file),
            files=file.as_files() if file is not None else None,
        )


class AsyncResource:
    """Async counterpart of SyncResource; all network calls are awaited."""

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def _request(
        self,
        method: str,
        path: str,
        *,
        query: QuerySchema | None = None,
        separators: dict[str, str] | None = None,
        body: RequestSchema | None = None,
        file: Upload | None = None,
    ) -> httpx.Response:
        return await self._transport.request_response(
            method,
            path,
            params=query_params(query, separators=separators or {}),
            json=body.to_payload() if body is not None else None,
            headers=request_headers(file),
            files=file.as_files() if file is not None else None,
        )
