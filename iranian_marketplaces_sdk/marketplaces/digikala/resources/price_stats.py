"""Digikala price stats: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import price_stats as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

BOUNDARY_PATH = "/pricing/price-stats/{variant_id}/boundary"


class PriceStatsSync(SyncResource):
    def boundary(
        self, variant_id: int, *, query: models.BoundaryQuery | None = None
    ) -> models.BoundaryResponse:
        """GET /pricing/price-stats/{variant_id}/boundary. Scopes => promotion, variant."""
        response = self._request(
            "GET", BOUNDARY_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.BoundaryResponse, response)


class PriceStatsAsync(AsyncResource):
    async def boundary(
        self, variant_id: int, *, query: models.BoundaryQuery | None = None
    ) -> models.BoundaryResponse:
        """GET /pricing/price-stats/{variant_id}/boundary. Scopes => promotion, variant."""
        response = await self._request(
            "GET", BOUNDARY_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.BoundaryResponse, response)
