"""Digikala shipping services: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import shipping_services as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

POSTEX_STATUS_PATH = "/shipping-services/postex-status"
WALLET_BALANCE_PATH = "/shipping-services/wallet/balance"
GET_USER_PATH = "/shipping-services/user"
TRANSACTION_PATH = "/shipping-services/wallet/transactions/{transaction_id}"
VERIFY_WALLET_PATH = "/shipping-services/wallet/verify"
BOXES_PATH = "/shipping-services/boxes"
TOKEN_STATUS_PATH = "/shipping-services/token-status"  # noqa: S105 - endpoint path, not a credential
BULK_TRACKING_CODES_PATH = "/shipping-services/parcels/post-tracking-code/bulk"
IMPORT_PARCELS_PATH = "/shipping-services/parcels/excel"
CALCULATE_COST_PATH = "/shipping-services/parcels/cost"
GET_ORDER_PATH = "/shipping-services/order/{shipment_id}"
ORDER_DETAIL_PATH = "/shipping-services/order/detail/{order_id}"
USER_INFO_PATH = "/shipping-services/user/info"
LABEL_PATH = "/shipping-services/label/{registration_method}/{parcel_number}"
REQUEST_LABEL_PATH = "/shipping-services/label-request"
LABEL_REQUEST_STATUS_PATH = "/shipping-services/label-request/{request_id}"


class ShippingServicesSync(SyncResource):
    def postex_status(self) -> RawResponse:
        """GET /shipping-services/postex-status. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", POSTEX_STATUS_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def wallet_balance(self) -> RawResponse:
        """GET /shipping-services/wallet/balance. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", WALLET_BALANCE_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def get_user(self) -> RawResponse:
        """GET /shipping-services/user. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", GET_USER_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def transaction(self, transaction_id: int) -> RawResponse:
        """GET /shipping-services/wallet/transactions/{transaction_id}. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET", TRANSACTION_PATH.format(transaction_id=path_value(transaction_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def verify_wallet(self, *, body: models.VerifyWalletRequest) -> RawResponse:
        """GET /shipping-services/wallet/verify. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", VERIFY_WALLET_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def boxes(self, *, query: models.BoxesQuery | None = None) -> models.BoxesResponse:
        """GET /shipping-services/boxes. Scopes => sbs_shipment."""
        response = self._request("GET", BOXES_PATH, query=query)
        return parse_response(models.BoxesResponse, response)

    def token_status(self) -> RawResponse:
        """GET /shipping-services/token-status. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", TOKEN_STATUS_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def bulk_tracking_codes(self, *, body: models.BulkTrackingCodesRequest) -> RawResponse:
        """POST /shipping-services/parcels/post-tracking-code/bulk. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", BULK_TRACKING_CODES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def import_parcels(self, *, body: models.ImportParcelsRequest) -> RawResponse:
        """POST /shipping-services/parcels/excel. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", IMPORT_PARCELS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def calculate_cost(self, *, body: models.CalculateCostRequest) -> RawResponse:
        """POST /shipping-services/parcels/cost. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", CALCULATE_COST_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def get_order(self, shipment_id: int) -> RawResponse:
        """GET /shipping-services/order/{shipment_id}. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request("GET", GET_ORDER_PATH.format(shipment_id=path_value(shipment_id)))
        return RawResponse(response.status_code, response.headers, response.content)

    def order_detail(
        self, order_id: int, *, query: models.OrderDetailQuery
    ) -> models.OrderDetailResponse:
        """GET /shipping-services/order/detail/{order_id}. Scopes => sbs_shipment."""
        response = self._request(
            "GET", ORDER_DETAIL_PATH.format(order_id=path_value(order_id)), query=query
        )
        return parse_response(models.OrderDetailResponse, response)

    def user_info(self) -> RawResponse:
        """GET /shipping-services/user/info. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("GET", USER_INFO_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    def label(self, registration_method: str, parcel_number: str) -> RawResponse:
        """GET /shipping-services/label/{registration_method}/{parcel_number}. Scopes =>
        sbs_shipment. Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET",
            LABEL_PATH.format(
                registration_method=path_value(registration_method),
                parcel_number=path_value(parcel_number),
            ),
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def request_label(self, *, body: models.RequestLabelRequest) -> RawResponse:
        """POST /shipping-services/label-request. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", REQUEST_LABEL_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def label_request_status(self, request_id: int) -> RawResponse:
        """GET /shipping-services/label-request/{request_id}. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET", LABEL_REQUEST_STATUS_PATH.format(request_id=path_value(request_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)


class ShippingServicesAsync(AsyncResource):
    async def postex_status(self) -> RawResponse:
        """GET /shipping-services/postex-status. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", POSTEX_STATUS_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def wallet_balance(self) -> RawResponse:
        """GET /shipping-services/wallet/balance. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", WALLET_BALANCE_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def get_user(self) -> RawResponse:
        """GET /shipping-services/user. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", GET_USER_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def transaction(self, transaction_id: int) -> RawResponse:
        """GET /shipping-services/wallet/transactions/{transaction_id}. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET", TRANSACTION_PATH.format(transaction_id=path_value(transaction_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def verify_wallet(self, *, body: models.VerifyWalletRequest) -> RawResponse:
        """GET /shipping-services/wallet/verify. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", VERIFY_WALLET_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def boxes(self, *, query: models.BoxesQuery | None = None) -> models.BoxesResponse:
        """GET /shipping-services/boxes. Scopes => sbs_shipment."""
        response = await self._request("GET", BOXES_PATH, query=query)
        return parse_response(models.BoxesResponse, response)

    async def token_status(self) -> RawResponse:
        """GET /shipping-services/token-status. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", TOKEN_STATUS_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def bulk_tracking_codes(self, *, body: models.BulkTrackingCodesRequest) -> RawResponse:
        """POST /shipping-services/parcels/post-tracking-code/bulk. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", BULK_TRACKING_CODES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def import_parcels(self, *, body: models.ImportParcelsRequest) -> RawResponse:
        """POST /shipping-services/parcels/excel. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", IMPORT_PARCELS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def calculate_cost(self, *, body: models.CalculateCostRequest) -> RawResponse:
        """POST /shipping-services/parcels/cost. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", CALCULATE_COST_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def get_order(self, shipment_id: int) -> RawResponse:
        """GET /shipping-services/order/{shipment_id}. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET", GET_ORDER_PATH.format(shipment_id=path_value(shipment_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def order_detail(
        self, order_id: int, *, query: models.OrderDetailQuery
    ) -> models.OrderDetailResponse:
        """GET /shipping-services/order/detail/{order_id}. Scopes => sbs_shipment."""
        response = await self._request(
            "GET", ORDER_DETAIL_PATH.format(order_id=path_value(order_id)), query=query
        )
        return parse_response(models.OrderDetailResponse, response)

    async def user_info(self) -> RawResponse:
        """GET /shipping-services/user/info. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("GET", USER_INFO_PATH)
        return RawResponse(response.status_code, response.headers, response.content)

    async def label(self, registration_method: str, parcel_number: str) -> RawResponse:
        """GET /shipping-services/label/{registration_method}/{parcel_number}. Scopes =>
        sbs_shipment. Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET",
            LABEL_PATH.format(
                registration_method=path_value(registration_method),
                parcel_number=path_value(parcel_number),
            ),
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def request_label(self, *, body: models.RequestLabelRequest) -> RawResponse:
        """POST /shipping-services/label-request. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", REQUEST_LABEL_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def label_request_status(self, request_id: int) -> RawResponse:
        """GET /shipping-services/label-request/{request_id}. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET", LABEL_REQUEST_STATUS_PATH.format(request_id=path_value(request_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)
