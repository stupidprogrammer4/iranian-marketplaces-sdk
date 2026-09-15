"""Digikala drop shipping: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import drop_shipping as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
)

SEND_OTP_PATH = "/shipping-services/send_otp"
TOTAL_WEIGHT_PATH = "/shipping-services/parcels/total-weight"
REGISTER_USER_PATH = "/shipping-services/user/register"


class DropShippingSync(SyncResource):
    def send_otp(self, *, body: models.SendOtpRequest) -> RawResponse:
        """POST /shipping-services/send_otp. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", SEND_OTP_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def total_weight(self, *, query: models.TotalWeightQuery) -> RawResponse:
        """GET /shipping-services/parcels/total-weight. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET",
            TOTAL_WEIGHT_PATH,
            query=query,
            separators={"variant_ids": ",", "quantities": ","},
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def register_user(self, *, body: models.RegisterUserRequest) -> RawResponse:
        """POST /shipping-services/user/register. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", REGISTER_USER_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class DropShippingAsync(AsyncResource):
    async def send_otp(self, *, body: models.SendOtpRequest) -> RawResponse:
        """POST /shipping-services/send_otp. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", SEND_OTP_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def total_weight(self, *, query: models.TotalWeightQuery) -> RawResponse:
        """GET /shipping-services/parcels/total-weight. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET",
            TOTAL_WEIGHT_PATH,
            query=query,
            separators={"variant_ids": ",", "quantities": ","},
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def register_user(self, *, body: models.RegisterUserRequest) -> RawResponse:
        """POST /shipping-services/user/register. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", REGISTER_USER_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
