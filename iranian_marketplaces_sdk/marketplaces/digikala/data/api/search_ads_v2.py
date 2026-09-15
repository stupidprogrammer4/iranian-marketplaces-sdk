"""Digikala search ads v2: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ProductsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: (
        Literal[
            "id",
            "created_at",
            "latest",
            "best_seller",
            "highest_cr",
            "most_visited",
            "most_popular",
            "fastest_shipping",
            "highest_discount",
            "price_high_low",
            "price_low_high",
            "recommended",
        ]
        | None
    ) = Field(default=None)
    order: str | None = Field(default=None)
    search_q: list[str] | None = Field(
        default=None, validation_alias="search[q]", serialization_alias="search[q]"
    )
    search_category_filter: int | None = Field(
        default=None,
        validation_alias="search[category_filter]",
        serialization_alias="search[category_filter]",
    )
    search_campaign_id: int | None = Field(
        default=None,
        validation_alias="search[campaign_id]",
        serialization_alias="search[campaign_id]",
    )


class ProductsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ProductsResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ProductsResponseDataItemsItem(APIResponseSchema):
    product_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    category_name: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    is_eligible: bool | None = Field(default=None)
    ineligible_reason: str | None = Field(default=None)
    ai_chosen: bool | None = Field(default=None)
    ai_score: float | None = Field(default=None)
    ai_chosen_reason: str | None = Field(default=None)


class SettingsQuery(QuerySchema):
    category_ids: int | None = Field(
        default=None, validation_alias="category_ids[]", serialization_alias="category_ids[]"
    )


class SettingsResponseDataBoundsItem(APIResponseSchema):
    category_id: int | None = Field(default=None)
    points: list[int] | None = Field(default=None)
    offered_price: int | None = Field(default=None)


class CreateRequestCampaignProductsItem(RequestSchema):
    product_id: int | None = Field(default=None)
    bid_amount: int | None = Field(default=None)


class CreateResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    message: str | None = Field(default=None)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: (
        Literal["id", "title", "start_date", "end_date", "status", "created_at", "updated_at"]
        | None
    ) = Field(default=None)
    order: str | None = Field(default=None)
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
    search_campaign_id: int | None = Field(
        default=None,
        validation_alias="search[campaign_id]",
        serialization_alias="search[campaign_id]",
    )


class ListResponseDataItemsItemUsedBudget(APIResponseSchema):
    today: int | None = Field(default=None)
    total: int | None = Field(default=None)


class GetResponseDataProductsItemCategory(APIResponseSchema):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)


class UpdateRequestCampaign(RequestSchema):
    title: str | None = Field(default=None)
    products: list[CreateRequestCampaignProductsItem] | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    payment_method: str | None = Field(default=None)


class UpdateResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    message: str | None = Field(default=None)


class ReportQuery(QuerySchema):
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class ReportResponseDataCampaignDateReportDtomapValue(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    date: str | None = Field(default=None)


class ReportResponseDataCampaignProductReportDtomapValue(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    product_date_report_dtomap: ObjectMap[JsonValue] | None = Field(
        default=None,
        validation_alias="productDateReportDTOMap",
        serialization_alias="productDateReportDTOMap",
    )


class OverviewQuery(QuerySchema):
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class OverviewResponseData(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    campaign_date_report_dtomap: (
        ObjectMap[ReportResponseDataCampaignDateReportDtomapValue] | None
    ) = Field(
        default=None,
        validation_alias="campaignDateReportDTOMap",
        serialization_alias="campaignDateReportDTOMap",
    )
    campaign_product_report_dtomap: (
        ObjectMap[ReportResponseDataCampaignProductReportDtomapValue] | None
    ) = Field(
        default=None,
        validation_alias="campaignProductReportDTOMap",
        serialization_alias="campaignProductReportDTOMap",
    )


class CampaignProductOverviewQuery(QuerySchema):
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class CampaignProductOverviewResponseDataProductDateReportDtomapValue(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    date: str | None = Field(default=None)


class ProductOverviewQuery(QuerySchema):
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class ProductOverviewResponseData(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class SellerOverviewQuery(QuerySchema):
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class SellerOverviewResponseData(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)


class UpdateStatusResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateBidRequestCampaign(RequestSchema):
    product_id: int
    bid_amount: int


class UpdateBidResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    bid_amount: int | None = Field(default=None)
    message: str | None = Field(default=None)


class AddProductsRequestProductsItem(RequestSchema):
    product_id: int | None = Field(default=None)
    bid_amount: int | None = Field(default=None)


class AddProductsResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    product_ids: list[int] | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateProductStatusRequest(RequestSchema):
    active: bool


class UpdateProductStatusResponseData(APIResponseSchema):
    campaign_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    active: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class ProductsResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ProductsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class SettingsResponseData(APIResponseSchema):
    bounds: list[SettingsResponseDataBoundsItem] | None = Field(default=None)
    now: str | None = Field(default=None)
    now_iso8601: str | None = Field(default=None)
    now_moment_js: str | None = Field(default=None)
    daily_budget_max: int | None = Field(default=None)
    daily_budget_min: int | None = Field(default=None)
    daily_budget_min_clicks: int | None = Field(default=None)
    total_budget_max: int | None = Field(default=None)
    total_budget_min: int | None = Field(default=None)
    total_budget_min_clicks: int | None = Field(default=None)


class CreateRequestCampaign(RequestSchema):
    title: str
    products: list[CreateRequestCampaignProductsItem]
    start_date: str
    end_date: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    payment_method: str | None = Field(default=None)


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    used_budget: ListResponseDataItemsItemUsedBudget | None = Field(default=None)
    payment_method: str | None = Field(default=None)
    pacing_info: ObjectMap[JsonValue] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)


class GetResponseDataProductsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    active: bool | None = Field(default=None)
    dkp: int | None = Field(default=None)
    title: str | None = Field(default=None)
    image: str | None = Field(default=None)
    category: GetResponseDataProductsItemCategory | None = Field(default=None)
    bid_amount: int | None = Field(default=None)
    has_optimized_bid_offer: bool | None = Field(default=None)
    optimized_bid_offer: int | None = Field(default=None)


class UpdateRequest(RequestSchema):
    campaign: UpdateRequestCampaign


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class ReportResponseData(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    campaign_date_report_dtomap: (
        ObjectMap[ReportResponseDataCampaignDateReportDtomapValue] | None
    ) = Field(
        default=None,
        validation_alias="campaignDateReportDTOMap",
        serialization_alias="campaignDateReportDTOMap",
    )
    campaign_product_report_dtomap: (
        ObjectMap[ReportResponseDataCampaignProductReportDtomapValue] | None
    ) = Field(
        default=None,
        validation_alias="campaignProductReportDTOMap",
        serialization_alias="campaignProductReportDTOMap",
    )


class OverviewResponse(APIResponseSchema):
    status: int | str
    data: OverviewResponseData


class CampaignProductOverviewResponseData(APIResponseSchema):
    campaign_id: int | None = Field(
        default=None, validation_alias="campaignId", serialization_alias="campaignId"
    )
    seller_id: int | None = Field(
        default=None, validation_alias="sellerId", serialization_alias="sellerId"
    )
    clicks: int | None = Field(default=None)
    impressions: int | None = Field(default=None)
    conversions: int | None = Field(default=None)
    conversion_items_count: int | None = Field(
        default=None,
        validation_alias="conversionItemsCount",
        serialization_alias="conversionItemsCount",
    )
    conversion_total_order_payable_price: int | None = Field(
        default=None,
        validation_alias="conversionTotalOrderPayablePrice",
        serialization_alias="conversionTotalOrderPayablePrice",
    )
    total_bid_price: int | None = Field(
        default=None, validation_alias="totalBidPrice", serialization_alias="totalBidPrice"
    )
    ctr_percent: float | None = Field(
        default=None, validation_alias="ctrPercent", serialization_alias="ctrPercent"
    )
    cr_percent: float | None = Field(
        default=None, validation_alias="crPercent", serialization_alias="crPercent"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    product_date_report_dtomap: (
        ObjectMap[CampaignProductOverviewResponseDataProductDateReportDtomapValue] | None
    ) = Field(
        default=None,
        validation_alias="productDateReportDTOMap",
        serialization_alias="productDateReportDTOMap",
    )


class ProductOverviewResponse(APIResponseSchema):
    status: int | str
    data: ProductOverviewResponseData


class SellerOverviewResponse(APIResponseSchema):
    status: int | str
    data: SellerOverviewResponseData


class UpdateStatusResponse(APIResponseSchema):
    status: str
    data: UpdateStatusResponseData


class UpdateBidRequest(RequestSchema):
    campaign: UpdateBidRequestCampaign


class UpdateBidResponse(APIResponseSchema):
    status: str
    data: UpdateBidResponseData


class AddProductsRequest(RequestSchema):
    products: list[AddProductsRequestProductsItem]


class AddProductsResponse(APIResponseSchema):
    status: str
    data: AddProductsResponseData


class UpdateProductStatusResponse(APIResponseSchema):
    status: str
    data: UpdateProductStatusResponseData


class ProductsResponse(APIResponseSchema):
    status: str
    data: ProductsResponseData


class SettingsResponse(APIResponseSchema):
    status: int | str
    data: SettingsResponseData


class CreateRequest(RequestSchema):
    campaign: CreateRequestCampaign


class ListResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    start_date: str | None = Field(default=None)
    end_date: str | None = Field(default=None)
    status: str | None = Field(default=None)
    reason: str | None = Field(default=None)
    daily_budget: int | None = Field(default=None)
    total_budget: int | None = Field(default=None)
    used_budget: ListResponseDataItemsItemUsedBudget | None = Field(default=None)
    payment_method: str | None = Field(default=None)
    pacing_info: ObjectMap[JsonValue] | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
    products: list[GetResponseDataProductsItem] | None = Field(default=None)


class ReportResponse(APIResponseSchema):
    status: int | str
    data: ReportResponseData


class CampaignProductOverviewResponse(APIResponseSchema):
    status: int | str
    data: CampaignProductOverviewResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


__all__ = [
    "AddProductsRequest",
    "AddProductsRequestProductsItem",
    "AddProductsResponse",
    "AddProductsResponseData",
    "CampaignProductOverviewQuery",
    "CampaignProductOverviewResponse",
    "CampaignProductOverviewResponseData",
    "CampaignProductOverviewResponseDataProductDateReportDtomapValue",
    "CreateRequest",
    "CreateRequestCampaign",
    "CreateRequestCampaignProductsItem",
    "CreateResponse",
    "CreateResponseData",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataProductsItem",
    "GetResponseDataProductsItemCategory",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemUsedBudget",
    "OverviewQuery",
    "OverviewResponse",
    "OverviewResponseData",
    "ProductOverviewQuery",
    "ProductOverviewResponse",
    "ProductOverviewResponseData",
    "ProductsQuery",
    "ProductsResponse",
    "ProductsResponseData",
    "ProductsResponseDataItemsItem",
    "ProductsResponseDataPager",
    "ProductsResponseDataSortData",
    "ReportQuery",
    "ReportResponse",
    "ReportResponseData",
    "ReportResponseDataCampaignDateReportDtomapValue",
    "ReportResponseDataCampaignProductReportDtomapValue",
    "SellerOverviewQuery",
    "SellerOverviewResponse",
    "SellerOverviewResponseData",
    "SettingsQuery",
    "SettingsResponse",
    "SettingsResponseData",
    "SettingsResponseDataBoundsItem",
    "UpdateBidRequest",
    "UpdateBidRequestCampaign",
    "UpdateBidResponse",
    "UpdateBidResponseData",
    "UpdateProductStatusRequest",
    "UpdateProductStatusResponse",
    "UpdateProductStatusResponseData",
    "UpdateRequest",
    "UpdateRequestCampaign",
    "UpdateResponse",
    "UpdateResponseData",
    "UpdateStatusResponse",
    "UpdateStatusResponseData",
]
