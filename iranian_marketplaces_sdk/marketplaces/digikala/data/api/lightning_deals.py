"""Digikala lightning deals: request and response models."""

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
    sort: str | None = Field(default=None)
    order: str | None = Field(default=None)
    search_q: str | None = Field(
        default=None, validation_alias="search[q]", serialization_alias="search[q]"
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
    id: int | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    image: str | None = Field(default=None)
    price: int | None = Field(default=None)
    views: int | None = Field(default=None)
    orders: int | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    disabled: bool | None = Field(default=None)
    validation_messages: list[str] | None = Field(
        default=None,
        validation_alias="validationMessages",
        serialization_alias="validationMessages",
    )
    stock: int | None = Field(default=None)


class GetProductQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)


class GetProductResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    image: str | None = Field(default=None)
    stock: int | None = Field(default=None)
    has_stock: bool | None = Field(default=None)
    max_send_to_warehouse: int | None = Field(default=None)
    min_discount: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    price: int | None = Field(default=None)
    views: int | None = Field(default=None)
    orders: int | None = Field(default=None)


class PromotionsResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ObjectMap[JsonValue]] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetPromotionsResponseDataItemsItemTimeslotsValue0(APIResponseSchema):
    start_at: str | None = Field(
        default=None, validation_alias="startAt", serialization_alias="startAt"
    )
    end_at: str | None = Field(default=None, validation_alias="endAt", serialization_alias="endAt")
    start_at_time: str | None = Field(
        default=None, validation_alias="startAtTime", serialization_alias="startAtTime"
    )
    end_at_time: str | None = Field(
        default=None, validation_alias="endAtTime", serialization_alias="endAtTime"
    )
    promotion_id: int | None = Field(
        default=None, validation_alias="promotionId", serialization_alias="promotionId"
    )
    bid_count: int | None = Field(
        default=None, validation_alias="bidCount", serialization_alias="bidCount"
    )
    max_bid: int | None = Field(
        default=None, validation_alias="maxBid", serialization_alias="maxBid"
    )
    min_bid_to_win: int | None = Field(
        default=None, validation_alias="minBidToWin", serialization_alias="minBidToWin"
    )
    min_allowable_bid: int | None = Field(
        default=None, validation_alias="minAllowableBid", serialization_alias="minAllowableBid"
    )
    max_allowable_bid: int | None = Field(
        default=None, validation_alias="maxAllowableBid", serialization_alias="maxAllowableBid"
    )


class CreateBidsRequestBidsDataItemPromotionsItem(RequestSchema):
    promotion_id: int | None = Field(
        default=None, validation_alias="promotionId", serialization_alias="promotionId"
    )
    promotion_price: int | None = Field(
        default=None, validation_alias="promotionPrice", serialization_alias="promotionPrice"
    )
    number_of_variants_in_promotion: int | None = Field(
        default=None,
        validation_alias="numberOfVariantsInPromotion",
        serialization_alias="numberOfVariantsInPromotion",
    )
    min_bid: int | None = Field(
        default=None, validation_alias="minBid", serialization_alias="minBid"
    )
    auto_raise: int | None = Field(
        default=None, validation_alias="autoRaise", serialization_alias="autoRaise"
    )
    upper_bound: int | None = Field(
        default=None, validation_alias="upperBound", serialization_alias="upperBound"
    )
    payment_method: str | None = Field(
        default=None, validation_alias="paymentMethod", serialization_alias="paymentMethod"
    )


class CreateBidsResponseData(APIResponseSchema):
    charge_wallet: bool | None = Field(
        default=None, validation_alias="chargeWallet", serialization_alias="chargeWallet"
    )
    total_bids_price: int | None = Field(
        default=None, validation_alias="totalBIdsPrice", serialization_alias="totalBIdsPrice"
    )
    product_variants_count: int | None = Field(
        default=None,
        validation_alias="productVariantsCount",
        serialization_alias="productVariantsCount",
    )
    promotions_count: int | None = Field(
        default=None, validation_alias="promotionsCount", serialization_alias="promotionsCount"
    )
    total_price: int | None = Field(
        default=None, validation_alias="totalPrice", serialization_alias="totalPrice"
    )
    total_price_wallet: int | None = Field(
        default=None, validation_alias="totalPriceWallet", serialization_alias="totalPriceWallet"
    )
    total_price_credit: int | None = Field(
        default=None, validation_alias="totalPriceCredit", serialization_alias="totalPriceCredit"
    )
    variant_quantity: int | None = Field(
        default=None, validation_alias="variantQuantity", serialization_alias="variantQuantity"
    )
    promotions_quantity: int | None = Field(
        default=None,
        validation_alias="promotionsQuantity",
        serialization_alias="promotionsQuantity",
    )


class BidsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_status: (
        Literal[
            "all", "pending", "payment", "productSupply", "approvedWinner", "live", "ended", "lost"
        ]
        | None
    ) = Field(default=None, validation_alias="search[status]", serialization_alias="search[status]")
    search_start_date: int | None = Field(
        default=None, validation_alias="search[startDate]", serialization_alias="search[startDate]"
    )
    search_end_date: int | None = Field(
        default=None, validation_alias="search[endDate]", serialization_alias="search[endDate]"
    )
    search_q: str | None = Field(
        default=None, validation_alias="search[q]", serialization_alias="search[q]"
    )


class BidsResponseDataItemsItemDate(APIResponseSchema):
    day: int | None = Field(default=None)
    month: str | None = Field(default=None)
    weekday_name: str | None = Field(
        default=None, validation_alias="weekdayName", serialization_alias="weekdayName"
    )
    start: str | None = Field(default=None)
    end: str | None = Field(default=None)
    start_hour: str | None = Field(
        default=None, validation_alias="startHour", serialization_alias="startHour"
    )
    end_hour: str | None = Field(
        default=None, validation_alias="endHour", serialization_alias="endHour"
    )


class BidsResponseDataItemsItemRemainingTime(APIResponseSchema):
    days: int | None = Field(default=None)
    hours: int | None = Field(default=None)
    minutes: int | None = Field(default=None)


class BidsResponseDataItemsItemProductVariantsItem(APIResponseSchema):
    title: str | None = Field(default=None)
    product_variant_id: int | None = Field(
        default=None, validation_alias="productVariantId", serialization_alias="productVariantId"
    )
    dkpc: int | None = Field(default=None)
    price: int | None = Field(default=None)
    promotion_price: int | None = Field(
        default=None, validation_alias="promotionPrice", serialization_alias="promotionPrice"
    )
    off_percent: int | None = Field(
        default=None, validation_alias="offPercent", serialization_alias="offPercent"
    )
    number_of_variants_in_promotion: int | None = Field(
        default=None,
        validation_alias="numberOfVariantsInPromotion",
        serialization_alias="numberOfVariantsInPromotion",
    )
    remaining_number_of_variants_in_promotion: int | None = Field(
        default=None,
        validation_alias="remainingNumberOfVariantsInPromotion",
        serialization_alias="remainingNumberOfVariantsInPromotion",
    )
    number_of_variants_sold_in_promotion: int | None = Field(
        default=None,
        validation_alias="numberOfVariantsSoldInPromotion",
        serialization_alias="numberOfVariantsSoldInPromotion",
    )
    revenue: int | None = Field(default=None)
    image: str | None = Field(default=None)


class BidsSummaryResponseData(APIResponseSchema):
    pending: int | None = Field(default=None)
    payment: int | None = Field(default=None)
    product_supply: int | None = Field(
        default=None, validation_alias="productSupply", serialization_alias="productSupply"
    )
    approved_winner: int | None = Field(
        default=None, validation_alias="approvedWinner", serialization_alias="approvedWinner"
    )
    live: int | None = Field(default=None)
    ended: int | None = Field(default=None)
    lost: int | None = Field(default=None)


class CheckDuplicateRequest(RequestSchema):
    promotion_id: int = Field(validation_alias="promotionId", serialization_alias="promotionId")
    product_id: int = Field(validation_alias="productId", serialization_alias="productId")


class CheckDuplicateResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class UpdatePaymentMethodRequest(RequestSchema):
    payment_method: str = Field(
        validation_alias="paymentMethod", serialization_alias="paymentMethod"
    )


class ProductsResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ProductsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetProductResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetProductResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class PromotionsResponse(APIResponseSchema):
    status: str
    data: PromotionsResponseData


class GetPromotionsResponseDataItemsItem(APIResponseSchema):
    start_date: str | None = Field(
        default=None, validation_alias="startDate", serialization_alias="startDate"
    )
    day: int | None = Field(default=None)
    month: str | None = Field(default=None)
    year: int | None = Field(default=None)
    weekday_name: str | None = Field(
        default=None, validation_alias="weekdayName", serialization_alias="weekdayName"
    )
    day_of_week: int | None = Field(
        default=None, validation_alias="dayOfWeek", serialization_alias="dayOfWeek"
    )
    message: str | None = Field(default=None)
    timeslots: ObjectMap[GetPromotionsResponseDataItemsItemTimeslotsValue0] | None = Field(
        default=None
    )


class CreateBidsRequestBidsDataItem(RequestSchema):
    product_variant_id: int | None = Field(
        default=None, validation_alias="productVariantId", serialization_alias="productVariantId"
    )
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    source: str | None = Field(default=None)
    promotions: list[CreateBidsRequestBidsDataItemPromotionsItem] | None = Field(default=None)


class CreateBidsResponse(APIResponseSchema):
    status: str
    data: CreateBidsResponseData


class BidsResponseDataItemsItem(APIResponseSchema):
    promotion_id: int | None = Field(
        default=None, validation_alias="promotionId", serialization_alias="promotionId"
    )
    bid_id: int | None = Field(default=None, validation_alias="bidId", serialization_alias="bidId")
    dkp: int | None = Field(default=None)
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    date: BidsResponseDataItemsItemDate | None = Field(default=None)
    remaining_time: BidsResponseDataItemsItemRemainingTime | None = Field(
        default=None, validation_alias="remainingTime", serialization_alias="remainingTime"
    )
    bid_count: int | None = Field(
        default=None, validation_alias="bidCount", serialization_alias="bidCount"
    )
    min_bid: int | None = Field(
        default=None, validation_alias="minBid", serialization_alias="minBid"
    )
    max_bid: int | None = Field(
        default=None, validation_alias="maxBid", serialization_alias="maxBid"
    )
    auto_raise: int | None = Field(
        default=None, validation_alias="autoRaise", serialization_alias="autoRaise"
    )
    final_bid_amount: int | None = Field(
        default=None, validation_alias="finalBidAmount", serialization_alias="finalBidAmount"
    )
    status: str | None = Field(default=None)
    payment_method: str | None = Field(
        default=None, validation_alias="paymentMethod", serialization_alias="paymentMethod"
    )
    is_payment_method_editable: bool | None = Field(
        default=None,
        validation_alias="isPaymentMethodEditable",
        serialization_alias="isPaymentMethodEditable",
    )
    available_payment_methods: list[str] | None = Field(
        default=None,
        validation_alias="availablePaymentMethods",
        serialization_alias="availablePaymentMethods",
    )
    product_variants: list[BidsResponseDataItemsItemProductVariantsItem] | None = Field(
        default=None, validation_alias="productVariants", serialization_alias="productVariants"
    )


class BidsSummaryResponse(APIResponseSchema):
    status: int | str
    data: BidsSummaryResponseData


class CheckDuplicateResponse(APIResponseSchema):
    status: int | str
    data: CheckDuplicateResponseData


class ProductsResponse(APIResponseSchema):
    status: str
    data: ProductsResponseData


class GetProductResponse(APIResponseSchema):
    status: str
    data: GetProductResponseData


class GetPromotionsResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetPromotionsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CreateBidsRequest(RequestSchema):
    bids_data: list[CreateBidsRequestBidsDataItem] = Field(
        validation_alias="bidsData", serialization_alias="bidsData"
    )


class BidsResponseData(APIResponseSchema):
    sort_data: ProductsResponseDataSortData | None = Field(default=None)
    pager: ProductsResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[BidsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetPromotionsResponse(APIResponseSchema):
    status: str
    data: GetPromotionsResponseData


class BidsResponse(APIResponseSchema):
    status: str
    data: BidsResponseData


__all__ = [
    "BidsQuery",
    "BidsResponse",
    "BidsResponseData",
    "BidsResponseDataItemsItem",
    "BidsResponseDataItemsItemDate",
    "BidsResponseDataItemsItemProductVariantsItem",
    "BidsResponseDataItemsItemRemainingTime",
    "BidsSummaryResponse",
    "BidsSummaryResponseData",
    "CheckDuplicateRequest",
    "CheckDuplicateResponse",
    "CheckDuplicateResponseData",
    "CreateBidsRequest",
    "CreateBidsRequestBidsDataItem",
    "CreateBidsRequestBidsDataItemPromotionsItem",
    "CreateBidsResponse",
    "CreateBidsResponseData",
    "GetProductQuery",
    "GetProductResponse",
    "GetProductResponseData",
    "GetProductResponseDataItemsItem",
    "GetPromotionsResponse",
    "GetPromotionsResponseData",
    "GetPromotionsResponseDataItemsItem",
    "GetPromotionsResponseDataItemsItemTimeslotsValue0",
    "ProductsQuery",
    "ProductsResponse",
    "ProductsResponseData",
    "ProductsResponseDataItemsItem",
    "ProductsResponseDataPager",
    "ProductsResponseDataSortData",
    "PromotionsResponse",
    "PromotionsResponseData",
    "UpdatePaymentMethodRequest",
]
