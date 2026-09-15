"""Digikala multi pricing: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import multi_pricing as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

ESTIMATE_PATH = "/pricing/multi-pricing/estimate"


class MultiPricingSync(SyncResource):
    def estimate(self, *, query: models.EstimateQuery) -> models.EstimateResponse:
        """GET /pricing/multi-pricing/estimate. Scopes => variant."""
        response = self._request("GET", ESTIMATE_PATH, query=query)
        return parse_response(models.EstimateResponse, response)


class MultiPricingAsync(AsyncResource):
    async def estimate(self, *, query: models.EstimateQuery) -> models.EstimateResponse:
        """GET /pricing/multi-pricing/estimate. Scopes => variant."""
        response = await self._request("GET", ESTIMATE_PATH, query=query)
        return parse_response(models.EstimateResponse, response)
