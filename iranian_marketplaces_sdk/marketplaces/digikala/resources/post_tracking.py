"""Digikala post tracking: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import post_tracking as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
)

SAMPLE_EXCEL_PATH = "/shipping-services/excel/post-tracking-sample"
IMPORT_TRACKING_CODES_PATH = "/shipping-services/import/tracking-code"


class PostTrackingSync(SyncResource):
    def sample_excel(self) -> RawResponse:
        """GET /shipping-services/excel/post-tracking-sample. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("GET", SAMPLE_EXCEL_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def import_tracking_codes(self, *, body: models.ImportTrackingCodesRequest) -> RawResponse:
        """POST /shipping-services/import/tracking-code. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", IMPORT_TRACKING_CODES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class PostTrackingAsync(AsyncResource):
    async def sample_excel(self) -> RawResponse:
        """GET /shipping-services/excel/post-tracking-sample. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("GET", SAMPLE_EXCEL_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def import_tracking_codes(
        self, *, body: models.ImportTrackingCodesRequest
    ) -> RawResponse:
        """POST /shipping-services/import/tracking-code. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", IMPORT_TRACKING_CODES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
