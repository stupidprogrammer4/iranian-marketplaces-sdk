"""Digikala — the order endpoints (scope: ``order``).

Two endpoints with two different shapes. ``GET /orders`` is the working queue: items that are
still owed to a customer. ``GET /orders/history`` is the record: everything ever sold, with its
serials, its cancellation reason, and how it was paid — and its filters are flat query parameters
rather than the ``search[...]`` form used everywhere else.
"""

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import (
    KeyTitle,
    Pager,
    RateLimit,
    SortData,
)

__all__ = [
    "CancellationReason",
    "OrderCancellationInfo",
    "OrderHistoryData",
    "OrderHistoryFilters",
    "OrderHistoryItem",
    "OrderHistoryMetaData",
    "OrderHistoryResponse",
    "OrderHistorySerial",
    "OrderItem",
    "OrderSearch",
    "OrdersData",
    "OrdersMetaData",
    "OrdersResponse",
]


class OrderItem(ResponseSchema):
    """A single active order item for the seller.

    ``commitment_date`` is the deadline the order must reach the warehouse by — the field that
    decides whether an order counts as late.
    """

    product_variant_id: int
    product_image_url: str
    product_variant_title: str
    supplier_code: str
    order_id: int
    order_created_at: str
    warehouse_status_at: str
    commitment_date: str
    quantity: int
    selling_price: int
    amazing_discount: int
    discount_manager: int
    total_price: int


class CancellationReason(ResponseSchema):
    """A cancellation reason entry inside order list metadata."""

    key: str
    title: str


class OrdersMetaData(ResponseSchema):
    """Extra metadata of an order list response.

    ``cancellation_reasons`` maps a reason id to its key/title — the lookup table for the ids that
    appear on cancelled items.
    """

    cancellation_reasons: dict[str, CancellationReason] | None = None


class OrdersData(ResponseSchema):
    """The ``data`` payload of an order list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[OrderItem]
    meta_data: OrdersMetaData


class OrdersResponse(ResponseSchema):
    """Full response body returned by ``GET /orders``."""

    status: str
    data: OrdersData


class OrderSearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /orders``."""

    search_term: str | None = None
    created_today: bool | None = None


class OrderHistorySerial(ResponseSchema):
    """A single serial attached to an order-history item.

    One physical unit. ``return_to_warehouse_at`` and ``return_reason`` are how a returned item is
    told apart from a delivered one at the unit level.
    """

    serial: str
    order_shipped_at: str | None = None
    return_to_warehouse_at: str | None = None
    warehouse_title: str
    serial_status: KeyTitle
    return_reason: str | None = None
    agent_note: str | None = None


class OrderCancellationInfo(ResponseSchema):
    """Cancellation detail of an order-history item."""

    canceled_by: str
    reason: str


class OrderHistoryItem(ResponseSchema):
    """A single order-history line item."""

    product_variant_title: str
    product_id: int
    product_variant_id: int
    order_id: int
    shipment_id: int
    order_created_at: str
    order_status: KeyTitle
    category: str
    product_supplier_code: str
    product_url: str
    image_src: str
    payment_type: KeyTitle
    sell_type: KeyTitle
    shipping_type: KeyTitle
    unit_discount: int
    unit_price: int
    lead_time: int
    serials: list[OrderHistorySerial]
    quantity: int
    discount_type: str
    seller_voucher_title: str | None = None
    seller_voucher_amount: int
    total_price: int
    cancellation_info: OrderCancellationInfo | None = None
    dual_price_tag: str
    extra_commission_tag: str


class OrderHistoryMetaData(ResponseSchema):
    """Extra metadata of an order-history response."""

    all_categories: dict[str, str] | None = None
    b2b_active: bool | None = None


class OrderHistoryData(ResponseSchema):
    """The ``data`` payload of an order-history response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[OrderHistoryItem]
    meta_data: OrderHistoryMetaData
    rate_limit: RateLimit | None = None


class OrderHistoryResponse(ResponseSchema):
    """Full response body returned by ``GET /orders/history``."""

    status: str
    data: OrderHistoryData


class OrderHistoryFilters(QuerySchema):
    """The flat query filters accepted by ``GET /orders/history``.

    Not the ``search[...]`` form — these are top-level query parameters. Date fields use
    ``Y-m-d\\TH:i:s.v\\Z``.
    """

    order_type: str | None = None
    category_id: int | None = None
    order_created_at_to: str | None = None
    order_created_at_from: str | None = None
    exit_from_warehouse_date_to: str | None = None
    exit_from_warehouse_date_from: str | None = None
    returned_to_warehouse_date_to: str | None = None
    returned_to_warehouse_date_from: str | None = None
    shipping_type: str | None = None
    search_text_all: str | int | None = None
    b2b_active: bool | None = None
