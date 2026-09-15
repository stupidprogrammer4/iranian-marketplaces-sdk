"""Digikala themes: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListValuesQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    brand_id: int | None = Field(default=None)


class ListValuesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ListValuesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListValuesResponseDataItemsItemValue(APIResponseSchema):
    hex: str | None = Field(default=None)
    rgb: str | None = Field(default=None)
    value: str | None = Field(default=None)


class ListValuesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title_fa: str | None = Field(
        default=None, validation_alias="titleFa", serialization_alias="titleFa"
    )
    title_en: str | None = Field(
        default=None, validation_alias="titleEn", serialization_alias="titleEn"
    )
    value: ListValuesResponseDataItemsItemValue | None = Field(default=None)
    nature: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    standard_unit_id: int | None = Field(
        default=None, validation_alias="standardUnitID", serialization_alias="standardUnitID"
    )
    color_pallate_ids: list[int] | None = Field(
        default=None, validation_alias="colorPallateIDs", serialization_alias="colorPallateIDs"
    )
    extra_data: list[ObjectMap[JsonValue]] | None = Field(
        default=None, validation_alias="extraData", serialization_alias="extraData"
    )


class ListValuesResponseData(APIResponseSchema):
    sort_data: ListValuesResponseDataSortData | None = Field(default=None)
    pager: ListValuesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListValuesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListValuesResponse(APIResponseSchema):
    status: str
    data: ListValuesResponseData


__all__ = [
    "ListValuesQuery",
    "ListValuesResponse",
    "ListValuesResponseData",
    "ListValuesResponseDataItemsItem",
    "ListValuesResponseDataItemsItemValue",
    "ListValuesResponseDataPager",
    "ListValuesResponseDataSortData",
]
