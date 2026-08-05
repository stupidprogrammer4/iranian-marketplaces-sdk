"""Digikala — the health-check endpoint.

Unauthenticated, and the cheapest way to confirm the base URL is reachable and to read the
seller's current rate-limit window before starting a batch.
"""

from iranian_marketplaces_sdk.common.data import ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import RateLimit

__all__ = ["HealthCheckData", "HealthCheckResponse"]


class HealthCheckData(ResponseSchema):
    """The ``data`` payload of a health-check response.

    ``routes`` is the list of endpoints this deployment serves — worth reading when a call 404s
    that the documentation says exists.
    """

    name: str
    mode: str
    time: str
    routes: list[str]
    rate_limit: RateLimit


class HealthCheckResponse(ResponseSchema):
    """Full response body returned by the Digikala health-check endpoint."""

    status: str
    data: HealthCheckData
