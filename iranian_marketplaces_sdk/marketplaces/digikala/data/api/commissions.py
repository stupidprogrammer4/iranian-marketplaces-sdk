"""Digikala commissions: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_my_commissions: bool | None = Field(
        default=None,
        validation_alias="search[my_commissions]",
        serialization_alias="search[my_commissions]",
    )
    search_main_category_id: int | None = Field(
        default=None,
        validation_alias="search[main_category_id]",
        serialization_alias="search[main_category_id]",
    )
    search_category_id: int | None = Field(
        default=None,
        validation_alias="search[category_id]",
        serialization_alias="search[category_id]",
    )
    search_brand_id: int | None = Field(
        default=None, validation_alias="search[brand_id]", serialization_alias="search[brand_id]"
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
    main_category_id: int | None = Field(default=None)
    main_category_title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    category_title: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    brand_title: str | None = Field(default=None)
    commission: float | None = Field(default=None)
    current_lead_time: int | None = Field(
        default=None, validation_alias="currentLeadTime", serialization_alias="currentLeadTime"
    )
    extra_commission: float | None = Field(default=None)
    return_free_commission: float | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


__all__ = [
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataPager",
    "ListResponseDataSortData",
]
