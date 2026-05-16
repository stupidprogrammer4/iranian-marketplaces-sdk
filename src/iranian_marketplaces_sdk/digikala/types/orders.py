"""TypedDicts for the Digikala order endpoints (orders + orders/history)."""

from typing import NotRequired, TypedDict

from .common import KeyTitle, Pager, RateLimit, SortData

__all__ = [
    "OrderItem",
    "CancellationReason",
    "OrdersMetaData",
    "OrdersData",
    "OrdersResponse",
    "OrderSearch",
    "OrderHistorySerial",
    "OrderCancellationInfo",
    "OrderHistoryItem",
    "OrderHistoryMetaData",
    "OrderHistoryData",
    "OrderHistoryResponse",
    "OrderHistoryFilters",
]


class OrderItem(TypedDict):
    """A single active order item for the seller."""

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


class CancellationReason(TypedDict):
    """A cancellation reason entry inside order list metadata."""

    key: str
    title: str


class OrdersMetaData(TypedDict, total=False):
    """Extra metadata of an order list response.

    ``cancellation_reasons`` maps a reason id to its key/title.
    """

    cancellation_reasons: dict[str, CancellationReason]


class OrdersData(TypedDict):
    """The ``data`` payload of an order list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[OrderItem]
    meta_data: OrdersMetaData


class OrdersResponse(TypedDict):
    """Full response body returned by ``GET /orders``."""

    status: str
    data: OrdersData


class OrderSearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /orders``."""

    search_term: str
    created_today: bool


class OrderHistorySerial(TypedDict):
    """A single serial attached to an order-history item."""

    serial: str
    order_shipped_at: str | None
    return_to_warehouse_at: str | None
    warehouse_title: str
    serial_status: KeyTitle
    return_reason: str | None
    agent_note: str | None


class OrderCancellationInfo(TypedDict):
    """Cancellation detail of an order-history item."""

    canceled_by: str
    reason: str


class OrderHistoryItem(TypedDict):
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
    seller_voucher_title: str | None
    seller_voucher_amount: int
    total_price: int
    cancellation_info: OrderCancellationInfo | None
    dual_price_tag: str
    extra_commission_tag: str


class OrderHistoryMetaData(TypedDict, total=False):
    """Extra metadata of an order-history response."""

    all_categories: dict[str, str]
    b2b_active: bool


class OrderHistoryData(TypedDict):
    """The ``data`` payload of an order-history response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[OrderHistoryItem]
    meta_data: OrderHistoryMetaData
    rate_limit: NotRequired[RateLimit]


class OrderHistoryResponse(TypedDict):
    """Full response body returned by ``GET /orders/history``."""

    status: str
    data: OrderHistoryData


class OrderHistoryFilters(TypedDict, total=False):
    """Optional flat query filters accepted by ``GET /orders/history``.

    Date fields use the ``Y-m-d\\TH:i:s.v\\Z`` format.
    """

    order_type: str
    category_id: int
    order_created_at_to: str
    order_created_at_from: str
    exit_from_warehouse_date_to: str
    exit_from_warehouse_date_from: str
    returned_to_warehouse_date_to: str
    returned_to_warehouse_date_from: str
    shipping_type: str
    search_text_all: str | int
    b2b_active: bool
