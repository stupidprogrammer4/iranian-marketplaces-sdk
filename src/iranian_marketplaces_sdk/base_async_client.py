"""Asynchronous base client every marketplace ``async_engine.py`` builds on.

Mirrors :class:`~iranian_marketplaces_sdk.base_client.BaseClient` but uses
:class:`httpx.AsyncClient`. Concrete async engines subclass
:class:`BaseAsyncClient`, pass their ``base_url`` and authentication headers up
to ``__init__``, and ``await`` the ``_get`` / ``_post`` / ``_request`` helpers.
"""

from __future__ import annotations

from types import TracebackType
from typing import Any, Mapping, Self

import httpx

from ._http import build_api_error
from .exceptions import NetworkError

DEFAULT_TIMEOUT = 30.0


class BaseAsyncClient:
    """Thin wrapper around :class:`httpx.AsyncClient` with unified errors."""

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

    @property
    def base_url(self) -> str:
        return self._base_url

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """Perform a request and return the parsed JSON body.

        Transport failures are re-raised as :class:`NetworkError`; non-2xx
        responses are mapped to the appropriate :class:`APIError` subclass.
        """
        try:
            response = await self._client.request(
                method,
                path,
                params=params,
                json=json,
                data=data,
                headers=dict(headers) if headers else None,
            )
        except httpx.TimeoutException as exc:
            raise NetworkError(f"Request to {path} timed out") from exc
        except httpx.TransportError as exc:
            raise NetworkError(f"Request to {path} failed: {exc}") from exc

        if response.is_error:
            raise build_api_error(response)

        if not response.content:
            return None
        try:
            return response.json()
        except ValueError:
            return response.text

    async def _get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self._request("GET", path, params=params, headers=headers)

    async def _post(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self._request(
            "POST", path, json=json, data=data, params=params, headers=headers
        )

    async def _put(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self._request(
            "PUT", path, json=json, data=data, params=params, headers=headers
        )

    async def _patch(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self._request(
            "PATCH", path, json=json, data=data, params=params, headers=headers
        )

    async def _delete(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return await self._request("DELETE", path, params=params, headers=headers)

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
