"""Digikala insight: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class OverviewQuery(QuerySchema):
    range: Literal["last_7_days", "last_14_days", "last_30_days", "before_last_14_days"]


class OverviewResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class OverviewResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class OverviewResponseDataItemsItemChartsItem(APIResponseSchema):
    date: str | None = Field(default=None)
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    conversion_rate: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    approved_promotion_participation: int | None = Field(default=None)
    net_item_sold_periodic_promotions: int | None = Field(default=None)
    net_item_sold_incredible_promotions: int | None = Field(default=None)
    net_item_sold_mega_promotions: int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: int | None = Field(default=None)
    count_variants: int | None = Field(default=None)
    count_live_variants: int | None = Field(default=None)
    count_deactive_variants: int | None = Field(default=None)
    count_variants_having_sales: int | None = Field(default=None)
    net_item_sold_click_campaigns: int | None = Field(default=None)


class OverviewResponseDataItemsItemSum(APIResponseSchema):
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    conversion_rate: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    approved_promotion_participation: int | None = Field(default=None)
    net_item_sold_periodic_promotions: int | None = Field(default=None)
    net_item_sold_incredible_promotions: int | None = Field(default=None)
    net_item_sold_mega_promotions: int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: int | None = Field(default=None)
    count_variants: int | None = Field(default=None)
    count_live_variants: int | None = Field(default=None)
    count_deactive_variants: int | None = Field(default=None)
    count_variants_having_sales: int | None = Field(default=None)
    net_item_sold_click_campaigns: int | None = Field(default=None)


class OverviewResponseDataItemsItemOldSum(APIResponseSchema):
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    conversion_rate: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    approved_promotion_participation: int | None = Field(default=None)
    net_item_sold_periodic_promotions: int | None = Field(default=None)
    net_item_sold_incredible_promotions: int | None = Field(default=None)
    net_item_sold_mega_promotions: int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: int | None = Field(default=None)
    count_variants: int | None = Field(default=None)
    count_live_variants: int | None = Field(default=None)
    count_deactive_variants: int | None = Field(default=None)
    count_variants_having_sales: int | None = Field(default=None)
    net_item_sold_click_campaigns: int | None = Field(default=None)


class OverviewResponseDataItemsItemAvg(APIResponseSchema):
    gross_sales_amount: float | int | None = Field(default=None)
    gross_item_sold: float | int | None = Field(default=None)
    conversion_rate: float | int | None = Field(default=None)
    visit_count: float | int | None = Field(default=None)
    approved_promotion_participation: float | int | None = Field(default=None)
    net_item_sold_periodic_promotions: float | int | None = Field(default=None)
    net_item_sold_incredible_promotions: float | int | None = Field(default=None)
    net_item_sold_mega_promotions: float | int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: float | int | None = Field(default=None)
    count_variants: float | int | None = Field(default=None)
    count_live_variants: float | int | None = Field(default=None)
    count_deactive_variants: float | int | None = Field(default=None)
    count_variants_having_sales: float | int | None = Field(default=None)
    net_item_sold_click_campaigns: float | int | None = Field(default=None)


class OverviewResponseDataItemsItemOldAvg(APIResponseSchema):
    gross_sales_amount: float | int | None = Field(default=None)
    gross_item_sold: float | int | None = Field(default=None)
    conversion_rate: float | int | None = Field(default=None)
    visit_count: float | int | None = Field(default=None)
    approved_promotion_participation: float | int | None = Field(default=None)
    net_item_sold_periodic_promotions: float | int | None = Field(default=None)
    net_item_sold_incredible_promotions: float | int | None = Field(default=None)
    net_item_sold_mega_promotions: float | int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: float | int | None = Field(default=None)
    count_variants: float | int | None = Field(default=None)
    count_live_variants: float | int | None = Field(default=None)
    count_deactive_variants: float | int | None = Field(default=None)
    count_variants_having_sales: float | int | None = Field(default=None)
    net_item_sold_click_campaigns: float | int | None = Field(default=None)


class OverviewResponseDataItemsItemProgress(APIResponseSchema):
    gross_sales_amount: float | int | None = Field(default=None)
    gross_item_sold: float | int | None = Field(default=None)
    conversion_rate: float | int | None = Field(default=None)
    visit_count: float | int | None = Field(default=None)
    approved_promotion_participation: float | int | None = Field(default=None)
    net_item_sold_periodic_promotions: float | int | None = Field(default=None)
    net_item_sold_incredible_promotions: float | int | None = Field(default=None)
    net_item_sold_mega_promotions: float | int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: float | int | None = Field(default=None)
    count_variants: float | int | None = Field(default=None)
    count_live_variants: float | int | None = Field(default=None)
    count_deactive_variants: float | int | None = Field(default=None)
    count_variants_having_sales: float | int | None = Field(default=None)
    net_item_sold_click_campaigns: float | int | None = Field(default=None)


class OverviewResponseDataItemsItemAvgProgress(APIResponseSchema):
    gross_sales_amount: float | int | None = Field(default=None)
    gross_item_sold: float | int | None = Field(default=None)
    conversion_rate: float | int | None = Field(default=None)
    visit_count: float | int | None = Field(default=None)
    approved_promotion_participation: float | int | None = Field(default=None)
    net_item_sold_periodic_promotions: float | int | None = Field(default=None)
    net_item_sold_incredible_promotions: float | int | None = Field(default=None)
    net_item_sold_mega_promotions: float | int | None = Field(default=None)
    net_item_sold_selling_and_sales_promotions: float | int | None = Field(default=None)
    count_variants: float | int | None = Field(default=None)
    count_live_variants: float | int | None = Field(default=None)
    count_deactive_variants: float | int | None = Field(default=None)
    count_variants_having_sales: float | int | None = Field(default=None)
    net_item_sold_click_campaigns: float | int | None = Field(default=None)


class TopDeactivatedResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class TopDeactivatedResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class TopDeactivatedResponseDataItemsItem(APIResponseSchema):
    product_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    main_category_id: int | None = Field(default=None)
    gross_amount: int | None = Field(default=None)
    product_title: str | None = Field(default=None)
    view_count: int | None = Field(default=None)
    impression_count: int | None = Field(default=None)
    notification_count: int | None = Field(default=None)
    product_image: str | None = Field(default=None)
    category_title: str | None = Field(default=None)


class SalesTrendQuery(QuerySchema):
    range: Literal["last_7_days", "last_14_days", "last_30_days", "before_last_14_days"]
    category_id: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemNetSales(APIResponseSchema):
    amount: int | None = Field(default=None)
    percentage: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemNetItemSold(APIResponseSchema):
    count: int | None = Field(default=None)
    percentage: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemVisitCount(APIResponseSchema):
    count: int | None = Field(default=None)
    percentage: float | None = Field(default=None)


class SalesTrendResponseDataItemsItemSatisfaction(APIResponseSchema):
    amount: JsonValue = Field(default=None)
    percentage: JsonValue = Field(default=None)


class SalesTrendResponseDataItemsItemOrderCount(APIResponseSchema):
    count: int | None = Field(default=None)
    percentage: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemNetSalesCreditMethod(APIResponseSchema):
    amount: int | None = Field(default=None)
    percentage: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemChartItem(APIResponseSchema):
    marketplace_seller_id: int | None = Field(default=None)
    date: str | None = Field(default=None)
    net_sales_amount: int | None = Field(default=None)
    net_item_sold: int | None = Field(default=None)
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    order_count: int | None = Field(default=None)
    main_category_id: int | None = Field(default=None)
    product_satisfaction_numerator: int | None = Field(default=None)
    product_satisfaction_denominator: int | None = Field(default=None)
    product_satisfaction_rate: int | None = Field(default=None)
    net_sales_amount_credit_method: int | None = Field(default=None)
    net_item_sold_credit_method: int | None = Field(default=None)


class SalesTrendResponseDataItemsItemChartAvg(APIResponseSchema):
    net_sales_amount: int | None = Field(default=None)
    net_item_sold: int | None = Field(default=None)
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    order_count: int | None = Field(default=None)
    main_category_id: int | None = Field(default=None)
    product_satisfaction_numerator: int | None = Field(default=None)
    product_satisfaction_denominator: int | None = Field(default=None)
    product_satisfaction_rate: int | None = Field(default=None)
    net_sales_amount_credit_method: int | None = Field(default=None)
    net_item_sold_credit_method: int | None = Field(default=None)


class SalesTrendResponseDataMetaData(APIResponseSchema):
    categories: ObjectMap[str] | None = Field(default=None)


class SalesReportQuery(QuerySchema):
    range: Literal["last_7_days", "last_14_days", "last_30_days", "before_last_14_days"]
    category_id: int | None = Field(default=None)
    net_item_sold_from: int | None = Field(default=None)
    net_item_sold_to: int | None = Field(default=None)
    net_sales_amount_from: float | None = Field(default=None)
    net_sales_amount_to: float | None = Field(default=None)
    search_field: str | int | None = Field(default=None)


class SalesReportResponseDataItemsItem(APIResponseSchema):
    product_id: int | None = Field(default=None)
    net_sales_amount: int | None = Field(default=None)
    net_item_sold: int | None = Field(default=None)
    gross_sales_amount: int | None = Field(default=None)
    gross_item_sold: int | None = Field(default=None)
    visit_count: int | None = Field(default=None)
    order_count: int | None = Field(default=None)
    main_category_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    conversion_rate: float | None = Field(default=None)
    title: str | None = Field(default=None)
    category_title: str | None = Field(default=None)
    image: str | None = Field(default=None)


class SalesReportResponseDataMetaData(APIResponseSchema):
    categories: ObjectMap[str] | None = Field(default=None)


class ExportResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class OverviewResponseDataItemsItem(APIResponseSchema):
    charts: list[OverviewResponseDataItemsItemChartsItem] | None = Field(default=None)
    sum: OverviewResponseDataItemsItemSum | None = Field(default=None)
    old_sum: OverviewResponseDataItemsItemOldSum | None = Field(default=None)
    avg: OverviewResponseDataItemsItemAvg | None = Field(default=None)
    old_avg: OverviewResponseDataItemsItemOldAvg | None = Field(default=None)
    progress: OverviewResponseDataItemsItemProgress | None = Field(default=None)
    avg_progress: OverviewResponseDataItemsItemAvgProgress | None = Field(default=None)


class TopDeactivatedResponseData(APIResponseSchema):
    sort_data: TopDeactivatedResponseDataSortData | None = Field(default=None)
    pager: TopDeactivatedResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TopDeactivatedResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class SalesTrendResponseDataItemsItem(APIResponseSchema):
    net_sales: SalesTrendResponseDataItemsItemNetSales | None = Field(default=None)
    net_item_sold: SalesTrendResponseDataItemsItemNetItemSold | None = Field(default=None)
    visit_count: SalesTrendResponseDataItemsItemVisitCount | None = Field(default=None)
    satisfaction: SalesTrendResponseDataItemsItemSatisfaction | None = Field(default=None)
    order_count: SalesTrendResponseDataItemsItemOrderCount | None = Field(default=None)
    net_sales_credit_method: SalesTrendResponseDataItemsItemNetSalesCreditMethod | None = Field(
        default=None
    )
    chart: list[SalesTrendResponseDataItemsItemChartItem] | None = Field(default=None)
    chart_avg: SalesTrendResponseDataItemsItemChartAvg | None = Field(default=None)


class SalesReportResponseData(APIResponseSchema):
    sort_data: OverviewResponseDataSortData | None = Field(default=None)
    pager: OverviewResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SalesReportResponseDataItemsItem] | None = Field(default=None)
    meta_data: SalesReportResponseDataMetaData | None = Field(default=None)


class ExportResponse(APIResponseSchema):
    status: str
    data: ExportResponseData


class OverviewResponseData(APIResponseSchema):
    sort_data: OverviewResponseDataSortData | None = Field(default=None)
    pager: OverviewResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[OverviewResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class TopDeactivatedResponse(APIResponseSchema):
    status: str
    data: TopDeactivatedResponseData


class SalesTrendResponseData(APIResponseSchema):
    sort_data: OverviewResponseDataSortData | None = Field(default=None)
    pager: OverviewResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SalesTrendResponseDataItemsItem] | None = Field(default=None)
    meta_data: SalesTrendResponseDataMetaData | None = Field(default=None)


class SalesReportResponse(APIResponseSchema):
    status: str
    data: SalesReportResponseData


class OverviewResponse(APIResponseSchema):
    status: str
    data: OverviewResponseData


class SalesTrendResponse(APIResponseSchema):
    status: str
    data: SalesTrendResponseData


__all__ = [
    "ExportResponse",
    "ExportResponseData",
    "OverviewQuery",
    "OverviewResponse",
    "OverviewResponseData",
    "OverviewResponseDataItemsItem",
    "OverviewResponseDataItemsItemAvg",
    "OverviewResponseDataItemsItemAvgProgress",
    "OverviewResponseDataItemsItemChartsItem",
    "OverviewResponseDataItemsItemOldAvg",
    "OverviewResponseDataItemsItemOldSum",
    "OverviewResponseDataItemsItemProgress",
    "OverviewResponseDataItemsItemSum",
    "OverviewResponseDataPager",
    "OverviewResponseDataSortData",
    "SalesReportQuery",
    "SalesReportResponse",
    "SalesReportResponseData",
    "SalesReportResponseDataItemsItem",
    "SalesReportResponseDataMetaData",
    "SalesTrendQuery",
    "SalesTrendResponse",
    "SalesTrendResponseData",
    "SalesTrendResponseDataItemsItem",
    "SalesTrendResponseDataItemsItemChartAvg",
    "SalesTrendResponseDataItemsItemChartItem",
    "SalesTrendResponseDataItemsItemNetItemSold",
    "SalesTrendResponseDataItemsItemNetSales",
    "SalesTrendResponseDataItemsItemNetSalesCreditMethod",
    "SalesTrendResponseDataItemsItemOrderCount",
    "SalesTrendResponseDataItemsItemSatisfaction",
    "SalesTrendResponseDataItemsItemVisitCount",
    "SalesTrendResponseDataMetaData",
    "TopDeactivatedResponse",
    "TopDeactivatedResponseData",
    "TopDeactivatedResponseDataItemsItem",
    "TopDeactivatedResponseDataPager",
    "TopDeactivatedResponseDataSortData",
]
