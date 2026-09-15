"""Digikala search ads: request and response models."""

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
    sort: str | None = Field(default=None)
    order: str | None = Field(default=None)
    search_q: str | None = Field(
        default=None, validation_alias="search[q]", serialization_alias="search[q]"
    )
    search_status: str | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_start_date: str | None = Field(
        default=None,
        validation_alias="search[start_date]",
        serialization_alias="search[start_date]",
    )
    search_end_date: str | None = Field(
        default=None, validation_alias="search[end_date]", serialization_alias="search[end_date]"
    )


class ListResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ListResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListResponseDataItemsItemUsedBudget(APIResponseSchema):
    today: int | None = Field(default=None)
    total: int | None = Field(default=None)


class CreateRequestCampaign(RequestSchema):
    title: str
    product_ids: list[int] | None = Field(default=None)
    start_date: str
    end_date: str | None = Field(default=None)
    bid_amount: int
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    payment_method: str | None = Field(default=None)


class CreateResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    message: str | None = Field(default=None)


class GetResponseDataProductsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    active: bool | None = Field(default=None)
    dkp: int | None = Field(default=None)
    title: str | None = Field(default=None)
    image: str | None = Field(default=None)


class RecommendedProductsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["cr"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_q: str | None = Field(
        default=None, validation_alias="search[q]", serialization_alias="search[q]"
    )


class RecommendedProductsResponseDataItemsItemCategory(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class UpdateRequestCampaign(RequestSchema):
    title: str
    start_date: str
    end_date: str | None = Field(default=None)
    bid_amount: int
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    payment_method: str | None = Field(default=None)


class UpdateResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateStatusRequest(RequestSchema):
    status: str


class UpdateStatusResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    bid_amount: int | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    payment_method: str | None = Field(default=None)
    used_budget: ListResponseDataItemsItemUsedBudget | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)


class CreateRequest(RequestSchema):
    campaign: CreateRequestCampaign | None = Field(default=None)


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    bid_amount: int | None = Field(default=None)
    products: list[GetResponseDataProductsItem] | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    payment_method: str | None = Field(default=None)
    used_budget: ListResponseDataItemsItemUsedBudget | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)


class RecommendedProductsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    image: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    category: RecommendedProductsResponseDataItemsItemCategory | None = Field(default=None)


class UpdateRequest(RequestSchema):
    campaign: UpdateRequestCampaign | None = Field(default=None)


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class RecommendedProductsResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[RecommendedProductsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class RecommendedProductsResponse(APIResponseSchema):
    status: str
    data: RecommendedProductsResponseData


__all__ = [
    "CreateRequest",
    "CreateRequestCampaign",
    "CreateResponse",
    "CreateResponseData",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataProductsItem",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemUsedBudget",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "RecommendedProductsQuery",
    "RecommendedProductsResponse",
    "RecommendedProductsResponseData",
    "RecommendedProductsResponseDataItemsItem",
    "RecommendedProductsResponseDataItemsItemCategory",
    "UpdateRequest",
    "UpdateRequestCampaign",
    "UpdateResponse",
    "UpdateResponseData",
    "UpdateStatusRequest",
    "UpdateStatusResponse",
]
