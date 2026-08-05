"""Tapsi Shop — the vendor-orders endpoint.

``POST /Web/Hub/vendors/v1/orders`` takes its filters as a JSON body and answers with a page-based
list. As everywhere in this API, the wire names are camelCase and carry aliases here.

Code tables, per Tapsi's documentation:

* ``order_status_id``: 4 order confirmed, 6 order canceled, 9 fully delivered.
* ``shipping_status_type`` (shipment state): 100 pre-order, 110 awaiting courier assignment,
  120 awaiting preparation, 140 awaiting delivery-method change, 200 awaiting collection,
  210 courier at store, 300 ready to ship, 310 shipped, 320 delivered to customer,
  400 delivery failed, 410 canceled, 420 expired, 900 awaiting re-inquiry.
* ``delivery_method``: ``"1"`` seller ships, ``"2"`` platform ships, ``"3"`` in-person pickup —
  documented as a string, not an integer.
"""

from iranian_marketplaces_sdk.common.data import (
    CamelCaseRequestSchema,
    CamelCaseResponseSchema,
)
from iranian_marketplaces_sdk.marketplaces.tapsi.data.common import ApiMessage

__all__ = [
    "Order",
    "OrdersPage",
    "OrdersQuery",
    "OrdersResponse",
]


class OrdersQuery(CamelCaseRequestSchema):
    """The JSON filter body for the orders endpoint.

    ``page_number`` is **zero-based** here, unlike the products list, whose page is 1-based.
    ``page_size`` defaults to 20 server-side. ``from_date``/``to_date`` are ``DATETIMEOFFSET``
    strings.

    ``product_id`` and ``category_ids`` have no published element type; every other identifier in
    this API is a string, so they are typed as lists of strings.
    """

    page_number: int | None = None
    page_size: int | None = None
    from_date: str | None = None
    to_date: str | None = None
    order_number: str | None = None
    bundle_id: str | None = None
    order_status_id: list[int] | None = None
    shipping_status_type: list[int] | None = None
    delivery_method: str | None = None
    product_id: list[str] | None = None
    category_ids: list[str] | None = None


class Order(CamelCaseResponseSchema):
    """A single order in the paginated orders response.

    ``created_on`` is an ISO-8601 UTC timestamp; ``persian_date_time`` is the same instant in the
    Persian calendar. ``final_price`` is what the customer paid, before ``service_fee`` is taken.
    """

    id: str
    order_number: str
    shipment_order_bundle_numbers: list[str]
    persian_date_time: str
    state_code: str
    state_title: str
    final_price: int
    service_fee: int
    voucher_total_fee: int
    created_on: str


class OrdersPage(CamelCaseResponseSchema):
    """Inner ``data`` envelope of the paginated orders response."""

    page_number: int
    page_size: int
    total_items: int
    items: list[Order]


class OrdersResponse(CamelCaseResponseSchema):
    """Full response body of ``POST /Web/Hub/vendors/v1/orders``."""

    success: bool
    messages: list[ApiMessage]
    data: OrdersPage
