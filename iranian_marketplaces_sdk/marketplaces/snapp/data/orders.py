"""Snapp Shop — the vendor-orders endpoints.

The customer ``address`` comes back as an empty list with no published element schema, so it is
left open rather than invented.
"""

from typing import Any

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.snapp.data.common import CursorMeta

__all__ = [
    "OrderCustomer",
    "OrderItem",
    "OrderPickupTime",
    "VendorOrder",
    "VendorOrderResponse",
    "VendorOrdersQuery",
    "VendorOrdersResponse",
]


class OrderPickupTime(ResponseSchema):
    """Pickup window of an order — when the courier will be at the store (``%Y-%m-%d %H:%M:%S``)."""

    start: str
    end: str


class OrderCustomer(ResponseSchema):
    """Customer attached to a vendor order."""

    first_name: str
    last_name: str
    phone: str
    national_id: str
    address: list[Any]


class OrderItem(ResponseSchema):
    """A single line item of a vendor order.

    ``canceled_quantity`` is subtracted from ``quantity``: an item can be partly cancelled, so the
    amount to actually fulfil is the difference.
    """

    sku: str
    vendor_product_info_id: str
    item_status: str
    quantity: int
    canceled_quantity: int
    original_price: int
    discount_amount: int
    final_price: int


class VendorOrder(ResponseSchema):
    """A single Snapp vendor order. Timestamps use ``%Y-%m-%d %H:%M:%S``."""

    order_number: int
    created_at: str
    delivery_type: str
    order_status: str
    item_origin: str
    point_of_sales_at: str
    pickup_time: OrderPickupTime
    customer: OrderCustomer
    items: list[OrderItem]


class VendorOrdersResponse(ResponseSchema):
    """Full response body of ``GET /vendors/{seller_id}/orders``."""

    status: bool
    data: list[VendorOrder]
    meta: CursorMeta


class VendorOrderResponse(ResponseSchema):
    """Full response body of ``GET /vendors/{seller_id}/orders/{order_number}``."""

    status: bool
    data: VendorOrder


class VendorOrdersQuery(QuerySchema):
    """Query filters for the vendor-orders endpoint.

    Cursor-paginated: leave ``cursor`` unset for the first page, then pass
    ``meta.pagination.next_cursor`` back while ``has_more`` is true. Dates are ``%Y-%m-%d``.
    """

    per_page: int | None = None
    cursor: str | None = None
    start_date: str | None = None
    end_date: str | None = None
