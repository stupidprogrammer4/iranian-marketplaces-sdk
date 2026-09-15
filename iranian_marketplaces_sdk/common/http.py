"""One HTTP round-trip, in both flavours, shared by every marketplace.

Every marketplace here speaks REST/JSON over a long-lived, authenticated session — dozens of calls
against the same host with the same bearer token — so unlike a one-shot payment call, the client
itself is worth keeping. :class:`SyncTransport` and :class:`AsyncTransport` each own one
``httpx`` client with the base URL and auth headers already bound, and normalise the two into the
same method names, the same arguments, and the same errors.

Keeping the transport in one place is also what stops the async engine from quietly growing a
blocking call: a synchronous request inside a coroutine parks the event loop for up to the timeout,
so one slow marketplace stalls every other request in the process.

The engines never touch ``httpx`` directly. They call ``get``/``post``/``put``/``patch``/``delete``
and get back the decoded body — or one of the exceptions in
:mod:`~iranian_marketplaces_sdk.common.exceptions`.
"""

from collections.abc import Mapping
from types import TracebackType
from typing import Any, BinaryIO, Self

import httpx

from iranian_marketplaces_sdk.common.constants import DEFAULT_TIMEOUT
from iranian_marketplaces_sdk.common.exceptions import (
    APIError,
    AuthenticationError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    ServerError,
)

type UploadFiles = Mapping[str, tuple[str, bytes | BinaryIO, str]]


def _extract_body(response: httpx.Response) -> Any:
    """The JSON body where there is one, the raw text where there is not.

    Error responses are the ones most likely to arrive as an HTML error page from a proxy in front
    of the marketplace, so this never assumes JSON.
    """
    try:
        return response.json()
    except (ValueError, UnicodeDecodeError):
        return response.text


def _parse_retry_after(response: httpx.Response) -> float | None:
    """``Retry-After`` in its delta-seconds form. The HTTP-date form is reported as unknown."""
    raw = response.headers.get("Retry-After")
    if raw is None:
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def build_api_error(response: httpx.Response) -> APIError:
    """Map an unsuccessful response onto the exception that says what actually went wrong."""
    status = response.status_code
    body = _extract_body(response)
    # `response.request` raises rather than returning None when a response was built without one,
    # which only happens to a hand-made Response. An error report is not worth failing over.
    try:
        url: str | None = str(response.request.url)
    except RuntimeError:
        url = None
    message = f"Request to {url or 'marketplace'} failed"

    if status in (401, 403):
        return AuthenticationError(message, status_code=status, response_body=body, request_url=url)
    if status == 404:
        return NotFoundError(message, status_code=status, response_body=body, request_url=url)
    if status == 429:
        return RateLimitError(
            message,
            status_code=status,
            response_body=body,
            request_url=url,
            retry_after=_parse_retry_after(response),
        )
    if status >= 500:
        return ServerError(message, status_code=status, response_body=body, request_url=url)
    return APIError(message, status_code=status, response_body=body, request_url=url)


def _decode(response: httpx.Response) -> Any:
    """The decoded body of a successful response, or ``None`` for an empty one.

    Several endpoints answer ``202`` or ``204`` with no body at all, which is a success and must
    not look like a parse failure.
    """
    if not response.content:
        return None
    try:
        return response.json()
    except ValueError:
        return response.text


class SyncTransport:
    """A bound :class:`httpx.Client`, with the SDK's error mapping on top."""

    def __init__(
        self,
        base_url: str,
        *,
        headers: Mapping[str, str] | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.Client | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = client or httpx.Client(
            base_url=self._base_url,
            headers=dict(headers or {}),
            timeout=timeout,
        )
        if client is not None:
            # An injected client — a test double, a custom transport, a proxy — supplies the
            # transport, not the destination. The base URL and the credentials are facts about the
            # marketplace, so they are bound here either way.
            self._client.base_url = httpx.URL(self._base_url)
            if headers:
                self._client.headers.update(dict(headers))

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def client(self) -> httpx.Client:
        """The underlying ``httpx`` client, for the cases the SDK does not cover."""
        return self._client

    def set_header(self, name: str, value: str) -> None:
        """Replace a header on the live session — how a refreshed token takes effect."""
        self._client.headers[name] = value

    def request_response(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        files: UploadFiles | None = None,
    ) -> httpx.Response:
        """Perform a request and preserve bytes and headers, including file downloads.

        Transport failures become :class:`NetworkError`; a non-2xx becomes the matching
        :class:`APIError` subclass, carrying the body the marketplace sent with it.
        """
        try:
            response = self._client.request(
                method,
                path,
                params=params,
                json=json,
                data=data,
                headers=dict(headers) if headers else None,
                files=files,
            )
        except httpx.TimeoutException as exc:
            raise NetworkError(f"Request to {path} timed out") from exc
        except httpx.TransportError as exc:
            raise NetworkError(f"Request to {path} failed: {exc}") from exc

        if response.is_error:
            raise build_api_error(response)
        return response

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """Perform a request and decode its JSON or text body."""
        return _decode(
            self.request_response(
                method, path, params=params, json=json, data=data, headers=headers
            )
        )

    def get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request("GET", path, params=params, headers=headers)

    def post(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request("POST", path, json=json, data=data, params=params, headers=headers)

    def put(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request("PUT", path, json=json, data=data, params=params, headers=headers)

    def patch(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self.request("PATCH", path, json=json, data=data, params=params, headers=headers)

    def delete(
        self,
        path: str,
        *,
        json: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """DELETE, with an optional body — Digikala and Basalam both take one."""
        return self.request("DELETE", path, json=json, params=params, headers=headers)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()


class AsyncTransport:
    """A bound :class:`httpx.AsyncClient`, with the SDK's error mapping on top.

    Method-for-method identical to :class:`SyncTransport`; porting a call site between the two
    engines is adding or removing ``await``.
    """

    def __init__(
        self,
        base_url: str,
        *,
        headers: Mapping[str, str] | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = client or httpx.AsyncClient(
            base_url=self._base_url,
            headers=dict(headers or {}),
            timeout=timeout,
        )
        if client is not None:
            # See the note in SyncTransport: an injected client supplies the transport, not the
            # destination.
            self._client.base_url = httpx.URL(self._base_url)
            if headers:
                self._client.headers.update(dict(headers))

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def client(self) -> httpx.AsyncClient:
        """The underlying ``httpx`` client, for the cases the SDK does not cover."""
        return self._client

    def set_header(self, name: str, value: str) -> None:
        """Replace a header on the live session — how a refreshed token takes effect."""
        self._client.headers[name] = value

    async def request_response(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
        files: UploadFiles | None = None,
    ) -> httpx.Response:
        """Perform a request and preserve bytes. See :meth:`SyncTransport.request_response`."""
        try:
            response = await self._client.request(
                method,
                path,
                params=params,
                json=json,
                data=data,
                headers=dict(headers) if headers else None,
                files=files,
            )
        except httpx.TimeoutException as exc:
            raise NetworkError(f"Request to {path} timed out") from exc
        except httpx.TransportError as exc:
            raise NetworkError(f"Request to {path} failed: {exc}") from exc

        if response.is_error:
            raise build_api_error(response)
        return response

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """Perform a request and decode its JSON or text body."""
        return _decode(
            await self.request_response(
                method, path, params=params, json=json, data=data, headers=headers
            )
        )

    async def get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self.request("GET", path, params=params, headers=headers)

    async def post(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self.request(
            "POST", path, json=json, data=data, params=params, headers=headers
        )

    async def put(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self.request("PUT", path, json=json, data=data, params=params, headers=headers)

    async def patch(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self.request(
            "PATCH", path, json=json, data=data, params=params, headers=headers
        )

    async def delete(
        self,
        path: str,
        *,
        json: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """DELETE, with an optional body — Digikala and Basalam both take one."""
        return await self.request("DELETE", path, json=json, params=params, headers=headers)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()
