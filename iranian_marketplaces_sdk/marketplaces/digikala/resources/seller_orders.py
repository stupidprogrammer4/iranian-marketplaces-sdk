"""Digikala seller orders: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import seller_orders as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/ship-by-seller-orders"
STATISTICS_PATH = "/ship-by-seller-orders/statistics"
GET_PATH = "/ship-by-seller-orders/{shipment_id}"
CUSTOMER_PATH = "/ship-by-seller-orders/customer/{shipment_id}"
POST_DATA_PATH = "/ship-by-seller-orders/post-data/{shipment_id}"
TIME_SCOPES_PATH = "/ship-by-seller-orders/time-scopes/{shipment_id}"
FAILED_DELIVERY_TIME_SCOPES_PATH = (
    "/ship-by-seller-orders/failed-delivery/time-scopes/{shipment_id}"
)
CANCEL_ITEM_PATH = "/ship-by-seller-orders/cancel-item"
CANCEL_SHIPMENT_PATH = "/ship-by-seller-orders/cancel-shipment"
UPDATE_TRACKING_CODE_PATH = "/ship-by-seller-orders/tracking-code"
UPDATE_STATUS_PATH = "/ship-by-seller-orders/update-status"
MARK_DELIVERED_PATH = "/ship-by-seller-orders/full-delivered"
UPDATE_EDITED_PATH = "/ship-by-seller-orders/update-edited"
REPORT_FAILED_DELIVERY_PATH = "/ship-by-seller-orders/failed-delivery"
CHANGE_TIME_SCOPE_PATH = "/ship-by-seller-orders/change-time-scope"
POST_ORDER_PATH = "/ship-by-seller-orders/post-order/{shipment_id}"
BATCH_UPDATE_STATUS_PATH = "/ship-by-seller-orders/batch-update-status"


class SellerOrdersSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /ship-by-seller-orders. Scopes => sbs_orders."""
        response = self._request(
            "GET", LIST_PATH, query=query, separators={"search[category_ids]": ","}
        )
        return parse_response(models.ListResponse, response)

    def statistics(self) -> models.StatisticsResponse:
        """GET /ship-by-seller-orders/statistics. Scopes => sbs_orders."""
        response = self._request("GET", STATISTICS_PATH)
        return parse_response(models.StatisticsResponse, response)

    def get(self, shipment_id: int) -> models.GetResponse:
        """GET /ship-by-seller-orders/{shipment_id}. Scopes => sbs_orders."""
        response = self._request("GET", GET_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.GetResponse, response)

    def customer(self, shipment_id: int) -> models.CustomerResponse:
        """GET /ship-by-seller-orders/customer/{shipment_id}. Scopes => sbs_orders."""
        response = self._request("GET", CUSTOMER_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.CustomerResponse, response)

    def post_data(self, shipment_id: int) -> models.PostDataResponse:
        """GET /ship-by-seller-orders/post-data/{shipment_id}. Scopes => sbs_orders."""
        response = self._request("GET", POST_DATA_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.PostDataResponse, response)

    def time_scopes(self, shipment_id: int) -> models.TimeScopesResponse:
        """GET /ship-by-seller-orders/time-scopes/{shipment_id}. Scopes => sbs_orders."""
        response = self._request(
            "GET", TIME_SCOPES_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.TimeScopesResponse, response)

    def failed_delivery_time_scopes(
        self, shipment_id: int
    ) -> models.FailedDeliveryTimeScopesResponse:
        """GET /ship-by-seller-orders/failed-delivery/time-scopes/{shipment_id}. Scopes =>
        sbs_orders."""
        response = self._request(
            "GET", FAILED_DELIVERY_TIME_SCOPES_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.FailedDeliveryTimeScopesResponse, response)

    def cancel_item(self, *, body: models.CancelItemRequest) -> RawResponse:
        """POST /ship-by-seller-orders/cancel-item. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", CANCEL_ITEM_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def cancel_shipment(self, *, body: models.CancelShipmentRequest) -> RawResponse:
        """POST /ship-by-seller-orders/cancel-shipment. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request("POST", CANCEL_SHIPMENT_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def update_tracking_code(self, *, body: models.UpdateTrackingCodeRequest) -> RawResponse:
        """POST /ship-by-seller-orders/tracking-code. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", UPDATE_TRACKING_CODE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def update_status(self, *, body: models.UpdateStatusRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/update-status. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("PUT", UPDATE_STATUS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def mark_delivered(self, *, body: models.MarkDeliveredRequest) -> RawResponse:
        """POST /ship-by-seller-orders/full-delivered. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", MARK_DELIVERED_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def update_edited(self, *, body: models.UpdateEditedRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/update-edited. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("PUT", UPDATE_EDITED_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def report_failed_delivery(self, *, body: models.ReportFailedDeliveryRequest) -> RawResponse:
        """POST /ship-by-seller-orders/failed-delivery. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request("POST", REPORT_FAILED_DELIVERY_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def change_time_scope(self, *, body: models.ChangeTimeScopeRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/change-time-scope. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request("PUT", CHANGE_TIME_SCOPE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def post_order(self, shipment_id: int) -> models.PostOrderResponse:
        """GET /ship-by-seller-orders/post-order/{shipment_id}. Scopes => sbs_orders."""
        response = self._request("GET", POST_ORDER_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.PostOrderResponse, response)

    def batch_update_status(self, *, body: models.BatchUpdateStatusRequest) -> RawResponse:
        """POST /ship-by-seller-orders/batch-update-status. Scopes => sbs_orders. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", BATCH_UPDATE_STATUS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class SellerOrdersAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /ship-by-seller-orders. Scopes => sbs_orders."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[category_ids]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def statistics(self) -> models.StatisticsResponse:
        """GET /ship-by-seller-orders/statistics. Scopes => sbs_orders."""
        response = await self._request("GET", STATISTICS_PATH)
        return parse_response(models.StatisticsResponse, response)

    async def get(self, shipment_id: int) -> models.GetResponse:
        """GET /ship-by-seller-orders/{shipment_id}. Scopes => sbs_orders."""
        response = await self._request("GET", GET_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.GetResponse, response)

    async def customer(self, shipment_id: int) -> models.CustomerResponse:
        """GET /ship-by-seller-orders/customer/{shipment_id}. Scopes => sbs_orders."""
        response = await self._request(
            "GET", CUSTOMER_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.CustomerResponse, response)

    async def post_data(self, shipment_id: int) -> models.PostDataResponse:
        """GET /ship-by-seller-orders/post-data/{shipment_id}. Scopes => sbs_orders."""
        response = await self._request(
            "GET", POST_DATA_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.PostDataResponse, response)

    async def time_scopes(self, shipment_id: int) -> models.TimeScopesResponse:
        """GET /ship-by-seller-orders/time-scopes/{shipment_id}. Scopes => sbs_orders."""
        response = await self._request(
            "GET", TIME_SCOPES_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.TimeScopesResponse, response)

    async def failed_delivery_time_scopes(
        self, shipment_id: int
    ) -> models.FailedDeliveryTimeScopesResponse:
        """GET /ship-by-seller-orders/failed-delivery/time-scopes/{shipment_id}. Scopes =>
        sbs_orders."""
        response = await self._request(
            "GET", FAILED_DELIVERY_TIME_SCOPES_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.FailedDeliveryTimeScopesResponse, response)

    async def cancel_item(self, *, body: models.CancelItemRequest) -> RawResponse:
        """POST /ship-by-seller-orders/cancel-item. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", CANCEL_ITEM_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def cancel_shipment(self, *, body: models.CancelShipmentRequest) -> RawResponse:
        """POST /ship-by-seller-orders/cancel-shipment. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request("POST", CANCEL_SHIPMENT_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def update_tracking_code(self, *, body: models.UpdateTrackingCodeRequest) -> RawResponse:
        """POST /ship-by-seller-orders/tracking-code. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", UPDATE_TRACKING_CODE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def update_status(self, *, body: models.UpdateStatusRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/update-status. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("PUT", UPDATE_STATUS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def mark_delivered(self, *, body: models.MarkDeliveredRequest) -> RawResponse:
        """POST /ship-by-seller-orders/full-delivered. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", MARK_DELIVERED_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def update_edited(self, *, body: models.UpdateEditedRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/update-edited. Scopes => sbs_orders. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("PUT", UPDATE_EDITED_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def report_failed_delivery(
        self, *, body: models.ReportFailedDeliveryRequest
    ) -> RawResponse:
        """POST /ship-by-seller-orders/failed-delivery. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request("POST", REPORT_FAILED_DELIVERY_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def change_time_scope(self, *, body: models.ChangeTimeScopeRequest) -> RawResponse:
        """PUT /ship-by-seller-orders/change-time-scope. Scopes => sbs_orders. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request("PUT", CHANGE_TIME_SCOPE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def post_order(self, shipment_id: int) -> models.PostOrderResponse:
        """GET /ship-by-seller-orders/post-order/{shipment_id}. Scopes => sbs_orders."""
        response = await self._request(
            "GET", POST_ORDER_PATH.format(shipment_id=path_value(shipment_id))
        )
        return parse_response(models.PostOrderResponse, response)

    async def batch_update_status(self, *, body: models.BatchUpdateStatusRequest) -> RawResponse:
        """POST /ship-by-seller-orders/batch-update-status. Scopes => sbs_orders. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", BATCH_UPDATE_STATUS_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
