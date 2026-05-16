"""Synchronous base client every marketplace ``engine.py`` builds on.

Concrete engines subclass :class:`BaseClient`, pass their ``base_url`` and
authentication headers up to ``__init__``, and use the ``_get`` / ``_post`` /
``_request`` helpers to talk to the marketplace. Subclasses remain responsible
for requiring their own credentials explicitly in their constructors.
"""

from __future__ import annotations

from types import TracebackType
from typing import Any, Mapping

import httpx

from ._http import build_api_error
from .exceptions import NetworkError

DEFAULT_TIMEOUT = 30.0


class BaseClient:
    """Thin wrapper around :class:`httpx.Client` with unified error handling."""

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

    @property
    def base_url(self) -> str:
        return self._base_url

    def _request(
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
            response = self._client.request(
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

    def _get(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self._request("GET", path, params=params, headers=headers)

    def _post(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self._request(
            "POST", path, json=json, data=data, params=params, headers=headers
        )

    def _put(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self._request(
            "PUT", path, json=json, data=data, params=params, headers=headers
        )

    def _patch(
        self,
        path: str,
        *,
        json: Any = None,
        data: Any = None,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self._request(
            "PATCH", path, json=json, data=data, params=params, headers=headers
        )

    def _delete(
        self,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        return self._request("DELETE", path, params=params, headers=headers)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "BaseClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()
