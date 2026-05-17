"""TypedDicts for the Tapsi vendor-orders endpoint.

``POST /Web/Hub/vendors/v1/orders`` takes a JSON filter body and returns a
page-based list. JSON keys mirror the API exactly.

Code references (per the API docs):

* ``orderStatusId`` items: 4 = order confirmed, 6 = order canceled,
  9 = fully delivered.
* ``shippingStatusType`` items (shipment state codes): 100 pre-order,
  110 awaiting courier assignment, 120 awaiting preparation,
  140 awaiting delivery-method change, 200 awaiting collection,
  210 courier at store, 300 ready to ship, 310 shipped,
  320 delivered to customer, 400 delivery failed, 410 canceled,
  420 expired, 900 awaiting re-inquiry.
* ``deliveryMethod``: "1" = seller ships, "2" = platform ships,
  "3" = in-person pickup (documented as a string).

``productId`` / ``categoryIds`` element types are not published; the API's
identifiers are strings elsewhere, so they are typed ``list[str]``.

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import TypedDict

from .common import ApiMessage

__all__ = [
    "OrdersQuery",
    "Order",
    "OrdersPage",
    "OrdersResponse",
]


class OrdersQuery(TypedDict, total=False):
    """Optional JSON filter body for the orders endpoint.

    ``pageNumber`` is zero-based. ``pageSize`` defaults to 20 server-side.
    ``fromDate`` / ``toDate`` are ``DATETIMEOFFSET`` strings.
    """

    pageNumber: int
    pageSize: int
    fromDate: str
    toDate: str
    orderNumber: str
    bundleId: str
    orderStatusId: list[int]
    shippingStatusType: list[int]
    deliveryMethod: str
    productId: list[str]
    categoryIds: list[str]


class Order(TypedDict):
    """A single order in the paginated orders response.

    ``createdOn`` is an ISO-8601 UTC timestamp; ``persianDateTime`` is the
    same instant rendered in the Persian calendar.
    """

    id: str
    orderNumber: str
    shipmentOrderBundleNumbers: list[str]
    persianDateTime: str
    stateCode: str
    stateTitle: str
    finalPrice: int
    serviceFee: int
    voucherTotalFee: int
    createdOn: str


class OrdersPage(TypedDict):
    """Inner ``data`` envelope of the paginated orders response."""

    pageNumber: int
    pageSize: int
    totalItems: int
    items: list[Order]


class OrdersResponse(TypedDict):
    """Full response body of ``POST /Web/Hub/vendors/v1/orders``."""

    success: bool
    messages: list[ApiMessage]
    data: OrdersPage
