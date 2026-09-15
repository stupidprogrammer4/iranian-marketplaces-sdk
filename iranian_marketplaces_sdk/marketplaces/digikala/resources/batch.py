"""Digikala batch: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import batch as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

INQUIRY_PATH = "/batch/inquiry"
UPDATE_VARIANTS_PATH = "/batch/variant/update"
UPDATE_ACTIVATION_PATH = "/batch/variant/activation/update"
UPDATE_STOCK_PATH = "/batch/variant/seller-stock/update"


class BatchSync(SyncResource):
    def inquiry(self, *, body: models.InquiryRequest) -> models.InquiryResponse:
        """POST /batch/inquiry. Scopes => self_settings."""
        response = self._request("POST", INQUIRY_PATH, body=body)
        return parse_response(models.InquiryResponse, response)

    def update_variants(
        self, *, body: models.UpdateVariantsRequest
    ) -> models.UpdateVariantsResponse:
        """POST /batch/variant/update. Scopes => variant."""
        response = self._request("POST", UPDATE_VARIANTS_PATH, body=body)
        return parse_response(models.UpdateVariantsResponse, response)

    def update_activation(
        self, *, body: models.UpdateActivationRequest
    ) -> models.UpdateActivationResponse:
        """POST /batch/variant/activation/update. Scopes => variant."""
        response = self._request("POST", UPDATE_ACTIVATION_PATH, body=body)
        return parse_response(models.UpdateActivationResponse, response)

    def update_stock(self, *, body: models.UpdateStockRequest) -> models.UpdateStockResponse:
        """POST /batch/variant/seller-stock/update. Scopes => variant."""
        response = self._request("POST", UPDATE_STOCK_PATH, body=body)
        return parse_response(models.UpdateStockResponse, response)


class BatchAsync(AsyncResource):
    async def inquiry(self, *, body: models.InquiryRequest) -> models.InquiryResponse:
        """POST /batch/inquiry. Scopes => self_settings."""
        response = await self._request("POST", INQUIRY_PATH, body=body)
        return parse_response(models.InquiryResponse, response)

    async def update_variants(
        self, *, body: models.UpdateVariantsRequest
    ) -> models.UpdateVariantsResponse:
        """POST /batch/variant/update. Scopes => variant."""
        response = await self._request("POST", UPDATE_VARIANTS_PATH, body=body)
        return parse_response(models.UpdateVariantsResponse, response)

    async def update_activation(
        self, *, body: models.UpdateActivationRequest
    ) -> models.UpdateActivationResponse:
        """POST /batch/variant/activation/update. Scopes => variant."""
        response = await self._request("POST", UPDATE_ACTIVATION_PATH, body=body)
        return parse_response(models.UpdateActivationResponse, response)

    async def update_stock(self, *, body: models.UpdateStockRequest) -> models.UpdateStockResponse:
        """POST /batch/variant/seller-stock/update. Scopes => variant."""
        response = await self._request("POST", UPDATE_STOCK_PATH, body=body)
        return parse_response(models.UpdateStockResponse, response)
