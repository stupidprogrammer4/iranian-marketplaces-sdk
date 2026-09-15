"""Digikala commitments: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import commitments as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/commitments"
METADATA_PATH = "/commitments/metadata"
EXPORT_PATH = "/commitments/export"
EXPORT_REPORT_PATH = "/commitments/report/export"
GET_PATH = "/commitments/{variant_id}"


class CommitmentsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /commitments. Scopes => order."""
        response = self._request(
            "GET",
            LIST_PATH,
            query=query,
            separators={"search[category_ids]": ",", "search[shipping_nature_ids]": ","},
        )
        return parse_response(models.ListResponse, response)

    def metadata(self, *, query: models.MetadataQuery | None = None) -> models.MetadataResponse:
        """GET /commitments/metadata. Scopes => order."""
        response = self._request("GET", METADATA_PATH, query=query)
        return parse_response(models.MetadataResponse, response)

    def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /commitments/export. Scopes => order."""
        response = self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)

    def export_report(
        self, *, body: models.ExportReportRequest | None = None
    ) -> models.ExportReportResponse:
        """POST /commitments/report/export. Scopes => order."""
        response = self._request("POST", EXPORT_REPORT_PATH, body=body)
        return parse_response(models.ExportReportResponse, response)

    def get(self, variant_id: int, *, query: models.GetQuery | None = None) -> models.GetResponse:
        """GET /commitments/{variant_id}. Scopes => order."""
        response = self._request(
            "GET", GET_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.GetResponse, response)


class CommitmentsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /commitments. Scopes => order."""
        response = await self._request(
            "GET",
            LIST_PATH,
            query=query,
            separators={"search[category_ids]": ",", "search[shipping_nature_ids]": ","},
        )
        return parse_response(models.ListResponse, response)

    async def metadata(
        self, *, query: models.MetadataQuery | None = None
    ) -> models.MetadataResponse:
        """GET /commitments/metadata. Scopes => order."""
        response = await self._request("GET", METADATA_PATH, query=query)
        return parse_response(models.MetadataResponse, response)

    async def export(self, *, body: models.ExportRequest | None = None) -> models.ExportResponse:
        """POST /commitments/export. Scopes => order."""
        response = await self._request("POST", EXPORT_PATH, body=body)
        return parse_response(models.ExportResponse, response)

    async def export_report(
        self, *, body: models.ExportReportRequest | None = None
    ) -> models.ExportReportResponse:
        """POST /commitments/report/export. Scopes => order."""
        response = await self._request("POST", EXPORT_REPORT_PATH, body=body)
        return parse_response(models.ExportReportResponse, response)

    async def get(
        self, variant_id: int, *, query: models.GetQuery | None = None
    ) -> models.GetResponse:
        """GET /commitments/{variant_id}. Scopes => order."""
        response = await self._request(
            "GET", GET_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.GetResponse, response)
