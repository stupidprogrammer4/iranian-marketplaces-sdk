"""Digikala smart discount: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import smart_discount as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

ELIGIBLE_PATH = "/pricing/smart-discount/variants/eligible"
LIST_PATH = "/pricing/smart-discount/variants/{active_status}"
CREATE_BATCH_PATH = "/pricing/smart-discount/variants/batch"
UPDATE_BATCH_PATH = "/pricing/smart-discount/variants/batch"
CREATE_PATH = "/pricing/smart-discount/variants"
UPDATE_PATH = "/pricing/smart-discount/variants"
DELETE_PATH = "/pricing/smart-discount/variants"
DELETE_ALL_PATH = "/pricing/smart-discount/variants/all"
EXPORT_ELIGIBLE_PATH = "/pricing/smart-discount/variants/eligible/excel"
SAMPLE_EXCEL_PATH = "/pricing/smart-discount/variants/excel/sample"
EXPORT_PATH = "/pricing/smart-discount/variants/excel/async-export"
IMPORT_EXCEL_PATH = "/pricing/smart-discount/variants/excel"
DELETE_ALL_ASYNC_PATH = "/pricing/smart-discount/variants/excel/delete-all-async"
AUTO_JOINED_PATH = "/pricing/smart-discount/auto-joined/{campaign_name}"
EXPORT_PROMOTION_ELIGIBLE_PATH = "/pricing/promotions/{promotion_id}/variants/eligible/excel"


class SmartDiscountSync(SyncResource):
    def eligible(self, *, query: models.EligibleQuery | None = None) -> models.EligibleResponse:
        """GET /pricing/smart-discount/variants/eligible. Scopes => promotion."""
        response = self._request("GET", ELIGIBLE_PATH, query=query)
        return parse_response(models.EligibleResponse, response)

    def list(
        self, active_status: str, *, query: models.ListQuery | None = None
    ) -> models.ListResponse:
        """GET /pricing/smart-discount/variants/{active_status}. Scopes => promotion."""
        response = self._request(
            "GET",
            LIST_PATH.format(active_status=path_value(active_status)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.ListResponse, response)

    def create_batch(self, *, body: models.CreateBatchRequest) -> models.CreateBatchResponse:
        """POST /pricing/smart-discount/variants/batch. Scopes => promotion."""
        response = self._request("POST", CREATE_BATCH_PATH, body=body)
        return parse_response(models.CreateBatchResponse, response)

    def update_batch(self, *, body: models.UpdateBatchRequest) -> models.UpdateBatchResponse:
        """PUT /pricing/smart-discount/variants/batch. Scopes => promotion."""
        response = self._request("PUT", UPDATE_BATCH_PATH, body=body)
        return parse_response(models.UpdateBatchResponse, response)

    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/smart-discount/variants. Scopes => promotion."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/smart-discount/variants. Scopes => promotion."""
        response = self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    def delete(self, *, body: models.DeleteRequest) -> models.DeleteResponse:
        """DELETE /pricing/smart-discount/variants. Scopes => promotion."""
        response = self._request("DELETE", DELETE_PATH, body=body)
        return parse_response(models.DeleteResponse, response)

    def delete_all(self, *, body: models.DeleteAllRequest) -> models.DeleteAllResponse:
        """DELETE /pricing/smart-discount/variants/all. Scopes => promotion."""
        response = self._request("DELETE", DELETE_ALL_PATH, body=body)
        return parse_response(models.DeleteAllResponse, response)

    def export_eligible(self) -> RawResponse:
        """GET /pricing/smart-discount/variants/eligible/excel. Scopes => promotion. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("GET", EXPORT_ELIGIBLE_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def sample_excel(self) -> RawResponse:
        """GET /pricing/smart-discount/variants/excel/sample. Scopes => promotion. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("GET", SAMPLE_EXCEL_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def export(self) -> models.ExportResponse:
        """GET /pricing/smart-discount/variants/excel/async-export. Scopes => promotion."""
        response = self._request("GET", EXPORT_PATH)
        return parse_response(models.ExportResponse, response)

    def import_excel(
        self, *, body: models.ImportExcelRequest | None = None
    ) -> models.ImportExcelResponse:
        """POST /pricing/smart-discount/variants/excel. Scopes => promotion."""
        response = self._request("POST", IMPORT_EXCEL_PATH, body=body)
        return parse_response(models.ImportExcelResponse, response)

    def delete_all_async(
        self, *, body: models.DeleteAllAsyncRequest
    ) -> models.DeleteAllAsyncResponse:
        """POST /pricing/smart-discount/variants/excel/delete-all-async. Scopes => promotion."""
        response = self._request("POST", DELETE_ALL_ASYNC_PATH, body=body)
        return parse_response(models.DeleteAllAsyncResponse, response)

    def auto_joined(
        self, campaign_name: str, *, query: models.AutoJoinedQuery
    ) -> models.AutoJoinedResponse:
        """GET /pricing/smart-discount/auto-joined/{campaign_name}. Scopes => promotion."""
        response = self._request(
            "GET", AUTO_JOINED_PATH.format(campaign_name=path_value(campaign_name)), query=query
        )
        return parse_response(models.AutoJoinedResponse, response)

    def export_promotion_eligible(self, promotion_id: int) -> RawResponse:
        """GET /pricing/promotions/{promotion_id}/variants/eligible/excel. Scopes => promotion.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET", EXPORT_PROMOTION_ELIGIBLE_PATH.format(promotion_id=path_value(promotion_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)


class SmartDiscountAsync(AsyncResource):
    async def eligible(
        self, *, query: models.EligibleQuery | None = None
    ) -> models.EligibleResponse:
        """GET /pricing/smart-discount/variants/eligible. Scopes => promotion."""
        response = await self._request("GET", ELIGIBLE_PATH, query=query)
        return parse_response(models.EligibleResponse, response)

    async def list(
        self, active_status: str, *, query: models.ListQuery | None = None
    ) -> models.ListResponse:
        """GET /pricing/smart-discount/variants/{active_status}. Scopes => promotion."""
        response = await self._request(
            "GET",
            LIST_PATH.format(active_status=path_value(active_status)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.ListResponse, response)

    async def create_batch(self, *, body: models.CreateBatchRequest) -> models.CreateBatchResponse:
        """POST /pricing/smart-discount/variants/batch. Scopes => promotion."""
        response = await self._request("POST", CREATE_BATCH_PATH, body=body)
        return parse_response(models.CreateBatchResponse, response)

    async def update_batch(self, *, body: models.UpdateBatchRequest) -> models.UpdateBatchResponse:
        """PUT /pricing/smart-discount/variants/batch. Scopes => promotion."""
        response = await self._request("PUT", UPDATE_BATCH_PATH, body=body)
        return parse_response(models.UpdateBatchResponse, response)

    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/smart-discount/variants. Scopes => promotion."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/smart-discount/variants. Scopes => promotion."""
        response = await self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    async def delete(self, *, body: models.DeleteRequest) -> models.DeleteResponse:
        """DELETE /pricing/smart-discount/variants. Scopes => promotion."""
        response = await self._request("DELETE", DELETE_PATH, body=body)
        return parse_response(models.DeleteResponse, response)

    async def delete_all(self, *, body: models.DeleteAllRequest) -> models.DeleteAllResponse:
        """DELETE /pricing/smart-discount/variants/all. Scopes => promotion."""
        response = await self._request("DELETE", DELETE_ALL_PATH, body=body)
        return parse_response(models.DeleteAllResponse, response)

    async def export_eligible(self) -> RawResponse:
        """GET /pricing/smart-discount/variants/eligible/excel. Scopes => promotion. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("GET", EXPORT_ELIGIBLE_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def sample_excel(self) -> RawResponse:
        """GET /pricing/smart-discount/variants/excel/sample. Scopes => promotion. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("GET", SAMPLE_EXCEL_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def export(self) -> models.ExportResponse:
        """GET /pricing/smart-discount/variants/excel/async-export. Scopes => promotion."""
        response = await self._request("GET", EXPORT_PATH)
        return parse_response(models.ExportResponse, response)

    async def import_excel(
        self, *, body: models.ImportExcelRequest | None = None
    ) -> models.ImportExcelResponse:
        """POST /pricing/smart-discount/variants/excel. Scopes => promotion."""
        response = await self._request("POST", IMPORT_EXCEL_PATH, body=body)
        return parse_response(models.ImportExcelResponse, response)

    async def delete_all_async(
        self, *, body: models.DeleteAllAsyncRequest
    ) -> models.DeleteAllAsyncResponse:
        """POST /pricing/smart-discount/variants/excel/delete-all-async. Scopes => promotion."""
        response = await self._request("POST", DELETE_ALL_ASYNC_PATH, body=body)
        return parse_response(models.DeleteAllAsyncResponse, response)

    async def auto_joined(
        self, campaign_name: str, *, query: models.AutoJoinedQuery
    ) -> models.AutoJoinedResponse:
        """GET /pricing/smart-discount/auto-joined/{campaign_name}. Scopes => promotion."""
        response = await self._request(
            "GET", AUTO_JOINED_PATH.format(campaign_name=path_value(campaign_name)), query=query
        )
        return parse_response(models.AutoJoinedResponse, response)

    async def export_promotion_eligible(self, promotion_id: int) -> RawResponse:
        """GET /pricing/promotions/{promotion_id}/variants/eligible/excel. Scopes => promotion.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET", EXPORT_PROMOTION_ELIGIBLE_PATH.format(promotion_id=path_value(promotion_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)
