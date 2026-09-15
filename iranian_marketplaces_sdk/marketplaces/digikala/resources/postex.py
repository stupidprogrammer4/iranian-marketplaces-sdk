"""Digikala postex: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import postex as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
)

CREATE_USER_PATH = "/shipping-services/user"
CHARGE_WALLET_PATH = "/shipping-services/wallet/charge"
TRANSACTIONS_PATH = "/shipping-services/wallet/transactions"
CALCULATE_PRICE_PATH = "/shipping-services/parcels/calculate-price"


class PostexSync(SyncResource):
    def create_user(self, *, body: models.CreateUserRequest) -> RawResponse:
        """POST /shipping-services/user. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", CREATE_USER_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def charge_wallet(self, *, body: models.ChargeWalletRequest) -> RawResponse:
        """POST /shipping-services/wallet/charge. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", CHARGE_WALLET_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def transactions(
        self, *, query: models.TransactionsQuery | None = None
    ) -> models.TransactionsResponse:
        """GET /shipping-services/wallet/transactions. Scopes => sbs_shipment."""
        response = self._request("GET", TRANSACTIONS_PATH, query=query)
        return parse_response(models.TransactionsResponse, response)

    def calculate_price(self, *, body: models.CalculatePriceRequest) -> RawResponse:
        """POST /shipping-services/parcels/calculate-price. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", CALCULATE_PRICE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class PostexAsync(AsyncResource):
    async def create_user(self, *, body: models.CreateUserRequest) -> RawResponse:
        """POST /shipping-services/user. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", CREATE_USER_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def charge_wallet(self, *, body: models.ChargeWalletRequest) -> RawResponse:
        """POST /shipping-services/wallet/charge. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", CHARGE_WALLET_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def transactions(
        self, *, query: models.TransactionsQuery | None = None
    ) -> models.TransactionsResponse:
        """GET /shipping-services/wallet/transactions. Scopes => sbs_shipment."""
        response = await self._request("GET", TRANSACTIONS_PATH, query=query)
        return parse_response(models.TransactionsResponse, response)

    async def calculate_price(self, *, body: models.CalculatePriceRequest) -> RawResponse:
        """POST /shipping-services/parcels/calculate-price. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", CALCULATE_PRICE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
