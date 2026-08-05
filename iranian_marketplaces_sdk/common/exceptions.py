"""One error hierarchy across every marketplace.

Everything the SDK raises inherits from :class:`MarketplaceError`, so a caller can catch one base
type or narrow down to the exact failure. The split that matters is *where* the request stopped:

* :class:`ConfigurationError` — it never left, because the credentials could not build a client.
* :class:`NetworkError` — it left and no HTTP response came back.
* :class:`APIError` and its subclasses — the marketplace answered, and said no.
* :class:`ResponseValidationError` — the marketplace answered with something that is not the
  documented shape. The undecoded body travels on the exception, so a schema drift upstream costs
  you a caught exception rather than the data.
"""

from typing import Any


class MarketplaceError(Exception):
    """Base class for every error raised by the SDK."""


class ConfigurationError(MarketplaceError):
    """An engine was constructed with missing or invalid credentials.

    Raised at construction, before any network call, so a half-configured client fails while you
    are wiring it up rather than in the middle of a stock sync.
    """


class NetworkError(MarketplaceError):
    """The request never produced an HTTP response.

    Wraps transport-level failures: DNS, connection resets, TLS, and timeouts.
    """


class APIError(MarketplaceError):
    """The marketplace answered with an unsuccessful HTTP status."""

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
        """The HTTP status the marketplace returned."""
        self.response_body = response_body
        """The decoded JSON body if there was one, otherwise the raw text."""
        self.request_url = request_url
        """The fully qualified URL that produced the error."""

    def __str__(self) -> str:
        base = super().__str__()
        if self.status_code is not None:
            return f"[{self.status_code}] {base}"
        return base


class AuthenticationError(APIError):
    """401/403 — the token is missing, expired, or lacks the scope for this endpoint."""


class NotFoundError(APIError):
    """404 — the requested resource does not exist."""


class RateLimitError(APIError):
    """429 — the client is being throttled."""

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
        """Seconds to wait before retrying, when the marketplace sent a ``Retry-After`` header in
        the delta-seconds form. ``None`` when it sent none, or sent an HTTP-date the SDK does not
        parse — pick your own backoff in that case."""


class ServerError(APIError):
    """5xx — the marketplace failed to handle a request it accepted."""


class ResponseValidationError(MarketplaceError):
    """The marketplace answered with a body that does not match the documented schema.

    These APIs are living systems: a field goes nullable, an object becomes a list, a new
    calculation type appears. Response models are permissive about *extra* keys precisely so that
    additions never break a caller — this fires only when something that must be there is missing
    or has the wrong type.

    The decoded body is on :attr:`raw`, so a caller who needs the data more than the type can
    still read it, and a caller who needs to report the drift has something to paste into a ticket.
    """

    def __init__(self, message: str, *, model: str, raw: Any = None, errors: Any = None) -> None:
        super().__init__(message)
        self.model = model
        """Name of the model that failed to validate."""
        self.raw = raw
        """The decoded response body, untouched."""
        self.errors = errors
        """Pydantic's per-field error list, when the failure came from validation."""
