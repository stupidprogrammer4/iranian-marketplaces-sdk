"""Exception hierarchy shared by all marketplace engines.

Every error raised by the SDK inherits from :class:`MarketplaceError`, so
callers can catch a single base type or narrow down to a specific failure.
"""

from __future__ import annotations

from typing import Any


class MarketplaceError(Exception):
    """Base class for every error raised by the SDK."""


class ConfigurationError(MarketplaceError):
    """Raised when an engine is constructed with missing/invalid credentials."""


class APIError(MarketplaceError):
    """Raised when the marketplace returns an unsuccessful HTTP response.

    Attributes:
        status_code: The HTTP status code returned by the marketplace.
        response_body: The parsed JSON body if available, otherwise raw text.
        request_url: The fully qualified URL that produced the error.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        response_body: Any = None,
        request_url: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body
        self.request_url = request_url

    def __str__(self) -> str:
        base = super().__str__()
        if self.status_code is not None:
            return f"[{self.status_code}] {base}"
        return base


class AuthenticationError(APIError):
    """Raised on 401/403 responses (invalid or expired credentials)."""


class NotFoundError(APIError):
    """Raised on 404 responses (the requested resource does not exist)."""


class RateLimitError(APIError):
    """Raised on 429 responses (the client is being throttled).

    Attributes:
        retry_after: Seconds to wait before retrying, if the marketplace
            provided a ``Retry-After`` header.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        response_body: Any = None,
        request_url: str | None = None,
        retry_after: float | None = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status_code,
            response_body=response_body,
            request_url=request_url,
        )
        self.retry_after = retry_after


class ServerError(APIError):
    """Raised on 5xx responses (the marketplace failed to handle the request)."""


class NetworkError(MarketplaceError):
    """Raised when the request never produced an HTTP response.

    This wraps transport-level failures such as DNS errors, connection
    resets, and timeouts.
    """
