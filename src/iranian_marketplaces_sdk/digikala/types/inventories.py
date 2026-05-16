"""TypedDicts for the Digikala inventory endpoints."""

from typing import TypedDict

from .common import Pager, SortData

__all__ = [
    "InventoryItem",
    "InventoryMetaData",
    "InventoriesData",
    "InventoriesResponse",
    "InventorySearch",
    "InventoryDeadStockItem",
    "InventoryDeadStockData",
    "InventoryDeadStockResponse",
]


class InventoryItem(TypedDict):
    """A single seller inventory line item."""

    category_title: str
    supplier_code: str
    product_id: int
    product_variant_id: int
    title: str
    marketplace_seller_stock: int
    warehouse_stock: int
    available: int
    reserve: int
    warehouse: list[int]
    img_src: str
    shipping_nature: str
    shipping_nature_id: int
    product_url: str
    supply_stock: int
    has_rts_package: bool
    has_dead_stock: bool
    hasRtsStock: bool
    has_checkbox_for_rts: bool


class InventoryMetaData(TypedDict, total=False):
    """Extra metadata of an inventory list response."""

    categories: dict[str, str]
    items_has_rts: bool
    warehouses: dict[str, str]


class InventoriesData(TypedDict):
    """The ``data`` payload of an inventory list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InventoryItem]
    meta_data: InventoryMetaData


class InventoriesResponse(TypedDict):
    """Full response body returned by ``GET /inventories``."""

    status: str
    data: InventoriesData


class InventorySearch(TypedDict, total=False):
    """Optional ``search[...]`` filters accepted by ``GET /inventories``.

    ``selling_stock`` and ``active`` must be ``0`` or ``1``.
    """

    stock_status: str
    selling_stock: int
    active: int
    # Sent comma-joined.
    category_ids: list[int]
    search_field: str
    product_filter: str
    warehouse_filter: str
    calculate_available_stock: bool
    over_30_days: int


class InventoryDeadStockItem(TypedDict):
    """A single dead-stock serial entry for a product variant."""

    item_serial: str
    age: int
    is_passed_discount_period: str
    discount_period: int
    current_warehouse_title: str


class InventoryDeadStockData(TypedDict):
    """The ``data`` payload of an inventory dead-stock response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InventoryDeadStockItem]
    meta_data: dict[str, object]


class InventoryDeadStockResponse(TypedDict):
    """Full response body of ``GET /inventories/{product_variant_id}``."""

    status: str
    data: InventoryDeadStockData
