"""TypedDicts for the Digikala health-check endpoint."""

from typing import TypedDict

from .common import RateLimit

__all__ = ["HealthCheckData", "HealthCheckResponse"]


class HealthCheckData(TypedDict):
    """The ``data`` payload of a health-check response."""

    name: str
    mode: str
    time: str
    routes: list[str]
    rate_limit: RateLimit


class HealthCheckResponse(TypedDict):
    """Full response body returned by the Digikala health-check endpoint."""

    status: str
    data: HealthCheckData
