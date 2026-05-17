"""TypedDicts for the Snapp vendor-orders endpoint.

The customer ``address`` is an empty list in the sample with no published
element schema, so it is typed ``list[object]`` deliberately (not invented,
not ``Any``).

NOTE: this package must NOT use ``from __future__ import annotations``.
"""

from typing import TypedDict

from .common import CursorMeta

__all__ = [
    "OrderPickupTime",
    "OrderCustomer",
    "OrderItem",
    "VendorOrder",
    "VendorOrdersResponse",
    "VendorOrderResponse",
    "VendorOrdersQuery",
]


class OrderPickupTime(TypedDict):
    """Pickup window of an order (``%Y-%m-%d %H:%M:%S``)."""

    start: str
    end: str


class OrderCustomer(TypedDict):
    """Customer attached to a vendor order."""

    first_name: str
    last_name: str
    phone: str
    national_id: str
    address: list[object]


class OrderItem(TypedDict):
    """A single line item of a vendor order."""

    sku: str
    vendor_product_info_id: str
    item_status: str
    quantity: int
    canceled_quantity: int
    original_price: int
    discount_amount: int
    final_price: int


class VendorOrder(TypedDict):
    """A single Snapp vendor order.

    ``created_at`` / ``point_of_sales_at`` use ``%Y-%m-%d %H:%M:%S``.
    """

    order_number: int
    created_at: str
    delivery_type: str
    order_status: str
    item_origin: str
    point_of_sales_at: str
    pickup_time: OrderPickupTime
    customer: OrderCustomer
    items: list[OrderItem]


class VendorOrdersResponse(TypedDict):
    """Full response body of ``GET /vendors/{seller_id}/orders``."""

    status: bool
    data: list[VendorOrder]
    meta: CursorMeta


class VendorOrderResponse(TypedDict):
    """Full response body of ``GET /vendors/{seller_id}/orders/{order_number}``."""

    status: bool
    data: VendorOrder


class VendorOrdersQuery(TypedDict, total=False):
    """Optional query filters for the vendor-orders endpoint.

    ``start_date`` / ``end_date`` use the ``%Y-%m-%d`` format.
    """

    per_page: int
    cursor: str
    start_date: str
    end_date: str
