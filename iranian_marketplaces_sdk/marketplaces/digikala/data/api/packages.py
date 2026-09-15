"""Digikala packages: request and response models."""

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
    sort: Literal["id", "created_at"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_multi_search: str | int | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_type: Literal["order_fulfilment", "consignment"] | None = Field(
        default=None, validation_alias="search[type]", serialization_alias="search[type]"
    )
    search_status: (
        Literal["new", "received", "partially_received", "rejected", "error", "deleted"] | None
    ) = Field(default=None, validation_alias="search[status]", serialization_alias="search[status]")
    search_delivery_type: (
        Literal["seller", "digikala", "mobile_hub", "post", "compensation", "retail_consignment"]
        | None
    ) = Field(
        default=None,
        validation_alias="search[delivery_type]",
        serialization_alias="search[delivery_type]",
    )
    search_package_created_at_from: str | None = Field(
        default=None,
        validation_alias="search[package_created_at_from]",
        serialization_alias="search[package_created_at_from]",
    )
    search_package_created_at_to: str | None = Field(
        default=None,
        validation_alias="search[package_created_at_to]",
        serialization_alias="search[package_created_at_to]",
    )
    search_package_received_at_from: str | None = Field(
        default=None,
        validation_alias="search[package_received_at_from]",
        serialization_alias="search[package_received_at_from]",
    )
    search_package_received_at_to: str | None = Field(
        default=None,
        validation_alias="search[package_received_at_to]",
        serialization_alias="search[package_received_at_to]",
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


class ListResponseDataItemsItemType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItemShippingNature(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItemStatus(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItemDeliveryType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItemWarehouse(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItemTimeCope(APIResponseSchema):
    start: int | None = Field(default=None)
    end: int | None = Field(default=None)


class ListResponseDataMetaDataFiltersPackageDeliveryTypesItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataMetaDataFiltersPackageTypesItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataMetaDataFiltersPackageStatusesItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class CreateRequest(RequestSchema):
    packages: dict[str, JsonValue]
    package_type: str


class WarehousesQuery(QuerySchema):
    delivery_type: (
        Literal["seller", "digikala", "mobile_hub", "post", "compensation", "retail_consignment"]
        | None
    ) = Field(default=None)
    shipping_nature_id: Literal[1, 2] | None = Field(default=None)


class WarehousesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class WarehousesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class WarehousesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    address: str | None = Field(default=None)
    postal_code: str | None = Field(default=None)
    latitude: str | None = Field(default=None)
    longitude: str | None = Field(default=None)


class WarehouseCapacitiesQuery(QuerySchema):
    delivery_type: Literal["digikala", "mobile_hub", "seller"]
    date: str
    package_type: Literal["order_fulfilment", "consignment"]
    shipping_nature_id: int | None = Field(default=None)
    variants: list[int]
    counts: list[int]


class WarehouseCapacitiesResponseDataCapacitiesItem(APIResponseSchema):
    capacity_id: int | None = Field(default=None)
    starts_at: int | None = Field(default=None)
    ends_at: int | None = Field(default=None)
    date: str | None = Field(default=None)
    remained_size_chunk: int | None = Field(default=None)
    disabled: bool | None = Field(default=None)


class CalculateWarehouseCapacitiesRequest(RequestSchema):
    delivery_type: str | None = Field(default=None)
    date: str | None = Field(default=None)
    package_type: str | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    variants: list[int] | None = Field(default=None)
    counts: list[int] | None = Field(default=None)


class GetQuery(QuerySchema):
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )


class GetResponseDataItemsItemPackageProductsItemSerialsItemStatus(APIResponseSchema):
    status_en: str | None = Field(
        default=None, validation_alias="status en", serialization_alias="status en"
    )


class GetResponseDataItemsItemPackageProductsItemStatus(APIResponseSchema):
    status_en: str | None = Field(
        default=None, validation_alias="status en", serialization_alias="status en"
    )


class GetResponseDataMetaDataPackageDeliveryType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class GetResponseDataMetaDataPackageStatus(APIResponseSchema):
    status: str | None = Field(default=None)


class GetResponseDataMetaDataPackageReceivedWarehouse(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class GetResponseDataMetaDataPackageReceivedTimeScope(APIResponseSchema):
    start: int | None = Field(default=None)
    end: int | None = Field(default=None)


class GetResponseDataMetaDataShippingNature(APIResponseSchema):
    shipping_nature_id: str | None = Field(default=None)


class GetResponseDataMetaDataStatusCountStatus(APIResponseSchema):
    count: int | None = Field(default=None)
    title: str | None = Field(default=None)


class ExportQuery(QuerySchema):
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )


class ExportResponseData(APIResponseSchema):
    file_link: str | None = Field(default=None)


class ConsignmentVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    variant_ids: list[int] | None = Field(default=None)


class ConsignmentVariantsResponseDataItemsItemShippingNatureIdShippingNature(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature(
    APIResponseSchema
):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ConsignmentVariantsResponseDataMetaDataPackageInfosShipmentAbilities(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class FulfilmentVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["commitment_date"] | None = Field(default=None)
    order: str | None = Field(default=None)
    order_item_ids: list[int] | None = Field(
        default=None, validation_alias="[order_item_ids]", serialization_alias="[order_item_ids]"
    )
    order_commitment_type: int | None = Field(
        default=None,
        validation_alias="[order_commitment_type]",
        serialization_alias="[order_commitment_type]",
    )
    search_commitment_to: str | None = Field(
        default=None,
        validation_alias="search[commitment_to]",
        serialization_alias="search[commitment_to]",
    )


class FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature(
    APIResponseSchema
):
    title: str | None = Field(default=None)
    key: str | None = Field(default=None)


class FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemAvailableStock(
    APIResponseSchema
):
    on_the_way_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)


class FilterFulfilmentVariantsRequest(RequestSchema):
    order_item_ids: list[int] | None = Field(default=None)


class ConsignmentQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["_id", "sale_quantity"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_shipping_nature_id: Literal[1, 3, 2] | None = Field(
        default=None,
        validation_alias="search[shipping_nature_id]",
        serialization_alias="search[shipping_nature_id]",
    )
    search_selected_variant_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[selected_variant_ids]",
        serialization_alias="search[selected_variant_ids]",
    )


class ConsignmentResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ConsignmentResponseDataItemsItemShippingNature(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    package_id: int | None = Field(default=None)
    package_number: str | None = Field(default=None)
    type: ListResponseDataItemsItemType | None = Field(default=None)
    shipping_nature: ListResponseDataItemsItemShippingNature | None = Field(default=None)
    status: ListResponseDataItemsItemStatus | None = Field(default=None)
    delivery_type: ListResponseDataItemsItemDeliveryType | None = Field(default=None)
    created_at: str | None = Field(default=None)
    received_at_forecast: str | None = Field(default=None)
    received_at: str | None = Field(default=None)
    effective_received_date: str | None = Field(default=None)
    warehouse: ListResponseDataItemsItemWarehouse | None = Field(default=None)
    is_shippable_by_dk: bool | None = Field(default=None)
    time_cope: ListResponseDataItemsItemTimeCope | None = Field(default=None)
    can_delete: bool | None = Field(default=None)
    show_print_label_package: bool | None = Field(default=None)
    show_print_label_serials: bool | None = Field(default=None)
    show_print_receive_receipt: bool | None = Field(default=None)
    package_label_html_uri: str | None = Field(default=None)
    package_label_pdf_uri: str | None = Field(default=None)


class ListResponseDataMetaDataFilters(APIResponseSchema):
    package_delivery_types: list[ListResponseDataMetaDataFiltersPackageDeliveryTypesItem] | None = (
        Field(default=None)
    )
    package_types: list[ListResponseDataMetaDataFiltersPackageTypesItem] | None = Field(
        default=None
    )
    package_statuses: list[ListResponseDataMetaDataFiltersPackageStatusesItem] | None = Field(
        default=None
    )


class WarehousesResponseData(APIResponseSchema):
    sort_data: WarehousesResponseDataSortData | None = Field(default=None)
    pager: WarehousesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[WarehousesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class WarehouseCapacitiesResponseData(APIResponseSchema):
    capacities: list[WarehouseCapacitiesResponseDataCapacitiesItem] | None = Field(default=None)
    price: str | None = Field(default=None)


class CalculateWarehouseCapacitiesResponse(APIResponseSchema):
    status: int | str
    data: WarehouseCapacitiesResponseData


class GetResponseDataItemsItemPackageProductsItemSerialsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    serial: str | None = Field(default=None)
    expiration_date: str | None = Field(default=None)
    production_date: str | None = Field(default=None)
    status: GetResponseDataItemsItemPackageProductsItemSerialsItemStatus | None = Field(
        default=None
    )
    show_print_label_package: bool | None = Field(default=None)


class GetResponseDataMetaDataPackageReceived(APIResponseSchema):
    date: str | None = Field(default=None)
    warehouse: GetResponseDataMetaDataPackageReceivedWarehouse | None = Field(default=None)
    time_scope: GetResponseDataMetaDataPackageReceivedTimeScope | None = Field(default=None)


class GetResponseDataMetaDataStatusCount(APIResponseSchema):
    status: GetResponseDataMetaDataStatusCountStatus | None = Field(default=None)


class ExportResponse(APIResponseSchema):
    status: int | str
    data: ExportResponseData


class ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem(APIResponseSchema):
    product_variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_id: str | int | None = Field(default=None)
    shipping_nature: (
        ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature | None
    ) = Field(default=None)
    supplier_code: str | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    dk_inventory: int | None = Field(default=None)
    allowed_consignment_count: int | None = Field(default=None)


class ConsignmentVariantsResponseDataMetaDataPackageInfos(APIResponseSchema):
    shipment_abilities: (
        ConsignmentVariantsResponseDataMetaDataPackageInfosShipmentAbilities | None
    ) = Field(default=None)


class FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem(APIResponseSchema):
    variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    product_id: int | str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_url_on_dk_site: str | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    shipping_nature: (
        FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature | None
    ) = Field(default=None)
    quantity: int | None = Field(default=None)
    available_stock: (
        FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemAvailableStock | None
    ) = Field(default=None)
    sent_optimal: int | bool | None = Field(default=None)
    has_imei: bool | None = Field(
        default=None, validation_alias="has_IMEI", serialization_alias="has_IMEI"
    )
    has_expiry_date: bool | None = Field(default=None)


class ConsignmentResponseDataItemsItem(APIResponseSchema):
    product_variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    link_to_product: str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    shipping_nature: ConsignmentResponseDataItemsItemShippingNature | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    dk_inventory: int | None = Field(default=None)
    allowed_count_consignment: int | None = Field(default=None)


class ListResponseDataMetaData(APIResponseSchema):
    filters: ListResponseDataMetaDataFilters | None = Field(default=None)
    is_shipment_allowed: bool | None = Field(default=None)


class WarehousesResponse(APIResponseSchema):
    status: str
    data: WarehousesResponseData


class WarehouseCapacitiesResponse(APIResponseSchema):
    status: int | str
    data: WarehouseCapacitiesResponseData


class GetResponseDataItemsItemPackageProductsItem(APIResponseSchema):
    package_item_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    dkp: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    dkpc: int | None = Field(default=None)
    delivered_count: int | None = Field(default=None)
    ordered_count: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    serials: list[GetResponseDataItemsItemPackageProductsItemSerialsItem] | None = Field(
        default=None
    )
    image: str | None = Field(default=None)
    status: GetResponseDataItemsItemPackageProductsItemStatus | None = Field(default=None)


class GetResponseDataMetaData(APIResponseSchema):
    package_id: int | None = Field(default=None)
    package_number: str | None = Field(default=None)
    package_delivery_type: GetResponseDataMetaDataPackageDeliveryType | None = Field(default=None)
    seller_created: bool | None = Field(default=None)
    package_status: GetResponseDataMetaDataPackageStatus | None = Field(default=None)
    package_received: GetResponseDataMetaDataPackageReceived | None = Field(default=None)
    shipping_nature: GetResponseDataMetaDataShippingNature | None = Field(default=None)
    status_count: GetResponseDataMetaDataStatusCount | None = Field(default=None)
    show_export_receipt: bool | None = Field(default=None)
    package_label_html_uri: str | None = Field(default=None)
    package_label_pdf_uri: str | None = Field(default=None)


class ConsignmentVariantsResponseDataItemsItemShippingNatureId(APIResponseSchema):
    shipping_nature: (
        ConsignmentVariantsResponseDataItemsItemShippingNatureIdShippingNature | None
    ) = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    variants: list[ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem] | None = (
        Field(default=None)
    )


class ConsignmentVariantsResponseDataMetaData(APIResponseSchema):
    package_infos: ConsignmentVariantsResponseDataMetaDataPackageInfos | None = Field(default=None)


class FulfilmentVariantsResponseDataItemsItemShippingNatureId(APIResponseSchema):
    shipping_nature: (
        ConsignmentVariantsResponseDataItemsItemShippingNatureIdShippingNature | None
    ) = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    variants: list[FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem] | None = (
        Field(default=None)
    )


class ConsignmentResponseData(APIResponseSchema):
    sort_data: ConsignmentResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ConsignmentResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ListResponseDataMetaData | None = Field(default=None)


class GetResponseDataItemsItem(APIResponseSchema):
    package_products: list[GetResponseDataItemsItemPackageProductsItem] | None = Field(default=None)


class ConsignmentVariantsResponseDataItemsItem(APIResponseSchema):
    shipping_nature_id: ConsignmentVariantsResponseDataItemsItemShippingNatureId | None = Field(
        default=None
    )


class FulfilmentVariantsResponseDataItemsItem(APIResponseSchema):
    shipping_nature_id: FulfilmentVariantsResponseDataItemsItemShippingNatureId | None = Field(
        default=None
    )


class ConsignmentResponse(APIResponseSchema):
    status: str
    data: ConsignmentResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class GetResponseData(APIResponseSchema):
    sort_data: WarehousesResponseDataSortData | None = Field(default=None)
    pager: WarehousesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetResponseDataItemsItem] | None = Field(default=None)
    meta_data: GetResponseDataMetaData | None = Field(default=None)


class ConsignmentVariantsResponseData(APIResponseSchema):
    sort_data: WarehousesResponseDataSortData | None = Field(default=None)
    pager: WarehousesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ConsignmentVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ConsignmentVariantsResponseDataMetaData | None = Field(default=None)


class FulfilmentVariantsResponseData(APIResponseSchema):
    sort_data: WarehousesResponseDataSortData | None = Field(default=None)
    pager: WarehousesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[FulfilmentVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ConsignmentVariantsResponseDataMetaData | None = Field(default=None)


class FilterFulfilmentVariantsResponse(APIResponseSchema):
    status: str
    data: FulfilmentVariantsResponseData


class GetResponse(APIResponseSchema):
    status: str
    data: GetResponseData


class ConsignmentVariantsResponse(APIResponseSchema):
    status: str
    data: ConsignmentVariantsResponseData


class FulfilmentVariantsResponse(APIResponseSchema):
    status: str
    data: FulfilmentVariantsResponseData


__all__ = [
    "CalculateWarehouseCapacitiesRequest",
    "CalculateWarehouseCapacitiesResponse",
    "ConsignmentQuery",
    "ConsignmentResponse",
    "ConsignmentResponseData",
    "ConsignmentResponseDataItemsItem",
    "ConsignmentResponseDataItemsItemShippingNature",
    "ConsignmentResponseDataSortData",
    "ConsignmentVariantsQuery",
    "ConsignmentVariantsResponse",
    "ConsignmentVariantsResponseData",
    "ConsignmentVariantsResponseDataItemsItem",
    "ConsignmentVariantsResponseDataItemsItemShippingNatureId",
    "ConsignmentVariantsResponseDataItemsItemShippingNatureIdShippingNature",
    "ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem",
    "ConsignmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature",
    "ConsignmentVariantsResponseDataMetaData",
    "ConsignmentVariantsResponseDataMetaDataPackageInfos",
    "ConsignmentVariantsResponseDataMetaDataPackageInfosShipmentAbilities",
    "CreateRequest",
    "ExportQuery",
    "ExportResponse",
    "ExportResponseData",
    "FilterFulfilmentVariantsRequest",
    "FilterFulfilmentVariantsResponse",
    "FulfilmentVariantsQuery",
    "FulfilmentVariantsResponse",
    "FulfilmentVariantsResponseData",
    "FulfilmentVariantsResponseDataItemsItem",
    "FulfilmentVariantsResponseDataItemsItemShippingNatureId",
    "FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItem",
    "FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemAvailableStock",
    "FulfilmentVariantsResponseDataItemsItemShippingNatureIdVariantsItemShippingNature",
    "GetQuery",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataItemsItem",
    "GetResponseDataItemsItemPackageProductsItem",
    "GetResponseDataItemsItemPackageProductsItemSerialsItem",
    "GetResponseDataItemsItemPackageProductsItemSerialsItemStatus",
    "GetResponseDataItemsItemPackageProductsItemStatus",
    "GetResponseDataMetaData",
    "GetResponseDataMetaDataPackageDeliveryType",
    "GetResponseDataMetaDataPackageReceived",
    "GetResponseDataMetaDataPackageReceivedTimeScope",
    "GetResponseDataMetaDataPackageReceivedWarehouse",
    "GetResponseDataMetaDataPackageStatus",
    "GetResponseDataMetaDataShippingNature",
    "GetResponseDataMetaDataStatusCount",
    "GetResponseDataMetaDataStatusCountStatus",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemDeliveryType",
    "ListResponseDataItemsItemShippingNature",
    "ListResponseDataItemsItemStatus",
    "ListResponseDataItemsItemTimeCope",
    "ListResponseDataItemsItemType",
    "ListResponseDataItemsItemWarehouse",
    "ListResponseDataMetaData",
    "ListResponseDataMetaDataFilters",
    "ListResponseDataMetaDataFiltersPackageDeliveryTypesItem",
    "ListResponseDataMetaDataFiltersPackageStatusesItem",
    "ListResponseDataMetaDataFiltersPackageTypesItem",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "WarehouseCapacitiesQuery",
    "WarehouseCapacitiesResponse",
    "WarehouseCapacitiesResponseData",
    "WarehouseCapacitiesResponseDataCapacitiesItem",
    "WarehousesQuery",
    "WarehousesResponse",
    "WarehousesResponseData",
    "WarehousesResponseDataItemsItem",
    "WarehousesResponseDataPager",
    "WarehousesResponseDataSortData",
]
