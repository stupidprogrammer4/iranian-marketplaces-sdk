"""Digikala invoices: request and response models."""

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
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_payout_order_status: int | None = Field(
        default=None,
        validation_alias="search[payout_order_status]",
        serialization_alias="search[payout_order_status]",
    )
    search_invoice_start_date: str | None = Field(
        default=None,
        validation_alias="search[invoice_start_date]",
        serialization_alias="search[invoice_start_date]",
    )
    search_invoice_end_date: str | None = Field(
        default=None,
        validation_alias="search[invoice_end_date]",
        serialization_alias="search[invoice_end_date]",
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


class ListResponseDataItemsItemPayoutOrderStatus(APIResponseSchema):
    title: str | None = Field(default=None)
    key: str | None = Field(default=None)


class ListResponseDataItemsItemSettlementStatus(APIResponseSchema):
    title: str | None = Field(default=None)
    key: str | None = Field(default=None)


class ListResponseDataMetaData(APIResponseSchema):
    last_updated_at: str | None = Field(default=None)


class DetailsResponseDataCashStatus(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class DetailsResponseDataCredit(APIResponseSchema):
    maturity_date: str | None = Field(default=None)
    total_amount: int | None = Field(default=None)
    status: DetailsResponseDataCashStatus | None = Field(default=None)


class DetailsResponseDataEarlySettlement(APIResponseSchema):
    status: str | None = Field(default=None)
    amount: int | str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    settlement_date: str | None = Field(default=None)


class DetailsResponseDataSalesNotationsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    item_count: int | None = Field(default=None)
    total_amount: int | None = Field(default=None)
    general_discount_credit: int | None = Field(default=None)
    general_discount_debit: int | None = Field(default=None)
    calculation_model_type: str | None = Field(default=None)
    is_vat_free: bool | None = Field(default=None)


class DetailsResponseDataSalesReturn(APIResponseSchema):
    notations: list[DetailsResponseDataSalesNotationsItem] | None = Field(default=None)
    total_amount: int | None = Field(default=None)


class DetailsResponseDataOthers(APIResponseSchema):
    notations: list[DetailsResponseDataSalesNotationsItem] | None = Field(default=None)
    total_amount: int | None = Field(default=None)


class DetailsResponseDataPaymentDeficit(APIResponseSchema):
    sales_amount: float | int | None = Field(default=None)
    sales_return_amount: float | int | None = Field(default=None)
    others_amount: float | int | None = Field(default=None)
    total_amount: float | int | None = Field(default=None)


class ItemsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_invoice_id: int | None = Field(
        default=None,
        validation_alias="search[invoice_id]",
        serialization_alias="search[invoice_id]",
    )
    search_financial_notation_id: int | None = Field(
        default=None,
        validation_alias="search[financial_notation_id]",
        serialization_alias="search[financial_notation_id]",
    )
    search_calculation_type: str | None = Field(
        default=None,
        validation_alias="search[calculation_type]",
        serialization_alias="search[calculation_type]",
    )


class ItemsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ItemsResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ItemsResponseDataItemsItem0PayMethod(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class ItemsResponseDataItemsItem1(APIResponseSchema):
    id: int | None = Field(default=None)
    event_datetime: int | None = Field(default=None)
    credit: float | None = Field(default=None)
    debit: float | None = Field(default=None)
    general_discount_credit: float | None = Field(default=None)
    general_discount_debit: float | None = Field(default=None)
    final_credit: float | None = Field(default=None)
    final_debit: float | None = Field(default=None)
    description: str | None = Field(default=None)
    calculation_model_type: str | None = Field(default=None)


class SubmitVatRequest(RequestSchema):
    product_id: int
    date: str
    price: int
    is_vat_included_in_price: bool


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    cash_sale_date: str | None = Field(default=None)
    credit_sale_date: str | None = Field(default=None)
    invoice_total_amount: int | None = Field(default=None)
    payout_order_status: ListResponseDataItemsItemPayoutOrderStatus | None = Field(default=None)
    settlement_status: ListResponseDataItemsItemSettlementStatus | None = Field(default=None)
    show_early_settlement: bool | None = Field(default=None)
    can_print: bool | None = Field(default=None)
    is_new: bool | None = Field(default=None)


class DetailsResponseDataCash(APIResponseSchema):
    maturity_date: str | None = Field(default=None)
    total_amount: int | None = Field(default=None)
    status: DetailsResponseDataCashStatus | None = Field(default=None)


class DetailsResponseDataSales(APIResponseSchema):
    notations: list[DetailsResponseDataSalesNotationsItem] | None = Field(default=None)
    total_amount: int | None = Field(default=None)


class ItemsResponseDataItemsItem0(APIResponseSchema):
    id: int | None = Field(default=None)
    event_datetime: int | None = Field(default=None)
    varinat_code: int | None = Field(default=None)
    varinat_title: str | None = Field(default=None)
    order_id: int | None = Field(default=None)
    item_serial: str | None = Field(default=None)
    credit: float | None = Field(default=None)
    debit: float | None = Field(default=None)
    general_discount_credit: float | None = Field(default=None)
    general_discount_debit: float | None = Field(default=None)
    final_credit: float | None = Field(default=None)
    final_debit: float | None = Field(default=None)
    description: str | None = Field(default=None)
    calculation_model_type: str | None = Field(default=None)
    pay_method: ItemsResponseDataItemsItem0PayMethod | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ListResponseDataMetaData | None = Field(default=None)


class DetailsResponseData(APIResponseSchema):
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    show_early_settlement: bool | None = Field(default=None)
    vat_amount: float | int | None = Field(default=None)
    show_income_factor: bool | None = Field(default=None)
    can_print: bool | None = Field(default=None)
    cash: DetailsResponseDataCash | None = Field(default=None)
    credit: DetailsResponseDataCredit | None = Field(default=None)
    total_income: float | int | None = Field(default=None)
    total_paid_amount: int | None = Field(default=None)
    payout_order_status: ListResponseDataItemsItemPayoutOrderStatus | None = Field(default=None)
    early_settlement: DetailsResponseDataEarlySettlement | None = Field(default=None)
    sales: DetailsResponseDataSales | None = Field(default=None)
    sales_return: DetailsResponseDataSalesReturn | None = Field(default=None)
    others: DetailsResponseDataOthers | None = Field(default=None)
    payment_deficit: DetailsResponseDataPaymentDeficit | None = Field(default=None)


class ItemsResponseData(APIResponseSchema):
    sort_data: ItemsResponseDataSortData | None = Field(default=None)
    pager: ItemsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ItemsResponseDataItemsItem0 | ItemsResponseDataItemsItem1] | None = Field(
        default=None
    )
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class DetailsResponse(APIResponseSchema):
    status: int | str
    data: DetailsResponseData


class ItemsResponse(APIResponseSchema):
    status: str
    data: ItemsResponseData


__all__ = [
    "DetailsResponse",
    "DetailsResponseData",
    "DetailsResponseDataCash",
    "DetailsResponseDataCashStatus",
    "DetailsResponseDataCredit",
    "DetailsResponseDataEarlySettlement",
    "DetailsResponseDataOthers",
    "DetailsResponseDataPaymentDeficit",
    "DetailsResponseDataSales",
    "DetailsResponseDataSalesNotationsItem",
    "DetailsResponseDataSalesReturn",
    "ItemsQuery",
    "ItemsResponse",
    "ItemsResponseData",
    "ItemsResponseDataItemsItem0",
    "ItemsResponseDataItemsItem0PayMethod",
    "ItemsResponseDataItemsItem1",
    "ItemsResponseDataPager",
    "ItemsResponseDataSortData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemPayoutOrderStatus",
    "ListResponseDataItemsItemSettlementStatus",
    "ListResponseDataMetaData",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "SubmitVatRequest",
]
