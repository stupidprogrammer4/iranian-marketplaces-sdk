"""Digikala plp: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import plp as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/pricing/plp"
DELETE_PATH = "/pricing/plp"
CREATE_PATH = "/pricing/plp"
UPDATE_PATH = "/pricing/plp"
GET_PATH = "/pricing/plp/{promotion_id}"
DELETE_VARIANTS_PATH = "/pricing/plp/variants"
ELIGIBLE_VARIANTS_PATH = "/pricing/plp/variants/eligible"
SAMPLE_EXCEL_PATH = "/pricing/plp/excel/import/sample"
EXPORT_PATH = "/pricing/plp/excel/{promotion_id}"
IMPORT_EXCEL_PATH = "/pricing/plp/excel"


class PlpSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/plp. Scopes => promotion."""
        response = self._request(
            "GET", LIST_PATH, query=query, separators={"search[statuses]": ","}
        )
        return parse_response(models.ListResponse, response)

    def delete(self, *, body: models.DeleteRequest) -> models.DeleteResponse:
        """DELETE /pricing/plp. Scopes => promotion."""
        response = self._request("DELETE", DELETE_PATH, body=body)
        return parse_response(models.DeleteResponse, response)

    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/plp. Scopes => promotion."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/plp. Scopes => promotion."""
        response = self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    def get(self, promotion_id: int, *, query: models.GetQuery | None = None) -> models.GetResponse:
        """GET /pricing/plp/{promotion_id}. Scopes => promotion."""
        response = self._request(
            "GET", GET_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.GetResponse, response)

    def delete_variants(
        self, *, body: models.DeleteVariantsRequest
    ) -> models.DeleteVariantsResponse:
        """DELETE /pricing/plp/variants. Scopes => promotion."""
        response = self._request("DELETE", DELETE_VARIANTS_PATH, body=body)
        return parse_response(models.DeleteVariantsResponse, response)

    def eligible_variants(
        self, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/plp/variants/eligible. Scopes => promotion."""
        response = self._request("GET", ELIGIBLE_VARIANTS_PATH, query=query)
        return parse_response(models.EligibleVariantsResponse, response)

    def sample_excel(self) -> models.SampleExcelResponse:
        """GET /pricing/plp/excel/import/sample. Scopes => promotion."""
        response = self._request("GET", SAMPLE_EXCEL_PATH)
        return parse_response(models.SampleExcelResponse, response)

    def export(self, promotion_id: int) -> models.ExportResponse:
        """GET /pricing/plp/excel/{promotion_id}. Scopes => promotion."""
        response = self._request("GET", EXPORT_PATH.format(promotion_id=path_value(promotion_id)))
        return parse_response(models.ExportResponse, response)

    def import_excel(self, *, body: models.ImportExcelRequest) -> models.ImportExcelResponse:
        """POST /pricing/plp/excel. Scopes => promotion."""
        response = self._request("POST", IMPORT_EXCEL_PATH, body=body)
        return parse_response(models.ImportExcelResponse, response)


class PlpAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/plp. Scopes => promotion."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[statuses]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def delete(self, *, body: models.DeleteRequest) -> models.DeleteResponse:
        """DELETE /pricing/plp. Scopes => promotion."""
        response = await self._request("DELETE", DELETE_PATH, body=body)
        return parse_response(models.DeleteResponse, response)

    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/plp. Scopes => promotion."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/plp. Scopes => promotion."""
        response = await self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    async def get(
        self, promotion_id: int, *, query: models.GetQuery | None = None
    ) -> models.GetResponse:
        """GET /pricing/plp/{promotion_id}. Scopes => promotion."""
        response = await self._request(
            "GET", GET_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.GetResponse, response)

    async def delete_variants(
        self, *, body: models.DeleteVariantsRequest
    ) -> models.DeleteVariantsResponse:
        """DELETE /pricing/plp/variants. Scopes => promotion."""
        response = await self._request("DELETE", DELETE_VARIANTS_PATH, body=body)
        return parse_response(models.DeleteVariantsResponse, response)

    async def eligible_variants(
        self, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/plp/variants/eligible. Scopes => promotion."""
        response = await self._request("GET", ELIGIBLE_VARIANTS_PATH, query=query)
        return parse_response(models.EligibleVariantsResponse, response)

    async def sample_excel(self) -> models.SampleExcelResponse:
        """GET /pricing/plp/excel/import/sample. Scopes => promotion."""
        response = await self._request("GET", SAMPLE_EXCEL_PATH)
        return parse_response(models.SampleExcelResponse, response)

    async def export(self, promotion_id: int) -> models.ExportResponse:
        """GET /pricing/plp/excel/{promotion_id}. Scopes => promotion."""
        response = await self._request(
            "GET", EXPORT_PATH.format(promotion_id=path_value(promotion_id))
        )
        return parse_response(models.ExportResponse, response)

    async def import_excel(self, *, body: models.ImportExcelRequest) -> models.ImportExcelResponse:
        """POST /pricing/plp/excel. Scopes => promotion."""
        response = await self._request("POST", IMPORT_EXCEL_PATH, body=body)
        return parse_response(models.ImportExcelResponse, response)
