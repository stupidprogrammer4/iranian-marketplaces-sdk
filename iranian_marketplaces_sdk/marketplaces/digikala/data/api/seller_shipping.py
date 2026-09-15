"""Digikala seller shipping: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class CreateRequestFreeShipping(RequestSchema):
    cost: int | None = Field(default=None)
    active: bool | None = Field(default=None)


class CreateRequestTimeScopesItem(RequestSchema):
    id: int | None = Field(default=None)
    active: bool | None = Field(default=None)
    capacity: int | None = Field(default=None)


class CreateRequestCoveragesItem(RequestSchema):
    id: int | None = Field(default=None)
    cost: int | None = Field(default=None)
    polygon_ids: list[int] | None = Field(default=None)


class CreateResponseDataFreeShipping(APIResponseSchema):
    active: str | None = Field(default=None)
    cost: int | None = Field(default=None)


class CreateResponseDataNature(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class CreateResponseDataDynamicTimeScopeSlotsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    starts_at: int | None = Field(default=None)
    ends_at: int | None = Field(default=None)
    active: bool | None = Field(default=None)
    capacity: int | None = Field(default=None)


class CreateResponseDataPic(APIResponseSchema):
    name: str | None = Field(default=None)
    phone: str | None = Field(default=None)


class CreateResponseDataCoveragesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    cost: int | None = Field(default=None)
    polygon_ids: list[int] | None = Field(default=None)


class CreateResponseDataWarehouseInfo(APIResponseSchema):
    warehouse_id: int | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)
    address: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ListQuery(QuerySchema):
    search_status: Literal["inactive", "active", "draft"] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_search_term: str | None = Field(
        default=None,
        validation_alias="search[search_term]",
        serialization_alias="search[search_term]",
    )
    search_nature_id: Literal[1, 2, 3] | None = Field(
        default=None, validation_alias="search[nature_id]", serialization_alias="search[nature_id]"
    )
    search_type: Literal["self_shipping", "partner_shipping"] = Field(
        validation_alias="search[type]", serialization_alias="search[type]"
    )
    search_ids: list[int] | None = Field(
        default=None, validation_alias="search[ids]", serialization_alias="search[ids]"
    )
    size: int | None = Field(default=None)
    page: int | None = Field(default=None)


class ListResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ListResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class UpdateRequest(RequestSchema):
    name: str | None = Field(default=None)
    cost: int | None = Field(default=None)
    free_shipping: CreateRequestFreeShipping | None = Field(default=None)
    nature_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    dynamic_time_scope_id: int | None = Field(default=None)
    time_distance: int | None = Field(default=None)
    first_mile_delivery_time: int | None = Field(default=None)
    cities: list[int] | None = Field(default=None)
    time_scopes: list[CreateRequestTimeScopesItem] | None = Field(default=None)
    coverages: list[CreateRequestCoveragesItem] | None = Field(default=None)
    warehouse_id: int | None = Field(default=None)
    pic_name: str | None = Field(default=None)
    pic_phone: str | None = Field(default=None)
    auto_approve_pending_orders: bool | None = Field(default=None)


class StatesQuery(QuerySchema):
    search_setting_id: int | None = Field(
        default=None,
        validation_alias="search[setting_id]",
        serialization_alias="search[setting_id]",
    )
    search_nature_id: Literal[1, 2, 3] = Field(
        validation_alias="search[nature_id]", serialization_alias="search[nature_id]"
    )
    search_active: Literal[0, 1] | None = Field(
        default=None, validation_alias="search[active]", serialization_alias="search[active]"
    )
    search_text: str | None = Field(
        default=None, validation_alias="search[text]", serialization_alias="search[text]"
    )
    size: int | None = Field(default=None)
    page: int | None = Field(default=None)


class StatesResponseDataItemsItemHasWarehouseItemCitiesItem(APIResponseSchema):
    state_id: int | None = Field(default=None)
    city_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    selected: bool | None = Field(default=None)
    exist_in_other_settings: bool | None = Field(default=None)


class TimeScopesQuery(QuerySchema):
    search_type: Literal["self_shipping", "partner_shipping", "nearby_shipping"] | None = Field(
        default=None, validation_alias="search[type]", serialization_alias="search[type]"
    )
    size: int | None = Field(default=None)
    page: int | None = Field(default=None)


class TimeScopesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    period: int | None = Field(default=None)
    start: int | None = Field(default=None)
    end: int | None = Field(default=None)
    title: str | None = Field(default=None)
    slots: list[CreateResponseDataDynamicTimeScopeSlotsItem] | None = Field(default=None)


class DeactivateCitiesRequest(RequestSchema):
    city_ids: list[int]
    nature_id: int


class CreateRequest(RequestSchema):
    type: str
    name: str | None = Field(default=None)
    cost: int | None = Field(default=None)
    free_shipping: CreateRequestFreeShipping | None = Field(default=None)
    nature_id: int
    status: str | None = Field(default=None)
    dynamic_time_scope_id: int | None = Field(default=None)
    time_distance: int | None = Field(default=None)
    first_mile_delivery_time: int | None = Field(default=None)
    cities: list[int] | None = Field(default=None)
    time_scopes: list[CreateRequestTimeScopesItem] | None = Field(default=None)
    coverages: list[CreateRequestCoveragesItem] | None = Field(default=None)
    warehouse_id: int | None = Field(default=None)
    pic_name: str | None = Field(default=None)
    pic_phone: str | None = Field(default=None)
    auto_approve_pending_orders: bool | None = Field(default=None)


class CreateResponseDataDynamicTimeScope(APIResponseSchema):
    id: int | None = Field(default=None)
    period: int | None = Field(default=None)
    start: int | None = Field(default=None)
    end: int | None = Field(default=None)
    title: str | None = Field(default=None)
    slots: list[CreateResponseDataDynamicTimeScopeSlotsItem] | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    cities_count: int | None = Field(default=None)
    time_distance: int | None = Field(default=None)
    first_mile_delivery_time: int | None = Field(default=None)
    cost: int | None = Field(default=None)
    time_scope: str | None = Field(default=None)
    total_capacity: int | None = Field(default=None)
    free_shipping: CreateResponseDataFreeShipping | None = Field(default=None)
    nature: CreateResponseDataNature | None = Field(default=None)
    dynamic_time_scope: CreateResponseDataDynamicTimeScope | None = Field(default=None)
    pic: CreateResponseDataPic | None = Field(default=None)
    auto_approve_pending_orders: bool | None = Field(default=None)
    coverages: list[CreateResponseDataCoveragesItem] | None = Field(default=None)
    warehouse_info: CreateResponseDataWarehouseInfo | None = Field(default=None)


class StatesResponseDataItemsItemHasWarehouseItem(APIResponseSchema):
    state_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    cities_count: int | None = Field(default=None)
    selected_cities_count: int | None = Field(default=None)
    selected_in_setting_cities_count: int | None = Field(default=None)
    disabled: bool | None = Field(default=None)
    cities: list[StatesResponseDataItemsItemHasWarehouseItemCitiesItem] | None = Field(default=None)


class TimeScopesResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TimeScopesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CreateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    type: str | None = Field(default=None)
    name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    cities_count: int | None = Field(default=None)
    time_distance: int | None = Field(default=None)
    first_mile_delivery_time: int | None = Field(default=None)
    cost: int | None = Field(default=None)
    time_scope: str | None = Field(default=None)
    total_capacity: int | None = Field(default=None)
    free_shipping: CreateResponseDataFreeShipping | None = Field(default=None)
    nature: CreateResponseDataNature | None = Field(default=None)
    dynamic_time_scope: CreateResponseDataDynamicTimeScope | None = Field(default=None)
    pic: CreateResponseDataPic | None = Field(default=None)
    auto_approve_pending_orders: bool | None = Field(default=None)
    coverages: list[CreateResponseDataCoveragesItem] | None = Field(default=None)
    warehouse_info: CreateResponseDataWarehouseInfo | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[CreateResponseData] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class UpdateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class StatesResponseDataItemsItem(APIResponseSchema):
    has_warehouse: list[StatesResponseDataItemsItemHasWarehouseItem] | None = Field(default=None)
    around_warehouse: list[StatesResponseDataItemsItemHasWarehouseItem] | None = Field(default=None)
    other: list[StatesResponseDataItemsItemHasWarehouseItem] | None = Field(default=None)


class TimeScopesResponse(APIResponseSchema):
    status: str
    data: TimeScopesResponseData


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class StatesResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[StatesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class StatesResponse(APIResponseSchema):
    status: str
    data: StatesResponseData


__all__ = [
    "CreateRequest",
    "CreateRequestCoveragesItem",
    "CreateRequestFreeShipping",
    "CreateRequestTimeScopesItem",
    "CreateResponse",
    "CreateResponseData",
    "CreateResponseDataCoveragesItem",
    "CreateResponseDataDynamicTimeScope",
    "CreateResponseDataDynamicTimeScopeSlotsItem",
    "CreateResponseDataFreeShipping",
    "CreateResponseDataNature",
    "CreateResponseDataPic",
    "CreateResponseDataWarehouseInfo",
    "DeactivateCitiesRequest",
    "GetResponse",
    "GetResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "StatesQuery",
    "StatesResponse",
    "StatesResponseData",
    "StatesResponseDataItemsItem",
    "StatesResponseDataItemsItemHasWarehouseItem",
    "StatesResponseDataItemsItemHasWarehouseItemCitiesItem",
    "TimeScopesQuery",
    "TimeScopesResponse",
    "TimeScopesResponseData",
    "TimeScopesResponseDataItemsItem",
    "UpdateRequest",
    "UpdateResponse",
]
