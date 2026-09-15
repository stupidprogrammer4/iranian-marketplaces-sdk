"""Digikala lightning deals: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import lightning_deals as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

PRODUCTS_PATH = "/lightening-deal/products"
GET_PRODUCT_PATH = "/lightening-deal/products/{product_id}"
PROMOTIONS_PATH = "/lightening-deal/promotions"
GET_PROMOTIONS_PATH = "/lightening-deal/promotions/{productId}"
CREATE_BIDS_PATH = "/lightening-deal/bids"
BIDS_PATH = "/lightening-deal/bids"
BIDS_SUMMARY_PATH = "/lightening-deal/bidsSummary"
CHECK_DUPLICATE_PATH = "/lightening-deal/check-duplicate-dkp-in-promotion/{promotionId}/{productId}"
UPDATE_PAYMENT_METHOD_PATH = "/lightening-deal/bids/{bidId}/payment-method"


class LightningDealsSync(SyncResource):
    def products(self, *, query: models.ProductsQuery | None = None) -> models.ProductsResponse:
        """GET /lightening-deal/products. Scopes => lightening_deal."""
        response = self._request("GET", PRODUCTS_PATH, query=query)
        return parse_response(models.ProductsResponse, response)

    def get_product(
        self, product_id: int, *, query: models.GetProductQuery | None = None
    ) -> models.GetProductResponse:
        """GET /lightening-deal/products/{product_id}. Scopes => lightening_deal."""
        response = self._request(
            "GET", GET_PRODUCT_PATH.format(product_id=path_value(product_id)), query=query
        )
        return parse_response(models.GetProductResponse, response)

    def promotions(self) -> models.PromotionsResponse:
        """GET /lightening-deal/promotions. Scopes => lightening_deal."""
        response = self._request("GET", PROMOTIONS_PATH)
        return parse_response(models.PromotionsResponse, response)

    def get_promotions(self, product_id: int) -> models.GetPromotionsResponse:
        """GET /lightening-deal/promotions/{productId}. Scopes => lightening_deal."""
        response = self._request(
            "GET", GET_PROMOTIONS_PATH.format(productId=path_value(product_id))
        )
        return parse_response(models.GetPromotionsResponse, response)

    def create_bids(self, *, body: models.CreateBidsRequest) -> models.CreateBidsResponse:
        """POST /lightening-deal/bids. Scopes => lightening_deal."""
        response = self._request("POST", CREATE_BIDS_PATH, body=body)
        return parse_response(models.CreateBidsResponse, response)

    def bids(self, *, query: models.BidsQuery | None = None) -> models.BidsResponse:
        """GET /lightening-deal/bids. Scopes => lightening_deal."""
        response = self._request("GET", BIDS_PATH, query=query)
        return parse_response(models.BidsResponse, response)

    def bids_summary(self) -> models.BidsSummaryResponse:
        """GET /lightening-deal/bidsSummary. Scopes => lightening_deal."""
        response = self._request("GET", BIDS_SUMMARY_PATH)
        return parse_response(models.BidsSummaryResponse, response)

    def check_duplicate(
        self, promotion_id: int, product_id: int, *, body: models.CheckDuplicateRequest
    ) -> models.CheckDuplicateResponse:
        """GET /lightening-deal/check-duplicate-dkp-in-promotion/{promotionId}/{productId}.
        Scopes => lightening_deal."""
        response = self._request(
            "GET",
            CHECK_DUPLICATE_PATH.format(
                promotionId=path_value(promotion_id), productId=path_value(product_id)
            ),
            body=body,
        )
        return parse_response(models.CheckDuplicateResponse, response)

    def update_payment_method(
        self, bid_id: int, *, body: models.UpdatePaymentMethodRequest
    ) -> RawResponse:
        """POST /lightening-deal/bids/{bidId}/payment-method. Scopes => lightening_deal.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "POST", UPDATE_PAYMENT_METHOD_PATH.format(bidId=path_value(bid_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)


class LightningDealsAsync(AsyncResource):
    async def products(
        self, *, query: models.ProductsQuery | None = None
    ) -> models.ProductsResponse:
        """GET /lightening-deal/products. Scopes => lightening_deal."""
        response = await self._request("GET", PRODUCTS_PATH, query=query)
        return parse_response(models.ProductsResponse, response)

    async def get_product(
        self, product_id: int, *, query: models.GetProductQuery | None = None
    ) -> models.GetProductResponse:
        """GET /lightening-deal/products/{product_id}. Scopes => lightening_deal."""
        response = await self._request(
            "GET", GET_PRODUCT_PATH.format(product_id=path_value(product_id)), query=query
        )
        return parse_response(models.GetProductResponse, response)

    async def promotions(self) -> models.PromotionsResponse:
        """GET /lightening-deal/promotions. Scopes => lightening_deal."""
        response = await self._request("GET", PROMOTIONS_PATH)
        return parse_response(models.PromotionsResponse, response)

    async def get_promotions(self, product_id: int) -> models.GetPromotionsResponse:
        """GET /lightening-deal/promotions/{productId}. Scopes => lightening_deal."""
        response = await self._request(
            "GET", GET_PROMOTIONS_PATH.format(productId=path_value(product_id))
        )
        return parse_response(models.GetPromotionsResponse, response)

    async def create_bids(self, *, body: models.CreateBidsRequest) -> models.CreateBidsResponse:
        """POST /lightening-deal/bids. Scopes => lightening_deal."""
        response = await self._request("POST", CREATE_BIDS_PATH, body=body)
        return parse_response(models.CreateBidsResponse, response)

    async def bids(self, *, query: models.BidsQuery | None = None) -> models.BidsResponse:
        """GET /lightening-deal/bids. Scopes => lightening_deal."""
        response = await self._request("GET", BIDS_PATH, query=query)
        return parse_response(models.BidsResponse, response)

    async def bids_summary(self) -> models.BidsSummaryResponse:
        """GET /lightening-deal/bidsSummary. Scopes => lightening_deal."""
        response = await self._request("GET", BIDS_SUMMARY_PATH)
        return parse_response(models.BidsSummaryResponse, response)

    async def check_duplicate(
        self, promotion_id: int, product_id: int, *, body: models.CheckDuplicateRequest
    ) -> models.CheckDuplicateResponse:
        """GET /lightening-deal/check-duplicate-dkp-in-promotion/{promotionId}/{productId}.
        Scopes => lightening_deal."""
        response = await self._request(
            "GET",
            CHECK_DUPLICATE_PATH.format(
                promotionId=path_value(promotion_id), productId=path_value(product_id)
            ),
            body=body,
        )
        return parse_response(models.CheckDuplicateResponse, response)

    async def update_payment_method(
        self, bid_id: int, *, body: models.UpdatePaymentMethodRequest
    ) -> RawResponse:
        """POST /lightening-deal/bids/{bidId}/payment-method. Scopes => lightening_deal.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "POST", UPDATE_PAYMENT_METHOD_PATH.format(bidId=path_value(bid_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)
