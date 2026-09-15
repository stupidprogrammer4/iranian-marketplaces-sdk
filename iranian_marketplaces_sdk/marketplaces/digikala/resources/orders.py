"""Digikala orders: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import orders as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/orders"
STATISTICS_PATH = "/orders/statistics"
HISTORY_PATH = "/orders/history"
CANCEL_PATH = "/orders/{order_item_id}"


class OrdersSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /orders. Scopes => order."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def statistics(self) -> models.StatisticsResponse:
        """GET /orders/statistics. Scopes => order."""
        response = self._request("GET", STATISTICS_PATH)
        return parse_response(models.StatisticsResponse, response)

    def history(self, *, query: models.HistoryQuery | None = None) -> models.HistoryResponse:
        """GET /orders/history. Scopes => order."""
        response = self._request("GET", HISTORY_PATH, query=query)
        return parse_response(models.HistoryResponse, response)

    def cancel(self, order_item_id: int, *, body: models.CancelRequest) -> models.CancelResponse:
        """DELETE /orders/{order_item_id}. Scopes => order."""
        response = self._request(
            "DELETE", CANCEL_PATH.format(order_item_id=path_value(order_item_id)), body=body
        )
        return parse_response(models.CancelResponse, response)


class OrdersAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /orders. Scopes => order."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def statistics(self) -> models.StatisticsResponse:
        """GET /orders/statistics. Scopes => order."""
        response = await self._request("GET", STATISTICS_PATH)
        return parse_response(models.StatisticsResponse, response)

    async def history(self, *, query: models.HistoryQuery | None = None) -> models.HistoryResponse:
        """GET /orders/history. Scopes => order."""
        response = await self._request("GET", HISTORY_PATH, query=query)
        return parse_response(models.HistoryResponse, response)

    async def cancel(
        self, order_item_id: int, *, body: models.CancelRequest
    ) -> models.CancelResponse:
        """DELETE /orders/{order_item_id}. Scopes => order."""
        response = await self._request(
            "DELETE", CANCEL_PATH.format(order_item_id=path_value(order_item_id)), body=body
        )
        return parse_response(models.CancelResponse, response)
