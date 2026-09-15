"""Digikala orders: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["order_created_at"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_search_term: str | None = Field(
        default=None,
        validation_alias="search[search_term]",
        serialization_alias="search[search_term]",
    )
    search_created_today: bool | None = Field(
        default=None,
        validation_alias="search[created_today]",
        serialization_alias="search[created_today]",
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
    product_variant_id: int | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    order_id: int | None = Field(default=None)
    order_created_at: str | None = Field(default=None)
    warehouse_status_at: str | None = Field(default=None)
    commitment_date: str | None = Field(default=None)
    quantity: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    amazing_discount: int | None = Field(default=None)
    discount_manager: int | None = Field(default=None)
    total_price: int | None = Field(default=None)


class ListResponseDataMetaDataCancellationReasonsId(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class StatisticsResponseData(APIResponseSchema):
    all_shipped_by_dk: int | None = Field(default=None)
    shipped_by_seller_count: int | None = Field(default=None)
    seller_nearby_stores_order_count: int | None = Field(default=None)


class HistoryQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    order_type: Literal["processed", "returned", "canceled"] | None = Field(default=None)
    category_id: int | None = Field(default=None)
    order_created_at_to: str | None = Field(default=None)
    order_created_at_from: str | None = Field(default=None)
    exit_from_warehouse_date_to: str | None = Field(default=None)
    exit_from_warehouse_date_from: str | None = Field(default=None)
    returned_to_warehouse_date_to: str | None = Field(default=None)
    returned_to_warehouse_date_from: str | None = Field(default=None)
    shipping_type: Literal["seller", "digikala", "nearby"] | None = Field(default=None)
    search_text_all: str | int | None = Field(default=None)
    b2b_active: bool | None = Field(default=None)


class HistoryResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class HistoryResponseDataItemsItemCancellationInfo(APIResponseSchema):
    canceled_by: str | None = Field(default=None)
    reason: str | None = Field(default=None)


class HistoryResponseDataMetaDataAllCategories(APIResponseSchema):
    category_id: str | None = Field(default=None)


class CancelRequest(RequestSchema):
    cancellation_reason_id: int
    count: int | None = Field(default=None)


class CancelResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    status: str | None = Field(default=None)
    code: int | None = Field(default=None)


class ListResponseDataMetaDataCancellationReasons(APIResponseSchema):
    id: ListResponseDataMetaDataCancellationReasonsId | None = Field(default=None)


class StatisticsResponse(APIResponseSchema):
    status: int | str
    data: StatisticsResponseData


class HistoryResponseDataItemsItem(APIResponseSchema):
    product_variant_title: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    order_id: int | None = Field(default=None)
    shipment_id: int | None = Field(default=None)
    order_created_at: str | None = Field(default=None)
    order_status: JsonValue = Field(default=None)
    category: str | None = Field(default=None)
    product_supplier_code: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    image_src: str | None = Field(default=None)
    payment_type: JsonValue = Field(default=None)
    sell_type: JsonValue = Field(default=None)
    shipping_type: JsonValue = Field(default=None)
    unit_discount: int | None = Field(default=None)
    unit_price: int | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    serials: list[JsonValue] | None = Field(default=None)
    quantity: int | None = Field(default=None)
    discount_type: str | None = Field(default=None)
    total_price: int | None = Field(default=None)
    cancellation_info: HistoryResponseDataItemsItemCancellationInfo | None = Field(default=None)
    seller_voucher_title: str | None = Field(default=None)
    seller_voucher_amount: str | int | None = Field(default=None)
    dual_price_tag: str | None = Field(default=None)
    extra_commission_tag: str | None = Field(default=None)


class HistoryResponseDataMetaData(APIResponseSchema):
    all_categories: HistoryResponseDataMetaDataAllCategories | None = Field(default=None)
    b2b_active: bool | None = Field(default=None)


class CancelResponse(APIResponseSchema):
    status: str
    data: CancelResponseData


class ListResponseDataMetaData(APIResponseSchema):
    cancellation_reasons: ListResponseDataMetaDataCancellationReasons | None = Field(default=None)


class HistoryResponseData(APIResponseSchema):
    sort_data: HistoryResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[HistoryResponseDataItemsItem] | None = Field(default=None)
    meta_data: HistoryResponseDataMetaData | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ListResponseDataMetaData | None = Field(default=None)


class HistoryResponse(APIResponseSchema):
    status: str
    data: HistoryResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


__all__ = [
    "CancelRequest",
    "CancelResponse",
    "CancelResponseData",
    "HistoryQuery",
    "HistoryResponse",
    "HistoryResponseData",
    "HistoryResponseDataItemsItem",
    "HistoryResponseDataItemsItemCancellationInfo",
    "HistoryResponseDataMetaData",
    "HistoryResponseDataMetaDataAllCategories",
    "HistoryResponseDataSortData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataMetaData",
    "ListResponseDataMetaDataCancellationReasons",
    "ListResponseDataMetaDataCancellationReasonsId",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "StatisticsResponse",
    "StatisticsResponseData",
]
