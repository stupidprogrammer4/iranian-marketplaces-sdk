"""Digikala finance: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class OverviewQuery(QuerySchema):
    start_date: str
    end_date: str


class OverviewResponseDataPeriod(APIResponseSchema):
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)


class OverviewResponseDataSalesItemsItemBadge(APIResponseSchema):
    type: str | None = Field(default=None)
    title: str | None = Field(default=None)


class OverviewResponseDataChartCreditItemsItemNotationsItem(APIResponseSchema):
    notation_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    count: int | None = Field(default=None)
    discount_amount: int | None = Field(default=None)
    vat_free: bool | None = Field(default=None)


class TransactionsQuery(QuerySchema):
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_aggregation_type: list[str] | None = Field(
        default=None,
        validation_alias="search[aggregation_type]",
        serialization_alias="search[aggregation_type]",
    )
    search_search: str | None = Field(
        default=None, validation_alias="search[search]", serialization_alias="search[search]"
    )
    search_start_date: str | None = Field(
        default=None,
        validation_alias="search[start_date]",
        serialization_alias="search[start_date]",
    )
    search_end_date: str | None = Field(
        default=None, validation_alias="search[end_date]", serialization_alias="search[end_date]"
    )


class TransactionsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class TransactionsResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class TransactionsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    unique_identifier: int | None = Field(default=None)
    unique_identifier_tag: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    direction: str | None = Field(default=None)
    discount_sum: int | None = Field(default=None)
    aggregation_type: str | None = Field(default=None)
    detail_page: str | None = Field(default=None)
    category_label: str | None = Field(default=None)
    status: str | None = Field(default=None)
    transaction_time: str | None = Field(default=None)
    settlement_time: str | None = Field(default=None)
    payout_transaction_id: int | None = Field(default=None)
    is_correction: bool | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_title: str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    serial: str | None = Field(default=None)
    order_shipment_id: str | None = Field(default=None)


class TransactionsResponseDataMetaDataStatusesItem(APIResponseSchema):
    value: str | None = Field(default=None)
    label: str | None = Field(default=None)


class TransactionRowsQuery(QuerySchema):
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_notations: list[str] | None = Field(
        default=None, validation_alias="search[notations]", serialization_alias="search[notations]"
    )
    search_search: str | None = Field(
        default=None, validation_alias="search[search]", serialization_alias="search[search]"
    )
    search_start_date: str | None = Field(
        default=None,
        validation_alias="search[start_date]",
        serialization_alias="search[start_date]",
    )
    search_end_date: str | None = Field(
        default=None, validation_alias="search[end_date]", serialization_alias="search[end_date]"
    )


class TransactionRowsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    unique_identifier: int | None = Field(default=None)
    unique_identifier_tag: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    direction: str | None = Field(default=None)
    notation_id: int | None = Field(default=None)
    notation_name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    transaction_time: str | None = Field(default=None)
    settlement_time: str | None = Field(default=None)
    payout_order_id: int | None = Field(default=None)
    is_correction: bool | None = Field(default=None)
    vat: int | None = Field(default=None)
    description: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_title: str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    serial: str | None = Field(default=None)
    order_shipment_id: str | None = Field(default=None)


class TransactionRowsResponseDataMetaData(APIResponseSchema):
    statuses: list[TransactionsResponseDataMetaDataStatusesItem] | None = Field(default=None)
    notations: ObjectMap[str] | None = Field(default=None)


class TransactionSummaryResponseDataTotal(APIResponseSchema):
    amount: int | None = Field(default=None)
    count: int | None = Field(default=None)


class TransactionSummaryResponseDataPayoutCycle(APIResponseSchema):
    days: int | None = Field(default=None)
    title: str | None = Field(default=None)


class GetTransactionResponseDataMetaData(APIResponseSchema):
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_title: str | None = Field(default=None)
    product_image_url: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    serial: str | None = Field(default=None)
    order_shipment_id: str | None = Field(default=None)


class GetTransactionResponseDataFinancialDetailsItem(APIResponseSchema):
    billing_event_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    debit: int | None = Field(default=None)
    credit: int | None = Field(default=None)
    notation_name: str | None = Field(default=None)
    description: str | None = Field(default=None)


class PayoutsQuery(QuerySchema):
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )


class PayoutsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class PayoutsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    amount: int | None = Field(default=None)
    status: str | None = Field(default=None)
    tracking_code: str | None = Field(default=None)
    suggested_payout_at: str | None = Field(default=None)
    payout_date: str | None = Field(default=None)


class PayoutsResponseDataMetaData(APIResponseSchema):
    statuses: list[TransactionsResponseDataMetaDataStatusesItem] | None = Field(default=None)


class GetPayoutResponseDataVat(APIResponseSchema):
    amount: int | None = Field(default=None)
    is_credit: bool | None = Field(default=None)


class GetPayoutResponseDataNotationsItem(APIResponseSchema):
    notation_id: int | None = Field(default=None)
    notation_name: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    is_credit: bool | None = Field(default=None)


class GetPayoutResponseDataEarlySettlementsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    tracking_code: str | None = Field(default=None)


class SellerInvoicesQuery(QuerySchema):
    search_month: int | None = Field(
        default=None, validation_alias="search[month]", serialization_alias="search[month]"
    )
    search_year: int | None = Field(
        default=None, validation_alias="search[year]", serialization_alias="search[year]"
    )
    search_invoice_id: int | None = Field(
        default=None,
        validation_alias="search[invoice_id]",
        serialization_alias="search[invoice_id]",
    )


class SellerInvoicesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class SellerInvoicesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class SellerInvoicesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    final_amount: int | None = Field(default=None)
    amount_type: str | None = Field(default=None)
    tax_id: str | None = Field(default=None)


class ExportTransactionsQuery(QuerySchema):
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)


class ExportTransactionsRequest(RequestSchema):
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)


class OverviewResponseDataSalesItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    items_count: int | None = Field(default=None)
    amount: int | None = Field(default=None)
    badge: OverviewResponseDataSalesItemsItemBadge | None = Field(default=None)


class OverviewResponseDataChartCreditItemsItem(APIResponseSchema):
    chart_group: str | None = Field(default=None)
    title: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    count: int | None = Field(default=None)
    discount_amount: int | None = Field(default=None)
    vat_free: bool | None = Field(default=None)
    notations: list[OverviewResponseDataChartCreditItemsItemNotationsItem] | None = Field(
        default=None
    )


class TransactionsResponseDataMetaData(APIResponseSchema):
    statuses: list[TransactionsResponseDataMetaDataStatusesItem] | None = Field(default=None)
    aggregation_types: list[TransactionsResponseDataMetaDataStatusesItem] | None = Field(
        default=None
    )


class TransactionRowsResponseData(APIResponseSchema):
    sort_data: TransactionsResponseDataSortData | None = Field(default=None)
    pager: TransactionsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TransactionRowsResponseDataItemsItem] | None = Field(default=None)
    meta_data: TransactionRowsResponseDataMetaData | None = Field(default=None)


class TransactionSummaryResponseData(APIResponseSchema):
    total: TransactionSummaryResponseDataTotal | None = Field(default=None)
    pending: TransactionSummaryResponseDataTotal | None = Field(default=None)
    accepted: TransactionSummaryResponseDataTotal | None = Field(default=None)
    released: TransactionSummaryResponseDataTotal | None = Field(default=None)
    paid: TransactionSummaryResponseDataTotal | None = Field(default=None)
    next_settlement_date: str | None = Field(default=None)
    payout_cycle: TransactionSummaryResponseDataPayoutCycle | None = Field(default=None)
    show_early_settlement: bool | None = Field(default=None)
    show_reserve_early_settlement: bool | None = Field(default=None)
    hover_content_key: str | None = Field(default=None)


class GetTransactionResponseData(APIResponseSchema):
    aggregation_type: str | None = Field(default=None)
    category_label: str | None = Field(default=None)
    unique_identifier: str | None = Field(default=None)
    unique_identifier_tag: str | None = Field(default=None)
    has_variant_info: bool | None = Field(default=None)
    status: str | None = Field(default=None)
    transaction_id: int | None = Field(default=None)
    transaction_time: str | None = Field(default=None)
    final_amount: int | None = Field(default=None)
    amount_type: str | None = Field(default=None)
    vat_sum: int | None = Field(default=None)
    discount_sum: int | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    billing_event_count: int | None = Field(default=None)
    payout_order_tracking_code: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    meta_data: GetTransactionResponseDataMetaData | None = Field(default=None)
    financial_details: list[GetTransactionResponseDataFinancialDetailsItem] | None = Field(
        default=None
    )


class PayoutsResponseData(APIResponseSchema):
    sort_data: PayoutsResponseDataSortData | None = Field(default=None)
    pager: TransactionsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[PayoutsResponseDataItemsItem] | None = Field(default=None)
    meta_data: PayoutsResponseDataMetaData | None = Field(default=None)


class GetPayoutResponseData(APIResponseSchema):
    payout_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    amount: int | None = Field(default=None)
    tracking_code: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    suggested_payout_at: str | None = Field(default=None)
    payout_date: str | None = Field(default=None)
    billing_event_count: int | None = Field(default=None)
    vat: GetPayoutResponseDataVat | None = Field(default=None)
    notations: list[GetPayoutResponseDataNotationsItem] | None = Field(default=None)
    early_settlements: list[GetPayoutResponseDataEarlySettlementsItem] | None = Field(default=None)


class SellerInvoicesResponseData(APIResponseSchema):
    sort_data: SellerInvoicesResponseDataSortData | None = Field(default=None)
    pager: SellerInvoicesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SellerInvoicesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class OverviewResponseDataSales(APIResponseSchema):
    title: str | None = Field(default=None)
    total_amount: int | None = Field(default=None)
    items: list[OverviewResponseDataSalesItemsItem] | None = Field(default=None)


class OverviewResponseDataChartCredit(APIResponseSchema):
    total: int | None = Field(default=None)
    items: list[OverviewResponseDataChartCreditItemsItem] | None = Field(default=None)


class TransactionsResponseData(APIResponseSchema):
    sort_data: TransactionsResponseDataSortData | None = Field(default=None)
    pager: TransactionsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TransactionsResponseDataItemsItem] | None = Field(default=None)
    meta_data: TransactionsResponseDataMetaData | None = Field(default=None)


class TransactionRowsResponse(APIResponseSchema):
    status: str
    data: TransactionRowsResponseData


class TransactionSummaryResponse(APIResponseSchema):
    status: int | str
    data: TransactionSummaryResponseData


class GetTransactionResponse(APIResponseSchema):
    status: int | str
    data: GetTransactionResponseData


class PayoutsResponse(APIResponseSchema):
    status: str
    data: PayoutsResponseData


class GetPayoutResponse(APIResponseSchema):
    status: int | str
    data: GetPayoutResponseData


class SellerInvoicesResponse(APIResponseSchema):
    status: str
    data: SellerInvoicesResponseData


class OverviewResponseDataChart(APIResponseSchema):
    credit: OverviewResponseDataChartCredit | None = Field(default=None)
    debit: OverviewResponseDataChartCredit | None = Field(default=None)


class TransactionsResponse(APIResponseSchema):
    status: str
    data: TransactionsResponseData


class OverviewResponseData(APIResponseSchema):
    period: OverviewResponseDataPeriod | None = Field(default=None)
    sales: OverviewResponseDataSales | None = Field(default=None)
    sales_returns: OverviewResponseDataSales | None = Field(default=None)
    chart: OverviewResponseDataChart | None = Field(default=None)


class OverviewResponse(APIResponseSchema):
    status: int | str
    data: OverviewResponseData


__all__ = [
    "ExportTransactionsQuery",
    "ExportTransactionsRequest",
    "GetPayoutResponse",
    "GetPayoutResponseData",
    "GetPayoutResponseDataEarlySettlementsItem",
    "GetPayoutResponseDataNotationsItem",
    "GetPayoutResponseDataVat",
    "GetTransactionResponse",
    "GetTransactionResponseData",
    "GetTransactionResponseDataFinancialDetailsItem",
    "GetTransactionResponseDataMetaData",
    "OverviewQuery",
    "OverviewResponse",
    "OverviewResponseData",
    "OverviewResponseDataChart",
    "OverviewResponseDataChartCredit",
    "OverviewResponseDataChartCreditItemsItem",
    "OverviewResponseDataChartCreditItemsItemNotationsItem",
    "OverviewResponseDataPeriod",
    "OverviewResponseDataSales",
    "OverviewResponseDataSalesItemsItem",
    "OverviewResponseDataSalesItemsItemBadge",
    "PayoutsQuery",
    "PayoutsResponse",
    "PayoutsResponseData",
    "PayoutsResponseDataItemsItem",
    "PayoutsResponseDataMetaData",
    "PayoutsResponseDataSortData",
    "SellerInvoicesQuery",
    "SellerInvoicesResponse",
    "SellerInvoicesResponseData",
    "SellerInvoicesResponseDataItemsItem",
    "SellerInvoicesResponseDataPager",
    "SellerInvoicesResponseDataSortData",
    "TransactionRowsQuery",
    "TransactionRowsResponse",
    "TransactionRowsResponseData",
    "TransactionRowsResponseDataItemsItem",
    "TransactionRowsResponseDataMetaData",
    "TransactionSummaryResponse",
    "TransactionSummaryResponseData",
    "TransactionSummaryResponseDataPayoutCycle",
    "TransactionSummaryResponseDataTotal",
    "TransactionsQuery",
    "TransactionsResponse",
    "TransactionsResponseData",
    "TransactionsResponseDataItemsItem",
    "TransactionsResponseDataMetaData",
    "TransactionsResponseDataMetaDataStatusesItem",
    "TransactionsResponseDataPager",
    "TransactionsResponseDataSortData",
]
