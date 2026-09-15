"""Digikala commissions: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import commissions as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

LIST_PATH = "/commissions/"


class CommissionsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /commissions/. Scopes => commission."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)


class CommissionsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /commissions/. Scopes => commission."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)
