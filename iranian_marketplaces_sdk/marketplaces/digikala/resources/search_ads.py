"""Digikala search ads: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import search_ads as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/search-ads/campaigns"
CREATE_PATH = "/search-ads/campaigns"
GET_PATH = "/search-ads/campaigns/{campaignId}"
RECOMMENDED_PRODUCTS_PATH = "/search-ads/campaigns/recommended-products"
UPDATE_PATH = "/search-ads/campaigns/{campaign_id}"
UPDATE_STATUS_PATH = "/search-ads/campaigns/{campaignId}/status"


class SearchAdsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /search-ads/campaigns. Scopes => search_ads."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /search-ads/campaigns. Scopes => search_ads."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def get(self, campaign_id: int) -> models.GetResponse:
        """GET /search-ads/campaigns/{campaignId}. Scopes => search_ads."""
        response = self._request("GET", GET_PATH.format(campaignId=path_value(campaign_id)))
        return parse_response(models.GetResponse, response)

    def recommended_products(
        self, *, query: models.RecommendedProductsQuery | None = None
    ) -> models.RecommendedProductsResponse:
        """GET /search-ads/campaigns/recommended-products. Scopes => search_ads."""
        response = self._request("GET", RECOMMENDED_PRODUCTS_PATH, query=query)
        return parse_response(models.RecommendedProductsResponse, response)

    def update(self, campaign_id: int, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /search-ads/campaigns/{campaign_id}. Scopes => search_ads."""
        response = self._request(
            "PUT", UPDATE_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    def update_status(
        self, campaign_id: int, *, body: models.UpdateStatusRequest
    ) -> models.UpdateStatusResponse:
        """PATCH /search-ads/campaigns/{campaignId}/status. Scopes => search_ads."""
        response = self._request(
            "PATCH", UPDATE_STATUS_PATH.format(campaignId=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateStatusResponse, response)


class SearchAdsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /search-ads/campaigns. Scopes => search_ads."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /search-ads/campaigns. Scopes => search_ads."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def get(self, campaign_id: int) -> models.GetResponse:
        """GET /search-ads/campaigns/{campaignId}. Scopes => search_ads."""
        response = await self._request("GET", GET_PATH.format(campaignId=path_value(campaign_id)))
        return parse_response(models.GetResponse, response)

    async def recommended_products(
        self, *, query: models.RecommendedProductsQuery | None = None
    ) -> models.RecommendedProductsResponse:
        """GET /search-ads/campaigns/recommended-products. Scopes => search_ads."""
        response = await self._request("GET", RECOMMENDED_PRODUCTS_PATH, query=query)
        return parse_response(models.RecommendedProductsResponse, response)

    async def update(
        self, campaign_id: int, *, body: models.UpdateRequest
    ) -> models.UpdateResponse:
        """PUT /search-ads/campaigns/{campaign_id}. Scopes => search_ads."""
        response = await self._request(
            "PUT", UPDATE_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    async def update_status(
        self, campaign_id: int, *, body: models.UpdateStatusRequest
    ) -> models.UpdateStatusResponse:
        """PATCH /search-ads/campaigns/{campaignId}/status. Scopes => search_ads."""
        response = await self._request(
            "PATCH", UPDATE_STATUS_PATH.format(campaignId=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateStatusResponse, response)
