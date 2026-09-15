"""Digikala search ads v2: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import search_ads_v2 as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

PRODUCTS_PATH = "/search-ads/v2/products"
SETTINGS_PATH = "/search-ads/v2/setting"
CREATE_PATH = "/search-ads/v2/campaigns"
LIST_PATH = "/search-ads/v2/campaigns"
GET_PATH = "/search-ads/v2/campaigns/{campaign_id}"
UPDATE_PATH = "/search-ads/v2/campaigns/{campaign_id}"
REPORT_PATH = "/search-ads/v2/campaigns/{campaign_id}/report"
OVERVIEW_PATH = "/search-ads/v2/campaigns/{campaign_id}/overview"
CAMPAIGN_PRODUCT_OVERVIEW_PATH = (
    "/search-ads/v2/campaigns/{campaign_id}/products/{product_id}/overview"
)
PRODUCT_OVERVIEW_PATH = "/search-ads/v2/products/{product_id}/overview"
SELLER_OVERVIEW_PATH = "/search-ads/v2/seller/overview"
UPDATE_STATUS_PATH = "/search-ads/v2/campaigns/{campaign_id}/status/{status}"
UPDATE_BID_PATH = "/search-ads/v2/campaigns/{campaign_id}/bid"
ADD_PRODUCTS_PATH = "/search-ads/v2/campaigns/{campaign_id}/products"
UPDATE_PRODUCT_STATUS_PATH = "/search-ads/v2/campaigns/{campaign_id}/products/{product_id}/status"


class SearchAdsV2Sync(SyncResource):
    def products(self, *, query: models.ProductsQuery | None = None) -> models.ProductsResponse:
        """GET /search-ads/v2/products. Scopes => search_ads."""
        response = self._request("GET", PRODUCTS_PATH, query=query, separators={"search[q]": ","})
        return parse_response(models.ProductsResponse, response)

    def settings(self, *, query: models.SettingsQuery | None = None) -> models.SettingsResponse:
        """GET /search-ads/v2/setting. Scopes => search_ads."""
        response = self._request("GET", SETTINGS_PATH, query=query)
        return parse_response(models.SettingsResponse, response)

    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /search-ads/v2/campaigns. Scopes => search_ads."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /search-ads/v2/campaigns. Scopes => search_ads."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def get(self, campaign_id: int) -> models.GetResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}. Scopes => search_ads."""
        response = self._request("GET", GET_PATH.format(campaign_id=path_value(campaign_id)))
        return parse_response(models.GetResponse, response)

    def update(self, campaign_id: int, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}. Scopes => search_ads."""
        response = self._request(
            "PATCH", UPDATE_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    def report(
        self, campaign_id: int, *, query: models.ReportQuery | None = None
    ) -> models.ReportResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/report. Scopes => search_ads."""
        response = self._request(
            "GET", REPORT_PATH.format(campaign_id=path_value(campaign_id)), query=query
        )
        return parse_response(models.ReportResponse, response)

    def overview(
        self, campaign_id: int, *, query: models.OverviewQuery | None = None
    ) -> models.OverviewResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/overview. Scopes => search_ads."""
        response = self._request(
            "GET", OVERVIEW_PATH.format(campaign_id=path_value(campaign_id)), query=query
        )
        return parse_response(models.OverviewResponse, response)

    def campaign_product_overview(
        self,
        campaign_id: int,
        product_id: int,
        *,
        query: models.CampaignProductOverviewQuery | None = None,
    ) -> models.CampaignProductOverviewResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/products/{product_id}/overview. Scopes =>
        search_ads."""
        response = self._request(
            "GET",
            CAMPAIGN_PRODUCT_OVERVIEW_PATH.format(
                campaign_id=path_value(campaign_id), product_id=path_value(product_id)
            ),
            query=query,
        )
        return parse_response(models.CampaignProductOverviewResponse, response)

    def product_overview(
        self, product_id: int, *, query: models.ProductOverviewQuery | None = None
    ) -> models.ProductOverviewResponse:
        """GET /search-ads/v2/products/{product_id}/overview. Scopes => search_ads."""
        response = self._request(
            "GET", PRODUCT_OVERVIEW_PATH.format(product_id=path_value(product_id)), query=query
        )
        return parse_response(models.ProductOverviewResponse, response)

    def seller_overview(
        self, *, query: models.SellerOverviewQuery | None = None
    ) -> models.SellerOverviewResponse:
        """GET /search-ads/v2/seller/overview. Scopes => search_ads."""
        response = self._request("GET", SELLER_OVERVIEW_PATH, query=query)
        return parse_response(models.SellerOverviewResponse, response)

    def update_status(self, campaign_id: int, status: str) -> models.UpdateStatusResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/status/{status}. Scopes => search_ads."""
        response = self._request(
            "PATCH",
            UPDATE_STATUS_PATH.format(
                campaign_id=path_value(campaign_id), status=path_value(status)
            ),
        )
        return parse_response(models.UpdateStatusResponse, response)

    def update_bid(
        self, campaign_id: int, *, body: models.UpdateBidRequest
    ) -> models.UpdateBidResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/bid. Scopes => search_ads."""
        response = self._request(
            "PATCH", UPDATE_BID_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateBidResponse, response)

    def add_products(
        self, campaign_id: int, *, body: models.AddProductsRequest
    ) -> models.AddProductsResponse:
        """POST /search-ads/v2/campaigns/{campaign_id}/products. Scopes => search_ads."""
        response = self._request(
            "POST", ADD_PRODUCTS_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.AddProductsResponse, response)

    def update_product_status(
        self, campaign_id: int, product_id: int, *, body: models.UpdateProductStatusRequest
    ) -> models.UpdateProductStatusResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/products/{product_id}/status. Scopes =>
        search_ads."""
        response = self._request(
            "PATCH",
            UPDATE_PRODUCT_STATUS_PATH.format(
                campaign_id=path_value(campaign_id), product_id=path_value(product_id)
            ),
            body=body,
        )
        return parse_response(models.UpdateProductStatusResponse, response)


class SearchAdsV2Async(AsyncResource):
    async def products(
        self, *, query: models.ProductsQuery | None = None
    ) -> models.ProductsResponse:
        """GET /search-ads/v2/products. Scopes => search_ads."""
        response = await self._request(
            "GET", PRODUCTS_PATH, query=query, separators={"search[q]": ","}
        )
        return parse_response(models.ProductsResponse, response)

    async def settings(
        self, *, query: models.SettingsQuery | None = None
    ) -> models.SettingsResponse:
        """GET /search-ads/v2/setting. Scopes => search_ads."""
        response = await self._request("GET", SETTINGS_PATH, query=query)
        return parse_response(models.SettingsResponse, response)

    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /search-ads/v2/campaigns. Scopes => search_ads."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /search-ads/v2/campaigns. Scopes => search_ads."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def get(self, campaign_id: int) -> models.GetResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}. Scopes => search_ads."""
        response = await self._request("GET", GET_PATH.format(campaign_id=path_value(campaign_id)))
        return parse_response(models.GetResponse, response)

    async def update(
        self, campaign_id: int, *, body: models.UpdateRequest
    ) -> models.UpdateResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}. Scopes => search_ads."""
        response = await self._request(
            "PATCH", UPDATE_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    async def report(
        self, campaign_id: int, *, query: models.ReportQuery | None = None
    ) -> models.ReportResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/report. Scopes => search_ads."""
        response = await self._request(
            "GET", REPORT_PATH.format(campaign_id=path_value(campaign_id)), query=query
        )
        return parse_response(models.ReportResponse, response)

    async def overview(
        self, campaign_id: int, *, query: models.OverviewQuery | None = None
    ) -> models.OverviewResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/overview. Scopes => search_ads."""
        response = await self._request(
            "GET", OVERVIEW_PATH.format(campaign_id=path_value(campaign_id)), query=query
        )
        return parse_response(models.OverviewResponse, response)

    async def campaign_product_overview(
        self,
        campaign_id: int,
        product_id: int,
        *,
        query: models.CampaignProductOverviewQuery | None = None,
    ) -> models.CampaignProductOverviewResponse:
        """GET /search-ads/v2/campaigns/{campaign_id}/products/{product_id}/overview. Scopes =>
        search_ads."""
        response = await self._request(
            "GET",
            CAMPAIGN_PRODUCT_OVERVIEW_PATH.format(
                campaign_id=path_value(campaign_id), product_id=path_value(product_id)
            ),
            query=query,
        )
        return parse_response(models.CampaignProductOverviewResponse, response)

    async def product_overview(
        self, product_id: int, *, query: models.ProductOverviewQuery | None = None
    ) -> models.ProductOverviewResponse:
        """GET /search-ads/v2/products/{product_id}/overview. Scopes => search_ads."""
        response = await self._request(
            "GET", PRODUCT_OVERVIEW_PATH.format(product_id=path_value(product_id)), query=query
        )
        return parse_response(models.ProductOverviewResponse, response)

    async def seller_overview(
        self, *, query: models.SellerOverviewQuery | None = None
    ) -> models.SellerOverviewResponse:
        """GET /search-ads/v2/seller/overview. Scopes => search_ads."""
        response = await self._request("GET", SELLER_OVERVIEW_PATH, query=query)
        return parse_response(models.SellerOverviewResponse, response)

    async def update_status(self, campaign_id: int, status: str) -> models.UpdateStatusResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/status/{status}. Scopes => search_ads."""
        response = await self._request(
            "PATCH",
            UPDATE_STATUS_PATH.format(
                campaign_id=path_value(campaign_id), status=path_value(status)
            ),
        )
        return parse_response(models.UpdateStatusResponse, response)

    async def update_bid(
        self, campaign_id: int, *, body: models.UpdateBidRequest
    ) -> models.UpdateBidResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/bid. Scopes => search_ads."""
        response = await self._request(
            "PATCH", UPDATE_BID_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.UpdateBidResponse, response)

    async def add_products(
        self, campaign_id: int, *, body: models.AddProductsRequest
    ) -> models.AddProductsResponse:
        """POST /search-ads/v2/campaigns/{campaign_id}/products. Scopes => search_ads."""
        response = await self._request(
            "POST", ADD_PRODUCTS_PATH.format(campaign_id=path_value(campaign_id)), body=body
        )
        return parse_response(models.AddProductsResponse, response)

    async def update_product_status(
        self, campaign_id: int, product_id: int, *, body: models.UpdateProductStatusRequest
    ) -> models.UpdateProductStatusResponse:
        """PATCH /search-ads/v2/campaigns/{campaign_id}/products/{product_id}/status. Scopes =>
        search_ads."""
        response = await self._request(
            "PATCH",
            UPDATE_PRODUCT_STATUS_PATH.format(
                campaign_id=path_value(campaign_id), product_id=path_value(product_id)
            ),
            body=body,
        )
        return parse_response(models.UpdateProductStatusResponse, response)
