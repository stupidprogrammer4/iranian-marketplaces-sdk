"""Digikala commitments: request and response models."""

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
    sort: Literal["variant_id", "commitment_count"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_category_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[category_ids]",
        serialization_alias="search[category_ids]",
    )
    search_shipping_nature_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[shipping_nature_ids]",
        serialization_alias="search[shipping_nature_ids]",
    )
    search_is_effective: bool | None = Field(
        default=None,
        validation_alias="search[is_effective]",
        serialization_alias="search[is_effective]",
    )
    search_to_commitment_date: str | None = Field(
        default=None,
        validation_alias="search[to_commitment_date]",
        serialization_alias="search[to_commitment_date]",
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


class ListResponseDataItemsItemSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ListResponseDataItemsItemPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListResponseDataItemsItemFormData(APIResponseSchema):
    is_past_and_today: str | None = Field(default=None)
    to_commitment_date: str | None = Field(default=None)


class ListResponseDataItemsItemItemsItemStock(APIResponseSchema):
    warehouse: int | None = Field(default=None)
    supply: int | None = Field(default=None)
    on_the_way: int | None = Field(
        default=None, validation_alias="onTheWay", serialization_alias="onTheWay"
    )
    stock: int | None = Field(default=None)


class ListResponseDataItemsItemItemsItemCommitment(APIResponseSchema):
    next_days: int | None = Field(
        default=None, validation_alias="nextDays", serialization_alias="nextDays"
    )
    today: int | None = Field(default=None)
    delayed: int | None = Field(default=None)
    all: int | None = Field(default=None)
    effective: int | None = Field(default=None)


class ListResponseDataItemsItemMetaData(APIResponseSchema):
    data_source: str | None = Field(default=None)
    supported_filters: list[str] | None = Field(default=None)
    supported_sorting: list[str] | None = Field(default=None)


class MetadataQuery(QuerySchema):
    commitment_date: str | None = Field(default=None)


class MetadataResponseDataSummaryStatistics(APIResponseSchema):
    total_commitments: int | None = Field(
        default=None, validation_alias="totalCommitments", serialization_alias="totalCommitments"
    )
    effective_commitments: int | None = Field(
        default=None,
        validation_alias="effectiveCommitments",
        serialization_alias="effectiveCommitments",
    )
    non_effective_commitments: int | None = Field(
        default=None,
        validation_alias="nonEffectiveCommitments",
        serialization_alias="nonEffectiveCommitments",
    )
    total_penalty: int | None = Field(
        default=None, validation_alias="totalPenalty", serialization_alias="totalPenalty"
    )
    effective_last_updated: str | None = Field(
        default=None,
        validation_alias="effectiveLastUpdated",
        serialization_alias="effectiveLastUpdated",
    )
    non_effective_last_updated: str | None = Field(
        default=None,
        validation_alias="nonEffectiveLastUpdated",
        serialization_alias="nonEffectiveLastUpdated",
    )


class MetadataResponseDataPackageConfig(APIResponseSchema):
    small: str | None = Field(default=None)
    medium: str | None = Field(default=None)
    heavy: str | None = Field(default=None)


class MetadataResponseDataCalendarDates(APIResponseSchema):
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    today: str | None = Field(default=None)


class MetadataResponseDataShipmentAbilitiesItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)


class MetadataResponseDataPenaltyConfig(APIResponseSchema):
    first_day: float | None = Field(
        default=None, validation_alias="firstDay", serialization_alias="firstDay"
    )
    second_day: float | None = Field(
        default=None, validation_alias="secondDay", serialization_alias="secondDay"
    )
    third_day: float | None = Field(
        default=None, validation_alias="thirdDay", serialization_alias="thirdDay"
    )
    fourth_day: float | None = Field(
        default=None, validation_alias="fourthDay", serialization_alias="fourthDay"
    )
    etc: float | None = Field(default=None)


class ExportRequestSearch(RequestSchema):
    multi_search: str | None = Field(default=None)
    category_ids: str | None = Field(default=None)
    shipping_nature_ids: str | None = Field(default=None)
    is_effective: bool | None = Field(default=None)
    to_commitment_date: str | None = Field(default=None)


class ExportResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class ExportReportRequest(RequestSchema):
    from_date: str | None = Field(
        default=None, validation_alias="fromDate", serialization_alias="fromDate"
    )
    to_date: str | None = Field(
        default=None, validation_alias="toDate", serialization_alias="toDate"
    )


class ExportReportResponse(APIResponseSchema):
    status: str
    data: ExportResponseData


class GetQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["commitment_date", "quantity"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_commitment_date: str | None = Field(
        default=None,
        validation_alias="search[commitment_date]",
        serialization_alias="search[commitment_date]",
    )


class GetResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class GetResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class GetResponseDataItemsItemSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class GetResponseDataItemsItemPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class GetResponseDataItemsItemItemsCommitmentsItem(APIResponseSchema):
    commitment_date: str | None = Field(
        default=None, validation_alias="commitmentDate", serialization_alias="commitmentDate"
    )
    type: str | None = Field(default=None)
    committed: int | None = Field(default=None)
    penalty_until_today: int | None = Field(
        default=None, validation_alias="penaltyUntilToday", serialization_alias="penaltyUntilToday"
    )
    total_penalty: int | None = Field(
        default=None, validation_alias="totalPenalty", serialization_alias="totalPenalty"
    )


class GetResponseDataItemsItemMetaDataVariantDetails(APIResponseSchema):
    id: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_id: int | None = Field(default=None)


class ListResponseDataItemsItemItemsItem(APIResponseSchema):
    variant_id: int | None = Field(
        default=None, validation_alias="variantId", serialization_alias="variantId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    brand_id: int | None = Field(
        default=None, validation_alias="brandId", serialization_alias="brandId"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    category_id: int | None = Field(
        default=None, validation_alias="categoryId", serialization_alias="categoryId"
    )
    nature_id: int | None = Field(
        default=None, validation_alias="natureId", serialization_alias="natureId"
    )
    title_fa: str | None = Field(
        default=None, validation_alias="titleFa", serialization_alias="titleFa"
    )
    supplier_code: str | None = Field(
        default=None, validation_alias="supplierCode", serialization_alias="supplierCode"
    )
    stock: ListResponseDataItemsItemItemsItemStock | None = Field(default=None)
    orders: int | None = Field(default=None)
    commitment: ListResponseDataItemsItemItemsItemCommitment | None = Field(default=None)
    on_the_way: int | None = Field(
        default=None, validation_alias="onTheWay", serialization_alias="onTheWay"
    )
    product_image: str | None = Field(default=None)
    product_link: str | None = Field(default=None)
    nature_label: str | None = Field(
        default=None, validation_alias="natureLabel", serialization_alias="natureLabel"
    )
    adverg_url: str | None = Field(default=None)


class MetadataResponseData(APIResponseSchema):
    summary_statistics: MetadataResponseDataSummaryStatistics | None = Field(default=None)
    categories: ObjectMap[str] | None = Field(default=None)
    package_config: MetadataResponseDataPackageConfig | None = Field(default=None)
    calendar_dates: MetadataResponseDataCalendarDates | None = Field(default=None)
    commitment_dates: list[str] | None = Field(default=None)
    shipment_abilities: list[MetadataResponseDataShipmentAbilitiesItem] | None = Field(default=None)
    penalty_config: MetadataResponseDataPenaltyConfig | None = Field(
        default=None, validation_alias="penaltyConfig", serialization_alias="penaltyConfig"
    )


class ExportRequest(RequestSchema):
    search: ExportRequestSearch | None = Field(default=None)
    sort: str | None = Field(default=None)
    order: str | None = Field(default=None)


class ExportResponse(APIResponseSchema):
    status: str
    data: ExportResponseData


class GetResponseDataItemsItemItems(APIResponseSchema):
    variant_id: int | None = Field(
        default=None, validation_alias="variantId", serialization_alias="variantId"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    nature_id: int | None = Field(
        default=None, validation_alias="natureId", serialization_alias="natureId"
    )
    title_fa: str | None = Field(
        default=None, validation_alias="titleFa", serialization_alias="titleFa"
    )
    supplier_code: str | None = Field(
        default=None, validation_alias="supplierCode", serialization_alias="supplierCode"
    )
    stock: ListResponseDataItemsItemItemsItemStock | None = Field(default=None)
    on_the_way: int | None = Field(
        default=None, validation_alias="onTheWay", serialization_alias="onTheWay"
    )
    orders: int | None = Field(default=None)
    commitments: list[GetResponseDataItemsItemItemsCommitmentsItem] | None = Field(default=None)
    product_image: str | None = Field(default=None)
    product_link: str | None = Field(default=None)
    nature_label: str | None = Field(default=None)
    adverge_url: str | None = Field(default=None)


class GetResponseDataItemsItemMetaData(APIResponseSchema):
    variant_id: str | None = Field(default=None)
    data_source: str | None = Field(default=None)
    variant_details: GetResponseDataItemsItemMetaDataVariantDetails | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    sort_data: ListResponseDataItemsItemSortData | None = Field(default=None)
    pager: ListResponseDataItemsItemPager | None = Field(default=None)
    form_data: ListResponseDataItemsItemFormData | None = Field(default=None)
    items: list[ListResponseDataItemsItemItemsItem] | None = Field(default=None)
    meta_data: ListResponseDataItemsItemMetaData | None = Field(default=None)


class MetadataResponse(APIResponseSchema):
    status: int | str
    data: MetadataResponseData


class GetResponseDataItemsItem(APIResponseSchema):
    sort_data: GetResponseDataItemsItemSortData | None = Field(default=None)
    pager: GetResponseDataItemsItemPager | None = Field(default=None)
    form_data: list[str] | None = Field(default=None)
    items: GetResponseDataItemsItemItems | None = Field(default=None)
    meta_data: GetResponseDataItemsItemMetaData | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    sort_data: GetResponseDataSortData | None = Field(default=None)
    pager: GetResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class GetResponse(APIResponseSchema):
    status: str
    data: GetResponseData


__all__ = [
    "ExportReportRequest",
    "ExportReportResponse",
    "ExportRequest",
    "ExportRequestSearch",
    "ExportResponse",
    "ExportResponseData",
    "GetQuery",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataItemsItem",
    "GetResponseDataItemsItemItems",
    "GetResponseDataItemsItemItemsCommitmentsItem",
    "GetResponseDataItemsItemMetaData",
    "GetResponseDataItemsItemMetaDataVariantDetails",
    "GetResponseDataItemsItemPager",
    "GetResponseDataItemsItemSortData",
    "GetResponseDataPager",
    "GetResponseDataSortData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemFormData",
    "ListResponseDataItemsItemItemsItem",
    "ListResponseDataItemsItemItemsItemCommitment",
    "ListResponseDataItemsItemItemsItemStock",
    "ListResponseDataItemsItemMetaData",
    "ListResponseDataItemsItemPager",
    "ListResponseDataItemsItemSortData",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "MetadataQuery",
    "MetadataResponse",
    "MetadataResponseData",
    "MetadataResponseDataCalendarDates",
    "MetadataResponseDataPackageConfig",
    "MetadataResponseDataPenaltyConfig",
    "MetadataResponseDataShipmentAbilitiesItem",
    "MetadataResponseDataSummaryStatistics",
]
