"""Digikala auth: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListScopesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ListScopesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListScopesResponseDataItemsItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    access: str | None = Field(default=None)


class GetClientScopesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class GetClientScopesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class GetClientScopesResponseDataItemsItem(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)
    description: str | None = Field(default=None)
    access: str | None = Field(default=None)


class RevokeResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class ListScopesResponseData(APIResponseSchema):
    sort_data: ListScopesResponseDataSortData | None = Field(default=None)
    pager: ListScopesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListScopesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetClientScopesResponseData(APIResponseSchema):
    sort_data: GetClientScopesResponseDataSortData | None = Field(default=None)
    pager: GetClientScopesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetClientScopesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class RevokeResponse(APIResponseSchema):
    status: str
    data: RevokeResponseData


class ListScopesResponse(APIResponseSchema):
    status: str
    data: ListScopesResponseData


class GetClientScopesResponse(APIResponseSchema):
    status: str
    data: GetClientScopesResponseData


__all__ = [
    "GetClientScopesResponse",
    "GetClientScopesResponseData",
    "GetClientScopesResponseDataItemsItem",
    "GetClientScopesResponseDataPager",
    "GetClientScopesResponseDataSortData",
    "ListScopesResponse",
    "ListScopesResponseData",
    "ListScopesResponseDataItemsItem",
    "ListScopesResponseDataPager",
    "ListScopesResponseDataSortData",
    "RevokeResponse",
    "RevokeResponseData",
]
