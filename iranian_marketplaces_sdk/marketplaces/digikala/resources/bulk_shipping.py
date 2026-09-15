"""Digikala bulk shipping: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import bulk_shipping as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

CANCEL_ORDER_PATH = "/shipping-services/order/cancel/{shipment_id}"
PACKAGE_PATH = "/bulk-shipping-services/packaging"
BULK_PACKAGE_PATH = "/bulk-shipping-services/bulk-packaging"
SIMPLE_PACKAGE_PATH = "/bulk-shipping-services/simple-packaging"
PICKUP_PATH = "/bulk-shipping-services/pickup"
DETAIL_PATH = "/bulk-shipping-services/detail/{shipment_ids}"
PROMISE_DATE_PATH = "/bulk-shipping-services/promise-date/{shipment_ids}"


class BulkShippingSync(SyncResource):
    def cancel_order(
        self, shipment_id: int, *, body: models.CancelOrderRequest | None = None
    ) -> RawResponse:
        """PUT /shipping-services/order/cancel/{shipment_id}. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "PUT", CANCEL_ORDER_PATH.format(shipment_id=path_value(shipment_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def package(self, *, body: models.PackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/packaging. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def bulk_package(self, *, body: models.BulkPackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/bulk-packaging. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = self._request("POST", BULK_PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def simple_package(self, *, body: models.SimplePackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/simple-packaging. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", SIMPLE_PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def pickup(self, *, body: models.PickupRequest) -> RawResponse:
        """POST /bulk-shipping-services/pickup. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", PICKUP_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def detail(
        self, shipment_ids: list[int], *, query: models.DetailQuery
    ) -> models.DetailResponse:
        """GET /bulk-shipping-services/detail/{shipment_ids}. Scopes => sbs_shipment."""
        response = self._request(
            "GET",
            DETAIL_PATH.format(shipment_ids=path_value(shipment_ids)),
            query=query,
            separators={"shipment_ids": ","},
        )
        return parse_response(models.DetailResponse, response)

    def promise_date(
        self, shipment_ids: list[int], *, query: models.PromiseDateQuery
    ) -> RawResponse:
        """GET /bulk-shipping-services/promise-date/{shipment_ids}. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET",
            PROMISE_DATE_PATH.format(shipment_ids=path_value(shipment_ids)),
            query=query,
            separators={"shipment_ids": ","},
        )
        return RawResponse(response.status_code, response.headers, response.content)


class BulkShippingAsync(AsyncResource):
    async def cancel_order(
        self, shipment_id: int, *, body: models.CancelOrderRequest | None = None
    ) -> RawResponse:
        """PUT /shipping-services/order/cancel/{shipment_id}. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "PUT", CANCEL_ORDER_PATH.format(shipment_id=path_value(shipment_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def package(self, *, body: models.PackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/packaging. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def bulk_package(self, *, body: models.BulkPackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/bulk-packaging. Scopes => sbs_shipment. Response schema
        is undocumented; returns original bytes and headers."""
        response = await self._request("POST", BULK_PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def simple_package(self, *, body: models.SimplePackageRequest) -> RawResponse:
        """POST /bulk-shipping-services/simple-packaging. Scopes => sbs_shipment. Response
        schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", SIMPLE_PACKAGE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def pickup(self, *, body: models.PickupRequest) -> RawResponse:
        """POST /bulk-shipping-services/pickup. Scopes => sbs_shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", PICKUP_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def detail(
        self, shipment_ids: list[int], *, query: models.DetailQuery
    ) -> models.DetailResponse:
        """GET /bulk-shipping-services/detail/{shipment_ids}. Scopes => sbs_shipment."""
        response = await self._request(
            "GET",
            DETAIL_PATH.format(shipment_ids=path_value(shipment_ids)),
            query=query,
            separators={"shipment_ids": ","},
        )
        return parse_response(models.DetailResponse, response)

    async def promise_date(
        self, shipment_ids: list[int], *, query: models.PromiseDateQuery
    ) -> RawResponse:
        """GET /bulk-shipping-services/promise-date/{shipment_ids}. Scopes => sbs_shipment.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET",
            PROMISE_DATE_PATH.format(shipment_ids=path_value(shipment_ids)),
            query=query,
            separators={"shipment_ids": ","},
        )
        return RawResponse(response.status_code, response.headers, response.content)
