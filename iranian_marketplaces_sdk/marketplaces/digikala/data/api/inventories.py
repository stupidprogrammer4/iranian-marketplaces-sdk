"""Digikala inventories: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_stock_status: (
        Literal[
            "has_warehouse_stock",
            "has_not_warehouse_stock",
            "has_marketplace_seller_stock",
            "has_not_marketplace_seller_stock",
            "soon_out_of_stock",
        ]
        | None
    ) = Field(
        default=None,
        validation_alias="search[stock_status]",
        serialization_alias="search[stock_status]",
    )
    search_selling_stock: int | None = Field(
        default=None,
        validation_alias="search[selling_stock]",
        serialization_alias="search[selling_stock]",
    )
    search_active: int | None = Field(
        default=None, validation_alias="search[active]", serialization_alias="search[active]"
    )
    search_category_ids: int | None = Field(
        default=None,
        validation_alias="search[category_ids]",
        serialization_alias="search[category_ids]",
    )
    search_search_field: str | None = Field(
        default=None,
        validation_alias="search[search_field]",
        serialization_alias="search[search_field]",
    )
    search_product_filter: Literal["has_dead_stock", "active", "inactive"] | None = Field(
        default=None,
        validation_alias="search[product_filter]",
        serialization_alias="search[product_filter]",
    )
    search_warehouse_filter: Literal[1, 50, 28, 48, "others"] | None = Field(
        default=None,
        validation_alias="search[warehouse_filter]",
        serialization_alias="search[warehouse_filter]",
    )
    search_calculate_available_stock: bool | None = Field(
        default=None,
        validation_alias="search[calculate_available_stock]",
        serialization_alias="search[calculate_available_stock]",
    )
    search_over_30_days: int | None = Field(
        default=None,
        validation_alias="search[over_30_days]",
        serialization_alias="search[over_30_days]",
    )


class ListResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ListResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    category_title: str | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    available: int | None = Field(default=None)
    reserve: int | None = Field(default=None)
    warehouse: list[int] | None = Field(default=None)
    img_src: str | None = Field(default=None)
    shipping_nature: str | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    product_url: str | None = Field(default=None)
    supply_stock: int | None = Field(default=None)
    has_rts_package: bool | None = Field(default=None)
    has_dead_stock: bool | None = Field(default=None)
    has_rts_stock: bool | None = Field(
        default=None, validation_alias="hasRtsStock", serialization_alias="hasRtsStock"
    )
    has_checkbox_for_rts: bool | None = Field(default=None)


class ListResponseDataMetaDataWarehouses(APIResponseSchema):
    value_1: str | None = Field(default=None, validation_alias="1", serialization_alias="1")
    value_28: str | None = Field(default=None, validation_alias="28", serialization_alias="28")
    value_48: str | None = Field(default=None, validation_alias="48", serialization_alias="48")
    value_50: str | None = Field(default=None, validation_alias="50", serialization_alias="50")
    others: str | None = Field(default=None)


class DeadStockQuery(QuerySchema):
    search_serial: str | None = Field(
        default=None, validation_alias="search serial", serialization_alias="search serial"
    )


class DeadStockResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class DeadStockResponseDataItemsItem(APIResponseSchema):
    item_serial: str | None = Field(default=None)
    age: int | None = Field(default=None)
    is_passed_discount_period: str | None = Field(default=None)
    discount_period: str | int | None = Field(default=None)
    current_warehouse_title: str | None = Field(default=None)


class ExportDeadStockQuery(QuerySchema):
    search_product_variant_id: int | None = Field(
        default=None,
        validation_alias="search[product_variant_id]",
        serialization_alias="search[product_variant_id]",
    )
    search_serial: str | None = Field(
        default=None, validation_alias="search[serial]", serialization_alias="search[serial]"
    )


class ExportDeadStockResponseData(APIResponseSchema):
    file_name: str | None = Field(
        default=None, validation_alias="fileName", serialization_alias="fileName"
    )
    excel_file: str | None = Field(
        default=None, validation_alias="excelFile", serialization_alias="excelFile"
    )


class ExportRequest(RequestSchema):
    stock_status: str | None = Field(default=None)
    selling_stock: bool | None = Field(default=None)
    active: bool | None = Field(default=None)
    category_id: int | None = Field(default=None)
    search_field: JsonValue = Field(default=None)
    product_filter: str | None = Field(default=None)
    warehouse_filter: int | None = Field(default=None)


class ExportResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class ListResponseDataMetaData(APIResponseSchema):
    categories: ObjectMap[str] | None = Field(default=None)
    items_has_rts: bool | None = Field(default=None)
    warehouses: ListResponseDataMetaDataWarehouses | None = Field(default=None)


class DeadStockResponseData(APIResponseSchema):
    sort_data: DeadStockResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[DeadStockResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ExportDeadStockResponse(APIResponseSchema):
    status: int | str
    data: ExportDeadStockResponseData


class ExportResponse(APIResponseSchema):
    status: str
    data: ExportResponseData


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ListResponseDataMetaData | None = Field(default=None)


class DeadStockResponse(APIResponseSchema):
    status: str
    data: DeadStockResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


__all__ = [
    "DeadStockQuery",
    "DeadStockResponse",
    "DeadStockResponseData",
    "DeadStockResponseDataItemsItem",
    "DeadStockResponseDataSortData",
    "ExportDeadStockQuery",
    "ExportDeadStockResponse",
    "ExportDeadStockResponseData",
    "ExportRequest",
    "ExportResponse",
    "ExportResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataMetaData",
    "ListResponseDataMetaDataWarehouses",
    "ListResponseDataPager",
    "ListResponseDataSortData",
]
