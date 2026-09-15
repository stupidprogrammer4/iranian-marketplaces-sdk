"""Digikala questions: request and response models."""

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
    sort: (
        Literal[
            "id", "most_viewed", "best_selling", "newest_product", "most-answers", "least-answers"
        ]
        | None
    ) = Field(default=None)
    order: str | None = Field(default=None)
    search_answer_status: list[str] | None = Field(
        default=None,
        validation_alias="search[answer-status]",
        serialization_alias="search[answer-status]",
    )
    search_question_date_from: str | None = Field(
        default=None,
        validation_alias="search[question-date-from]",
        serialization_alias="search[question-date-from]",
    )
    search_question_date_to: str | None = Field(
        default=None,
        validation_alias="search[question-date-to]",
        serialization_alias="search[question-date-to]",
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


class ListResponseDataItemsItemAnswerStatus(APIResponseSchema):
    title: str | None = Field(default=None)
    key: str | None = Field(default=None)


class ListResponseDataItemsItemProduct(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    link: str | None = Field(default=None)
    photo: str | None = Field(default=None)


class GetResponseDataProduct(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    link: str | None = Field(default=None)
    photo: str | None = Field(default=None)


class AnswerRequest(RequestSchema):
    question_id: int
    answer: str
    file_ids: list[int] | None = Field(default=None)


class ListResponseDataItemsItemAnswer(APIResponseSchema):
    id: int | None = Field(default=None)
    body: str | None = Field(default=None)
    files: list[str] | None = Field(default=None)
    status: ListResponseDataItemsItemAnswerStatus | None = Field(default=None)
    date: str | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    body: str | None = Field(default=None)
    date: str | None = Field(default=None)
    answer: ListResponseDataItemsItemAnswer | None = Field(default=None)
    answer_count: int | None = Field(default=None)
    product: GetResponseDataProduct | None = Field(default=None)
    user: str | None = Field(default=None)


class AnswerResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    body: str | None = Field(default=None)
    date: str | None = Field(default=None)
    answer: ListResponseDataItemsItemAnswer | None = Field(default=None)
    answer_count: int | None = Field(default=None)
    product: ListResponseDataItemsItemProduct | None = Field(default=None)
    user: str | None = Field(default=None)


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


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
    "AnswerRequest",
    "AnswerResponse",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataProduct",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemAnswer",
    "ListResponseDataItemsItemAnswerStatus",
    "ListResponseDataItemsItemProduct",
    "ListResponseDataPager",
    "ListResponseDataSortData",
]
