"""Digikala shipments: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListQuery(QuerySchema):
    search_created_at_end: JsonValue = Field(
        default=None,
        validation_alias="search[created_at_end]",
        serialization_alias="search[created_at_end]",
    )
    search_shipment_receive_at_start: JsonValue = Field(
        default=None,
        validation_alias="search[shipment_receive_at_start]",
        serialization_alias="search[shipment_receive_at_start]",
    )
    search_shipment_receive_at_end: JsonValue = Field(
        default=None,
        validation_alias="search[shipment_receive_at_end]",
        serialization_alias="search[shipment_receive_at_end]",
    )
    search_shipment_status: (
        Literal["new", "received", "partially_received", "rejected", "error"] | None
    ) = Field(
        default=None,
        validation_alias="search[shipment_status]",
        serialization_alias="search[shipment_status]",
    )
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
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
    id: int | None = Field(default=None)
    shipment_number: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    pickup_warehouse_title: str | None = Field(default=None)
    pickup_date: str | None = Field(default=None)
    cost: int | None = Field(default=None)
    status: str | None = Field(default=None)
    total_volume: int | None = Field(default=None)
    total_weight: int | None = Field(default=None)
    min_distance: int | None = Field(default=None)
    can_delete: bool | None = Field(default=None)


class CreateRequest(RequestSchema):
    package_ids: list[int] | None = Field(default=None)
    warehouse_id: int | None = Field(default=None)
    pickup_date: str | None = Field(default=None)
    time_scope: str | None = Field(default=None)


class CreateResponseDataShipmentEntity(APIResponseSchema):
    number: str | None = Field(default=None)
    warehouse: str | None = Field(default=None)
    received_at_forecast_date: str | None = Field(default=None)
    time_scope: str | None = Field(default=None)


class PackagesQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    package_ids: list[int] | None = Field(default=None)
    search_warehouse_id: int | None = Field(
        default=None,
        validation_alias="search[warehouse_id]",
        serialization_alias="search[warehouse_id]",
    )


class PackagesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class PackagesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class PackagesResponseDataItemsItemShipmentType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class PackagesResponseDataItemsItemShippingNature(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class PackagesResponseDataMetaDataWarehouse(APIResponseSchema):
    time_scopes: list[str] | None = Field(default=None)


class GetResponseDataPackagesPackageIdType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class GetResponseDataPackagesPackageIdShippingNature(APIResponseSchema):
    shipping_nature_id: str | None = Field(default=None)


class GetResponseDataPackagesPackageIdStatus(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class GetResponseDataTimeScope(APIResponseSchema):
    start: int | None = Field(default=None)
    end: int | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CreateResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    shipment_entity: CreateResponseDataShipmentEntity | None = Field(default=None)


class PackagesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    package_number: str | None = Field(default=None)
    shipment_type: PackagesResponseDataItemsItemShipmentType | None = Field(default=None)
    shipping_nature: PackagesResponseDataItemsItemShippingNature | None = Field(default=None)
    created_at: str | None = Field(default=None)
    shipment_cost: int | None = Field(default=None)


class PackagesResponseDataMetaData(APIResponseSchema):
    warehouse: PackagesResponseDataMetaDataWarehouse | None = Field(default=None)


class GetResponseDataPackagesPackageId(APIResponseSchema):
    id: int | None = Field(default=None)
    package_number: str | None = Field(default=None)
    type: GetResponseDataPackagesPackageIdType | None = Field(default=None)
    shipping_nature: GetResponseDataPackagesPackageIdShippingNature | None = Field(default=None)
    create_date: str | None = Field(default=None)
    estimated_pickup_date: str | None = Field(default=None)
    status: GetResponseDataPackagesPackageIdStatus | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class PackagesResponseData(APIResponseSchema):
    sort_data: PackagesResponseDataSortData | None = Field(default=None)
    pager: PackagesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[PackagesResponseDataItemsItem] | None = Field(default=None)
    meta_data: PackagesResponseDataMetaData | None = Field(default=None)


class GetResponseDataPackages(APIResponseSchema):
    package_id: GetResponseDataPackagesPackageId | None = Field(default=None)


class PackagesResponse(APIResponseSchema):
    status: str
    data: PackagesResponseData


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    shipment_number: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    pickup_warehouse_title: str | None = Field(default=None)
    pickup_date: str | None = Field(default=None)
    cost: int | None = Field(default=None)
    status: str | None = Field(default=None)
    total_volume: int | None = Field(default=None)
    total_weight: int | None = Field(default=None)
    min_distance: int | None = Field(default=None)
    can_delete: bool | None = Field(default=None)
    packages: GetResponseDataPackages | None = Field(default=None)
    packages_count: int | None = Field(default=None)
    time_scope: GetResponseDataTimeScope | None = Field(default=None)


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


__all__ = [
    "CreateRequest",
    "CreateResponse",
    "CreateResponseData",
    "CreateResponseDataShipmentEntity",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataPackages",
    "GetResponseDataPackagesPackageId",
    "GetResponseDataPackagesPackageIdShippingNature",
    "GetResponseDataPackagesPackageIdStatus",
    "GetResponseDataPackagesPackageIdType",
    "GetResponseDataTimeScope",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "PackagesQuery",
    "PackagesResponse",
    "PackagesResponseData",
    "PackagesResponseDataItemsItem",
    "PackagesResponseDataItemsItemShipmentType",
    "PackagesResponseDataItemsItemShippingNature",
    "PackagesResponseDataMetaData",
    "PackagesResponseDataMetaDataWarehouse",
    "PackagesResponseDataPager",
    "PackagesResponseDataSortData",
]
