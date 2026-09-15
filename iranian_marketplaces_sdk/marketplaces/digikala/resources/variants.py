"""Digikala variants: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import variants as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/variants"
GET_PATH = "/variants/{variant_id}"
UPDATE_PATH = "/variants/{variant_id}"
UPDATE_B2B_ACTIVATION_PATH = "/variants/b2b-activation"
EXPORT_PATH = "/variants/export"
GET_GOLD_PATH = "/variants/{variant_id}/gold"
UPDATE_GOLD_PATH = "/variants/{variant_id}/gold"
CALCULATE_PRICE_PATH = "/variants/{variant_id}/price-calculator"
UPDATE_ACTIVATION_PATH = "/variants/{variant_id}/activation"
GET_B2B_PRICES_PATH = "/variants/{variant_id}/b2b-prices"
UPDATE_B2B_PRICES_PATH = "/variants/{variant_id}/b2b-prices"
ARCHIVE_PATH = "/variants/{variant_id}/archive"
GET_SELLER_STOCK_PATH = "/variants/{variant_id}/seller-stock"
UPDATE_SELLER_STOCK_PATH = "/variants/{variant_id}/seller-stock"
UPDATE_SELLING_PRICE_PATH = "/variants/selling-price"


class VariantsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /variants. Scopes => variant."""
        response = self._request(
            "GET",
            LIST_PATH,
            query=query,
            separators={
                "search[ids]": "_",
                "search[category_ids]": ",",
                "search[price_terms]": ",",
            },
        )
        return parse_response(models.ListResponse, response)

    def get(self, variant_id: int) -> models.GetResponse:
        """GET /variants/{variant_id}. Scopes => variant."""
        response = self._request("GET", GET_PATH.format(variant_id=path_value(variant_id)))
        return parse_response(models.GetResponse, response)

    def update(
        self, variant_id: int, *, body: models.UpdateRequest | None = None
    ) -> models.UpdateResponse:
        """PUT /variants/{variant_id}. Scopes => variant."""
        response = self._request(
            "PUT", UPDATE_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    def update_b2b_activation(
        self, *, body: models.UpdateB2bActivationRequest
    ) -> models.UpdateB2bActivationResponse:
        """PUT /variants/b2b-activation. Scopes => variant."""
        response = self._request("PUT", UPDATE_B2B_ACTIVATION_PATH, body=body)
        return parse_response(models.UpdateB2bActivationResponse, response)

    def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /variants/export. Scopes => variant."""
        response = self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)

    def get_gold(self, variant_id: int) -> models.GetGoldResponse:
        """GET /variants/{variant_id}/gold. Scopes => variant."""
        response = self._request("GET", GET_GOLD_PATH.format(variant_id=path_value(variant_id)))
        return parse_response(models.GetGoldResponse, response)

    def update_gold(
        self, variant_id: int, *, body: models.UpdateGoldRequest
    ) -> models.UpdateGoldResponse:
        """PUT /variants/{variant_id}/gold. Scopes => variant."""
        response = self._request(
            "PUT", UPDATE_GOLD_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateGoldResponse, response)

    def calculate_price(
        self, variant_id: int, *, query: models.CalculatePriceQuery
    ) -> models.CalculatePriceResponse:
        """GET /variants/{variant_id}/price-calculator. Scopes => variant."""
        response = self._request(
            "GET", CALCULATE_PRICE_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.CalculatePriceResponse, response)

    def update_activation(
        self, variant_id: int, *, body: models.UpdateActivationRequest
    ) -> models.UpdateActivationResponse:
        """PUT /variants/{variant_id}/activation. Scopes => variant."""
        response = self._request(
            "PUT", UPDATE_ACTIVATION_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateActivationResponse, response)

    def get_b2b_prices(self, variant_id: int) -> models.GetB2bPricesResponse:
        """GET /variants/{variant_id}/b2b-prices. Scopes => variant."""
        response = self._request(
            "GET", GET_B2B_PRICES_PATH.format(variant_id=path_value(variant_id))
        )
        return parse_response(models.GetB2bPricesResponse, response)

    def update_b2b_prices(
        self, variant_id: int, *, body: models.UpdateB2bPricesRequest
    ) -> models.UpdateB2bPricesResponse:
        """PUT /variants/{variant_id}/b2b-prices. Scopes => variant."""
        response = self._request(
            "PUT", UPDATE_B2B_PRICES_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateB2bPricesResponse, response)

    def archive(self, variant_id: int, *, body: models.ArchiveRequest) -> models.ArchiveResponse:
        """PUT /variants/{variant_id}/archive. Scopes => variant."""
        response = self._request(
            "PUT", ARCHIVE_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.ArchiveResponse, response)

    def get_seller_stock(self, variant_id: int) -> models.GetSellerStockResponse:
        """GET /variants/{variant_id}/seller-stock. Scopes => variant."""
        response = self._request(
            "GET", GET_SELLER_STOCK_PATH.format(variant_id=path_value(variant_id))
        )
        return parse_response(models.GetSellerStockResponse, response)

    def update_seller_stock(
        self, variant_id: int, *, body: models.UpdateSellerStockRequest
    ) -> models.UpdateSellerStockResponse:
        """PATCH /variants/{variant_id}/seller-stock. Scopes => variant."""
        response = self._request(
            "PATCH", UPDATE_SELLER_STOCK_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateSellerStockResponse, response)

    def update_selling_price(
        self, *, body: models.UpdateSellingPriceRequest
    ) -> models.UpdateSellingPriceResponse:
        """PATCH /variants/selling-price. Scopes => variant."""
        response = self._request("PATCH", UPDATE_SELLING_PRICE_PATH, body=body)
        return parse_response(models.UpdateSellingPriceResponse, response)


class VariantsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /variants. Scopes => variant."""
        response = await self._request(
            "GET",
            LIST_PATH,
            query=query,
            separators={
                "search[ids]": "_",
                "search[category_ids]": ",",
                "search[price_terms]": ",",
            },
        )
        return parse_response(models.ListResponse, response)

    async def get(self, variant_id: int) -> models.GetResponse:
        """GET /variants/{variant_id}. Scopes => variant."""
        response = await self._request("GET", GET_PATH.format(variant_id=path_value(variant_id)))
        return parse_response(models.GetResponse, response)

    async def update(
        self, variant_id: int, *, body: models.UpdateRequest | None = None
    ) -> models.UpdateResponse:
        """PUT /variants/{variant_id}. Scopes => variant."""
        response = await self._request(
            "PUT", UPDATE_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateResponse, response)

    async def update_b2b_activation(
        self, *, body: models.UpdateB2bActivationRequest
    ) -> models.UpdateB2bActivationResponse:
        """PUT /variants/b2b-activation. Scopes => variant."""
        response = await self._request("PUT", UPDATE_B2B_ACTIVATION_PATH, body=body)
        return parse_response(models.UpdateB2bActivationResponse, response)

    async def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /variants/export. Scopes => variant."""
        response = await self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)

    async def get_gold(self, variant_id: int) -> models.GetGoldResponse:
        """GET /variants/{variant_id}/gold. Scopes => variant."""
        response = await self._request(
            "GET", GET_GOLD_PATH.format(variant_id=path_value(variant_id))
        )
        return parse_response(models.GetGoldResponse, response)

    async def update_gold(
        self, variant_id: int, *, body: models.UpdateGoldRequest
    ) -> models.UpdateGoldResponse:
        """PUT /variants/{variant_id}/gold. Scopes => variant."""
        response = await self._request(
            "PUT", UPDATE_GOLD_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateGoldResponse, response)

    async def calculate_price(
        self, variant_id: int, *, query: models.CalculatePriceQuery
    ) -> models.CalculatePriceResponse:
        """GET /variants/{variant_id}/price-calculator. Scopes => variant."""
        response = await self._request(
            "GET", CALCULATE_PRICE_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.CalculatePriceResponse, response)

    async def update_activation(
        self, variant_id: int, *, body: models.UpdateActivationRequest
    ) -> models.UpdateActivationResponse:
        """PUT /variants/{variant_id}/activation. Scopes => variant."""
        response = await self._request(
            "PUT", UPDATE_ACTIVATION_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateActivationResponse, response)

    async def get_b2b_prices(self, variant_id: int) -> models.GetB2bPricesResponse:
        """GET /variants/{variant_id}/b2b-prices. Scopes => variant."""
        response = await self._request(
            "GET", GET_B2B_PRICES_PATH.format(variant_id=path_value(variant_id))
        )
        return parse_response(models.GetB2bPricesResponse, response)

    async def update_b2b_prices(
        self, variant_id: int, *, body: models.UpdateB2bPricesRequest
    ) -> models.UpdateB2bPricesResponse:
        """PUT /variants/{variant_id}/b2b-prices. Scopes => variant."""
        response = await self._request(
            "PUT", UPDATE_B2B_PRICES_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateB2bPricesResponse, response)

    async def archive(
        self, variant_id: int, *, body: models.ArchiveRequest
    ) -> models.ArchiveResponse:
        """PUT /variants/{variant_id}/archive. Scopes => variant."""
        response = await self._request(
            "PUT", ARCHIVE_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.ArchiveResponse, response)

    async def get_seller_stock(self, variant_id: int) -> models.GetSellerStockResponse:
        """GET /variants/{variant_id}/seller-stock. Scopes => variant."""
        response = await self._request(
            "GET", GET_SELLER_STOCK_PATH.format(variant_id=path_value(variant_id))
        )
        return parse_response(models.GetSellerStockResponse, response)

    async def update_seller_stock(
        self, variant_id: int, *, body: models.UpdateSellerStockRequest
    ) -> models.UpdateSellerStockResponse:
        """PATCH /variants/{variant_id}/seller-stock. Scopes => variant."""
        response = await self._request(
            "PATCH", UPDATE_SELLER_STOCK_PATH.format(variant_id=path_value(variant_id)), body=body
        )
        return parse_response(models.UpdateSellerStockResponse, response)

    async def update_selling_price(
        self, *, body: models.UpdateSellingPriceRequest
    ) -> models.UpdateSellingPriceResponse:
        """PATCH /variants/selling-price. Scopes => variant."""
        response = await self._request("PATCH", UPDATE_SELLING_PRICE_PATH, body=body)
        return parse_response(models.UpdateSellingPriceResponse, response)
