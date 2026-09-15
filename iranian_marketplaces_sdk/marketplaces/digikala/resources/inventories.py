"""Digikala inventories: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import inventories as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/inventories"
DEAD_STOCK_PATH = "/inventories/{product_variant_id}"
EXPORT_DEAD_STOCK_PATH = "/inventories/{product_variant_id}/export"
EXPORT_PATH = "/inventories/export"


class InventoriesSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /inventories. Scopes => inventory."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def dead_stock(
        self, product_variant_id: int, *, query: models.DeadStockQuery | None = None
    ) -> models.DeadStockResponse:
        """GET /inventories/{product_variant_id}. Scopes => inventory."""
        response = self._request(
            "GET",
            DEAD_STOCK_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.DeadStockResponse, response)

    def export_dead_stock(
        self, product_variant_id: int, *, query: models.ExportDeadStockQuery | None = None
    ) -> models.ExportDeadStockResponse:
        """GET /inventories/{product_variant_id}/export. Scopes => inventory."""
        response = self._request(
            "GET",
            EXPORT_DEAD_STOCK_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.ExportDeadStockResponse, response)

    def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /inventories/export. Scopes => inventory."""
        response = self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)


class InventoriesAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /inventories. Scopes => inventory."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def dead_stock(
        self, product_variant_id: int, *, query: models.DeadStockQuery | None = None
    ) -> models.DeadStockResponse:
        """GET /inventories/{product_variant_id}. Scopes => inventory."""
        response = await self._request(
            "GET",
            DEAD_STOCK_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.DeadStockResponse, response)

    async def export_dead_stock(
        self, product_variant_id: int, *, query: models.ExportDeadStockQuery | None = None
    ) -> models.ExportDeadStockResponse:
        """GET /inventories/{product_variant_id}/export. Scopes => inventory."""
        response = await self._request(
            "GET",
            EXPORT_DEAD_STOCK_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.ExportDeadStockResponse, response)

    async def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /inventories/export. Scopes => inventory."""
        response = await self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)
