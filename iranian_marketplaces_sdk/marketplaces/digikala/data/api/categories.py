"""Digikala categories: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class TreeQuery(QuerySchema):
    search_parent_id: int | None = Field(
        default=None, validation_alias="search[parent_id]", serialization_alias="search[parent_id]"
    )


class TreeResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class TreeResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class TreeResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class TreeResponseData(APIResponseSchema):
    sort_data: TreeResponseDataSortData | None = Field(default=None)
    pager: TreeResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TreeResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class TreeResponse(APIResponseSchema):
    status: str
    data: TreeResponseData


__all__ = [
    "TreeQuery",
    "TreeResponse",
    "TreeResponseData",
    "TreeResponseDataItemsItem",
    "TreeResponseDataPager",
    "TreeResponseDataSortData",
]
