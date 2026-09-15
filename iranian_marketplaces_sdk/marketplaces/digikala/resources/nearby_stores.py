"""Digikala nearby stores: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import nearby_stores as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
)

LIST_PATH = "/near-by-stores"
CUSTOMER_NOT_RESPONDING_PATH = "/near-by-stores/customer-not-respond"


class NearbyStoresSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /near-by-stores. Scopes => sbs_orders."""
        response = self._request(
            "GET", LIST_PATH, query=query, separators={"search[category_ids]": ","}
        )
        return parse_response(models.ListResponse, response)

    def customer_not_responding(self, *, body: models.CustomerNotRespondingRequest) -> RawResponse:
        """POST /near-by-stores/customer-not-respond. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", CUSTOMER_NOT_RESPONDING_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class NearbyStoresAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /near-by-stores. Scopes => sbs_orders."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[category_ids]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def customer_not_responding(
        self, *, body: models.CustomerNotRespondingRequest
    ) -> RawResponse:
        """POST /near-by-stores/customer-not-respond. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", CUSTOMER_NOT_RESPONDING_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
