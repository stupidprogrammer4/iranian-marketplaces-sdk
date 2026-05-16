"""Internal helpers shared by the sync and async base clients."""

from __future__ import annotations

from typing import Any

import httpx

from .exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
)


def _extract_body(response: httpx.Response) -> Any:
    """Return the JSON body when possible, falling back to raw text."""
    try:
        return response.json()
    except (ValueError, UnicodeDecodeError):
        return response.text


def _parse_retry_after(response: httpx.Response) -> float | None:
    raw = response.headers.get("Retry-After")
    if raw is None:
        return None
    try:
        return float(raw)
    except ValueError:
        # HTTP-date form is not supported; let the caller decide a backoff.
        return None


def build_api_error(response: httpx.Response) -> APIError:
    """Map an unsuccessful :class:`httpx.Response` to a specific exception."""
    status = response.status_code
    body = _extract_body(response)
    url = str(response.request.url) if response.request is not None else None
    message = f"Request to {url or 'marketplace'} failed"

    if status in (401, 403):
        return AuthenticationError(
            message, status_code=status, response_body=body, request_url=url
        )
    if status == 404:
        return NotFoundError(
            message, status_code=status, response_body=body, request_url=url
        )
    if status == 429:
        return RateLimitError(
            message,
            status_code=status,
            response_body=body,
            request_url=url,
            retry_after=_parse_retry_after(response),
        )
    if status >= 500:
        return ServerError(
            message, status_code=status, response_body=body, request_url=url
        )
    return APIError(
        message, status_code=status, response_body=body, request_url=url
    )
