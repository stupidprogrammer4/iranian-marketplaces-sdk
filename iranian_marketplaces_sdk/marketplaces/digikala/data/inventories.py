"""Digikala — the inventory endpoints (scope: ``inventory``).

Stock as Digikala sees it, per product variant and per warehouse, plus the dead-stock view: units
that have sat long enough to be eligible for a forced discount.
"""

from typing import Any

from pydantic import Field

from iranian_marketplaces_sdk.common.data import QuerySchema, ResponseSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.common import Pager, SortData

__all__ = [
    "InventoriesData",
    "InventoriesResponse",
    "InventoryDeadStockData",
    "InventoryDeadStockItem",
    "InventoryDeadStockResponse",
    "InventoryItem",
    "InventoryMetaData",
    "InventorySearch",
]


class InventoryItem(ResponseSchema):
    """A single seller inventory line item.

    ``available`` is what a customer can still buy: warehouse stock minus what is already reserved
    against open orders.
    """

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
    has_rts_stock: bool = Field(validation_alias="hasRtsStock", serialization_alias="hasRtsStock")
    has_checkbox_for_rts: bool


class InventoryMetaData(ResponseSchema):
    """Extra metadata of an inventory list response: the id/title lookups for its filters."""

    categories: dict[str, str] | None = None
    items_has_rts: bool | None = None
    warehouses: dict[str, str] | None = None


class InventoriesData(ResponseSchema):
    """The ``data`` payload of an inventory list response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InventoryItem]
    meta_data: InventoryMetaData


class InventoriesResponse(ResponseSchema):
    """Full response body returned by ``GET /inventories``."""

    status: str
    data: InventoriesData


class InventorySearch(QuerySchema):
    """The ``search[...]`` filters accepted by ``GET /inventories``.

    ``selling_stock`` and ``active`` are the API's integer booleans: pass ``0`` or ``1``.
    """

    stock_status: str | None = None
    selling_stock: int | None = None
    active: int | None = None
    category_ids: list[int] | None = None
    search_field: str | None = None
    product_filter: str | None = None
    warehouse_filter: str | None = None
    calculate_available_stock: bool | None = None
    over_30_days: int | None = None


class InventoryDeadStockItem(ResponseSchema):
    """A single dead-stock serial entry for a product variant.

    ``age`` is days in the warehouse; once it passes ``discount_period``,
    ``is_passed_discount_period`` flips and the unit becomes eligible for a mandatory discount.
    """

    item_serial: str
    age: int
    is_passed_discount_period: str
    discount_period: int
    current_warehouse_title: str


class InventoryDeadStockData(ResponseSchema):
    """The ``data`` payload of an inventory dead-stock response."""

    sort_data: SortData
    pager: Pager
    form_data: list[None]
    items: list[InventoryDeadStockItem]
    meta_data: dict[str, Any]


class InventoryDeadStockResponse(ResponseSchema):
    """Full response body of ``GET /inventories/{product_variant_id}``."""

    status: str
    data: InventoryDeadStockData
