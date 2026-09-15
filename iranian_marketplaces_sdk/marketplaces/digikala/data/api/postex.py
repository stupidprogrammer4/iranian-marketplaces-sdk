"""Digikala postex: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class CreateUserRequest(RequestSchema):
    first_name: str
    last_name: str
    birth_certificate_serial: str
    birth_certificate_series: str
    birth_certificate_issued_city_id: int
    birth_date: str
    gender: str
    national_identity_number: str
    national_identity_series: str
    warehouse_id: int
    register_phone: str
    store_name: str
    store_category_name: str
    store_phone: str


class ChargeWalletRequest(RequestSchema):
    amount: int
    order_id: int | None = Field(default=None)
    order_shipment_ids: list[JsonValue] | None = Field(default=None)
    callback_url: str | None = Field(default=None)


class TransactionsQuery(QuerySchema):
    type: str | None = Field(default=None)
    from_date: str | None = Field(default=None)
    to_date: str | None = Field(default=None)


class TransactionsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class TransactionsResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class CalculatePriceRequest(RequestSchema):
    shipment_id: int
    registration_method: str | list[JsonValue]
    warehouse_id: int
    added_services: list[JsonValue]
    ready_date_time: str
    parcel: list[JsonValue] | None = Field(default=None)


class TransactionsResponseData(APIResponseSchema):
    sort_data: TransactionsResponseDataSortData | None = Field(default=None)
    pager: TransactionsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ObjectMap[JsonValue]] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class TransactionsResponse(APIResponseSchema):
    status: str
    data: TransactionsResponseData


__all__ = [
    "CalculatePriceRequest",
    "ChargeWalletRequest",
    "CreateUserRequest",
    "TransactionsQuery",
    "TransactionsResponse",
    "TransactionsResponseData",
    "TransactionsResponseDataPager",
    "TransactionsResponseDataSortData",
]
