"""Digikala insight: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import insight as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

OVERVIEW_PATH = "/insight/overview"
TOP_DEACTIVATED_PATH = "/insight/top-deactivated"
SALES_TREND_PATH = "/insight/trend-sales-reports"
SALES_REPORT_PATH = "/insight/sales-reports"
EXPORT_PATH = "/insight/overview/export"


class InsightSync(SyncResource):
    def overview(self, *, query: models.OverviewQuery) -> models.OverviewResponse:
        """GET /insight/overview. Scopes => insight."""
        response = self._request("GET", OVERVIEW_PATH, query=query)
        return parse_response(models.OverviewResponse, response)

    def top_deactivated(self) -> models.TopDeactivatedResponse:
        """GET /insight/top-deactivated. Scopes => insight."""
        response = self._request("GET", TOP_DEACTIVATED_PATH)
        return parse_response(models.TopDeactivatedResponse, response)

    def sales_trend(self, *, query: models.SalesTrendQuery) -> models.SalesTrendResponse:
        """GET /insight/trend-sales-reports. Scopes => insight."""
        response = self._request("GET", SALES_TREND_PATH, query=query)
        return parse_response(models.SalesTrendResponse, response)

    def sales_report(self, *, query: models.SalesReportQuery) -> models.SalesReportResponse:
        """GET /insight/sales-reports. Scopes => insight."""
        response = self._request("GET", SALES_REPORT_PATH, query=query)
        return parse_response(models.SalesReportResponse, response)

    def export(self) -> models.ExportResponse:
        """POST /insight/overview/export. Scopes => insight."""
        response = self._request("POST", EXPORT_PATH)
        return parse_response(models.ExportResponse, response)


class InsightAsync(AsyncResource):
    async def overview(self, *, query: models.OverviewQuery) -> models.OverviewResponse:
        """GET /insight/overview. Scopes => insight."""
        response = await self._request("GET", OVERVIEW_PATH, query=query)
        return parse_response(models.OverviewResponse, response)

    async def top_deactivated(self) -> models.TopDeactivatedResponse:
        """GET /insight/top-deactivated. Scopes => insight."""
        response = await self._request("GET", TOP_DEACTIVATED_PATH)
        return parse_response(models.TopDeactivatedResponse, response)

    async def sales_trend(self, *, query: models.SalesTrendQuery) -> models.SalesTrendResponse:
        """GET /insight/trend-sales-reports. Scopes => insight."""
        response = await self._request("GET", SALES_TREND_PATH, query=query)
        return parse_response(models.SalesTrendResponse, response)

    async def sales_report(self, *, query: models.SalesReportQuery) -> models.SalesReportResponse:
        """GET /insight/sales-reports. Scopes => insight."""
        response = await self._request("GET", SALES_REPORT_PATH, query=query)
        return parse_response(models.SalesReportResponse, response)

    async def export(self) -> models.ExportResponse:
        """POST /insight/overview/export. Scopes => insight."""
        response = await self._request("POST", EXPORT_PATH)
        return parse_response(models.ExportResponse, response)
