"""Digikala vouchers: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import vouchers as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/pricing/vouchers"
CREATE_PATH = "/pricing/vouchers"
UPDATE_PATH = "/pricing/vouchers"
TYPES_PATH = "/pricing/vouchers/types"
GET_PATH = "/pricing/vouchers/{voucher_id}"
ELIGIBLE_VARIANTS_PATH = "/pricing/vouchers/variants/eligible"


class VouchersSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/vouchers. Scopes => voucher."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/vouchers. Scopes => voucher."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/vouchers. Scopes => voucher."""
        response = self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    def types(self, *, query: models.TypesQuery | None = None) -> models.TypesResponse:
        """GET /pricing/vouchers/types. Scopes => voucher."""
        response = self._request("GET", TYPES_PATH, query=query)
        return parse_response(models.TypesResponse, response)

    def get(self, voucher_id: int) -> models.GetResponse:
        """GET /pricing/vouchers/{voucher_id}. Scopes => voucher."""
        response = self._request("GET", GET_PATH.format(voucher_id=path_value(voucher_id)))
        return parse_response(models.GetResponse, response)

    def eligible_variants(
        self, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/vouchers/variants/eligible. Scopes => voucher."""
        response = self._request("GET", ELIGIBLE_VARIANTS_PATH, query=query)
        return parse_response(models.EligibleVariantsResponse, response)


class VouchersAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/vouchers. Scopes => voucher."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /pricing/vouchers. Scopes => voucher."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def update(self, *, body: models.UpdateRequest) -> models.UpdateResponse:
        """PUT /pricing/vouchers. Scopes => voucher."""
        response = await self._request("PUT", UPDATE_PATH, body=body)
        return parse_response(models.UpdateResponse, response)

    async def types(self, *, query: models.TypesQuery | None = None) -> models.TypesResponse:
        """GET /pricing/vouchers/types. Scopes => voucher."""
        response = await self._request("GET", TYPES_PATH, query=query)
        return parse_response(models.TypesResponse, response)

    async def get(self, voucher_id: int) -> models.GetResponse:
        """GET /pricing/vouchers/{voucher_id}. Scopes => voucher."""
        response = await self._request("GET", GET_PATH.format(voucher_id=path_value(voucher_id)))
        return parse_response(models.GetResponse, response)

    async def eligible_variants(
        self, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/vouchers/variants/eligible. Scopes => voucher."""
        response = await self._request("GET", ELIGIBLE_VARIANTS_PATH, query=query)
        return parse_response(models.EligibleVariantsResponse, response)
