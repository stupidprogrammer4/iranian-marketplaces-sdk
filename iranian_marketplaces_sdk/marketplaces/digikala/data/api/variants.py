"""Digikala variants: request and response models."""

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
            "id",
            "product_variant_id",
            "selling_stock",
            "selling_price",
            "marketplace_seller_stock",
            "warehouse_stock",
            "created_at",
        ]
        | None
    ) = Field(default=None)
    order: str | None = Field(default=None)
    search_id: int | None = Field(
        default=None, validation_alias="search[id]", serialization_alias="search[id]"
    )
    search_ids: list[int] | None = Field(
        default=None, validation_alias="search[ids]", serialization_alias="search[ids]"
    )
    search_shipping_type: Literal["seller", "digikala", "both"] | None = Field(
        default=None,
        validation_alias="search[shipping_type]",
        serialization_alias="search[shipping_type]",
    )
    search_active: bool | None = Field(
        default=None, validation_alias="search[active]", serialization_alias="search[active]"
    )
    search_moderation_status: str | None = Field(
        default=None,
        validation_alias="search[moderation_status]",
        serialization_alias="search[moderation_status]",
    )
    search_category_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[category_ids]",
        serialization_alias="search[category_ids]",
    )
    search_buy_box_winner: Literal["product", "no_winner", "sku", "suppressed"] | None = Field(
        default=None,
        validation_alias="search[buy_box_winner]",
        serialization_alias="search[buy_box_winner]",
    )
    search_in_competition: bool | None = Field(
        default=None,
        validation_alias="search[in_competition]",
        serialization_alias="search[in_competition]",
    )
    search_search_term: str | None = Field(
        default=None,
        validation_alias="search[search_term]",
        serialization_alias="search[search_term]",
    )
    search_price_terms: list[str] | None = Field(
        default=None,
        validation_alias="search[price_terms]",
        serialization_alias="search[price_terms]",
    )
    search_out_of_stock: bool | None = Field(
        default=None,
        validation_alias="search[out_of_stock]",
        serialization_alias="search[out_of_stock]",
    )
    search_archived: bool | None = Field(
        default=None, validation_alias="search[archived]", serialization_alias="search[archived]"
    )
    search_selling_channel: (
        Literal[
            "digikala",
            "digistyle",
            "digikala_digistyle",
            "b2b",
            "digikala_b2b",
            "digistyle_b2b",
            "all",
        ]
        | None
    ) = Field(
        default=None,
        validation_alias="search[selling_channel]",
        serialization_alias="search[selling_channel]",
    )
    search_creation_time_from: str | None = Field(
        default=None,
        validation_alias="search[creation_time_from]",
        serialization_alias="search[creation_time_from]",
    )
    search_creation_time_to: str | None = Field(
        default=None,
        validation_alias="search[creation_time_to]",
        serialization_alias="search[creation_time_to]",
    )
    search_seller_product_tags: str | None = Field(
        default=None,
        validation_alias="search[seller_product_tags]",
        serialization_alias="search[seller_product_tags]",
    )
    search_nearby_seller_shipment: bool | None = Field(
        default=None,
        validation_alias="search[nearby_seller_shipment]",
        serialization_alias="search[nearby_seller_shipment]",
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


class ListResponseDataItemsItemCreatedAt1(APIResponseSchema):
    date: str | None = Field(default=None)
    timezone_type: int | None = Field(default=None)
    timezone: str | None = Field(default=None)


class ListResponseDataItemsItemB2bParams(APIResponseSchema):
    seller_b2b_active: bool | None = Field(default=None)
    is_only_b2b: bool | None = Field(default=None)
    is_b2b_active: bool | None = Field(default=None)


class ListResponseDataItemsItemSkuConfig(APIResponseSchema):
    color: str | None = Field(default=None)
    size: str | None = Field(default=None)


class ListResponseDataItemsItemProductSellingChanel(APIResponseSchema):
    active_digikala: bool | None = Field(default=None)
    active_digistyle: bool | None = Field(default=None)


class ListResponseDataItemsItemVariantSellingChanel(APIResponseSchema):
    active_digikala: bool | None = Field(default=None)
    active_digistyle: bool | None = Field(default=None)


class ListResponseDataItemsItemThemeValuesItemThemeValueValue(APIResponseSchema):
    hex: str | None = Field(default=None)
    rgb: str | None = Field(default=None)
    value: str | None = Field(default=None)


class ListResponseDataItemsItemShippingOptions(APIResponseSchema):
    is_fbs_ability_enable: bool | None = Field(default=None)
    is_fbd_active: bool | None = Field(default=None)
    is_fbs_active: bool | None = Field(default=None)
    is_needed_fbs_setting: bool | None = Field(default=None)
    is_sbs_module_active: bool | None = Field(default=None)
    only_sbs: bool | None = Field(default=None)
    is_three_hour_delivery_active: bool | None = Field(default=None)
    is_three_hour_checkbox_active: bool | None = Field(default=None)


class UpdateRequest(RequestSchema):
    seller_stock: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    price_limit: int | None = Field(default=None)
    credit_increase_percentage: float | None = Field(default=None)
    shipping_type: str | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    seller_lead_time: int | None = Field(default=None)
    activation: bool | None = Field(default=None)
    three_hour_delivery: bool | None = Field(default=None)


class UpdateResponseDataShippingOptions(APIResponseSchema):
    is_fbs_ability_enable: bool | None = Field(default=None)
    is_fbd_active: bool | None = Field(default=None)
    is_fbs_active: bool | None = Field(default=None)
    is_needed_fbs_setting: bool | None = Field(default=None)
    is_sbs_module_active: bool | None = Field(default=None)
    only_sbs: bool | None = Field(default=None)
    is_three_hour_delivery_active: bool | None = Field(default=None)


class UpdateB2bActivationRequest(RequestSchema):
    variant_ids: list[int]


class UpdateB2bActivationResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class ExportRequest(RequestSchema):
    id: int | None = Field(default=None)
    shipping_type: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    moderation_status: str | None = Field(default=None)
    category_ids: str | None = Field(default=None)
    buy_box_winner: bool | None = Field(default=None)
    in_competition: bool | None = Field(default=None)
    search_term: str | None = Field(default=None)
    price_terms: str | None = Field(default=None)
    out_of_stock: bool | None = Field(default=None)
    archived: bool | None = Field(default=None)
    selling_channel: str | None = Field(default=None)


class ExportResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class GetGoldResponseData(APIResponseSchema):
    gold_wage: float | None = Field(default=None)
    gold_profit: float | None = Field(default=None)
    none_gold_wage: float | None = Field(default=None)
    none_gold_cost: float | None = Field(default=None)
    is_pure: bool | None = Field(default=None)
    size: float | None = Field(default=None)
    tax: int | None = Field(default=None)
    live_gold_price: int | None = Field(default=None)


class UpdateGoldRequest(RequestSchema):
    gold_wage: float
    gold_profit: float
    none_gold_wage: float | None = Field(default=None)
    none_gold_cost: float | None = Field(default=None)
    order_limit: int


class UpdateGoldResponseData(APIResponseSchema):
    status: str | None = Field(default=None)
    did_b2b_deactivate: bool | None = Field(default=None)


class CalculatePriceQuery(QuerySchema):
    gold_wage: float
    gold_profit: float
    none_gold_wage: float
    none_gold_cost: float


class CalculatePriceResponseDataPrice(APIResponseSchema):
    variant_id: int | None = Field(
        default=None, validation_alias="variantId", serialization_alias="variantId"
    )
    selling_price: int | None = Field(
        default=None, validation_alias="sellingPrice", serialization_alias="sellingPrice"
    )
    is_active: bool | None = Field(
        default=None, validation_alias="isActive", serialization_alias="isActive"
    )
    has_stock: bool | None = Field(
        default=None, validation_alias="hasStock", serialization_alias="hasStock"
    )
    is_winner_buy_box: bool | None = Field(
        default=None, validation_alias="isWinnerBuyBox", serialization_alias="isWinnerBuyBox"
    )
    is_gold: bool | None = Field(
        default=None, validation_alias="isGold", serialization_alias="isGold"
    )


class UpdateActivationRequest(RequestSchema):
    activation: bool


class UpdateActivationResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    main_category_title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_url: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_moderation_status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    product_title: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    price_list: int | None = Field(default=None)
    market_price_last_update: str | None = Field(default=None)
    price_type: str | None = Field(default=None)
    selling_channel_site: str | None = Field(default=None)
    price_sale: int | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    reservation: int | None = Field(default=None)
    left_consumer: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    allowed_count: int | None = Field(default=None)
    ovl_selling_active: bool | None = Field(default=None)
    b2b_params: ListResponseDataItemsItemB2bParams | None = Field(default=None)
    max_lead_time: int | None = Field(default=None)
    buy_box_price: int | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    is_seller_buy_box_winner: bool | None = Field(default=None)
    is_in_buy_box_challenge: bool | None = Field(default=None)
    min_selling_price_limit: int | None = Field(default=None)
    product_selling_chanel: ListResponseDataItemsItemProductSellingChanel | None = Field(
        default=None
    )
    variant_selling_chanel: ListResponseDataItemsItemVariantSellingChanel | None = Field(
        default=None
    )
    is_in_incredible_promotion: bool | None = Field(default=None)
    is_in_periodic_promotion: bool | None = Field(default=None)
    is_in_promotion: bool | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    default_selling_chanel_code: int | None = Field(default=None)
    rating: float | None = Field(default=None)
    is_promotion_management_visible_for_seller: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    fulfilment_and_delivery_cost: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)
    seller_shipping_lead_time: int | None = Field(default=None)
    shipping_options: UpdateResponseDataShippingOptions | None = Field(default=None)


class GetB2bPricesResponseDataBucketsItem(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)
    selling_price: int | None = Field(
        default=None, validation_alias="sellingPrice", serialization_alias="sellingPrice"
    )


class UpdateB2bPricesRequestB2bPricesItem(RequestSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)


class UpdateB2bPricesResponse(APIResponseSchema):
    status: str
    data: UpdateB2bActivationResponseData


class ArchiveRequest(RequestSchema):
    archive: bool


class ArchiveResponse(APIResponseSchema):
    status: str
    data: UpdateB2bActivationResponseData


class GetSellerStockResponseData(APIResponseSchema):
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    reservation: int | None = Field(default=None)
    left_consumer: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)


class UpdateSellerStockRequest(RequestSchema):
    seller_stock: int


class UpdateSellerStockResponseData(APIResponseSchema):
    selling_stock: int | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    dk_warehouse_stock: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)


class UpdateSellingPriceRequest(RequestSchema):
    variant_id: int
    selling_price: int
    credit_increase_percentage: int


class UpdateSellingPriceResponseData(APIResponseSchema):
    variant_id: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    credit_increase_percentage: int | None = Field(default=None)


class ListResponseDataItemsItemThemeValuesItemThemeValue(APIResponseSchema):
    id: int | None = Field(default=None)
    title_fa: str | None = Field(
        default=None, validation_alias="titleFa", serialization_alias="titleFa"
    )
    title_en: str | None = Field(
        default=None, validation_alias="titleEn", serialization_alias="titleEn"
    )
    value: ListResponseDataItemsItemThemeValuesItemThemeValueValue | None = Field(default=None)
    nature: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    standard_unit_id: int | None = Field(
        default=None, validation_alias="standardUnitID", serialization_alias="standardUnitID"
    )
    color_pallate_ids: list[int] | None = Field(
        default=None, validation_alias="colorPallateIDs", serialization_alias="colorPallateIDs"
    )
    extra_data: ObjectMap[JsonValue] | None = Field(
        default=None, validation_alias="extraData", serialization_alias="extraData"
    )


class UpdateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    main_category_title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_url: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_moderation_status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    product_title: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    price_list: int | None = Field(default=None)
    market_price_last_update: str | None = Field(default=None)
    price_type: str | None = Field(default=None)
    selling_channel_site: str | None = Field(default=None)
    price_sale: int | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    reservation: int | None = Field(default=None)
    left_consumer: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    allowed_count: int | None = Field(default=None)
    ovl_selling_active: bool | None = Field(default=None)
    b2b_params: ListResponseDataItemsItemB2bParams | None = Field(default=None)
    max_lead_time: int | None = Field(default=None)
    buy_box_price: int | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    is_seller_buy_box_winner: bool | None = Field(default=None)
    is_in_buy_box_challenge: bool | None = Field(default=None)
    min_selling_price_limit: int | None = Field(default=None)
    price_limit: int | None = Field(default=None)
    credit_increase_percentage: int | None = Field(default=None)
    product_selling_chanel: ListResponseDataItemsItemProductSellingChanel | None = Field(
        default=None
    )
    variant_selling_chanel: ListResponseDataItemsItemVariantSellingChanel | None = Field(
        default=None
    )
    is_in_incredible_promotion: bool | None = Field(default=None)
    is_in_periodic_promotion: bool | None = Field(default=None)
    is_in_promotion: bool | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    default_selling_chanel_code: int | None = Field(default=None)
    rating: float | None = Field(default=None)
    is_promotion_management_visible_for_seller: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    fulfilment_and_delivery_cost: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)
    seller_shipping_lead_time: int | None = Field(default=None)
    shipping_options: UpdateResponseDataShippingOptions | None = Field(default=None)


class UpdateB2bActivationResponse(APIResponseSchema):
    status: str
    data: UpdateB2bActivationResponseData


class ExportResponse(APIResponseSchema):
    status: str
    data: ExportResponseData


class GetGoldResponse(APIResponseSchema):
    status: int | str
    data: GetGoldResponseData


class UpdateGoldResponse(APIResponseSchema):
    status: str
    data: UpdateGoldResponseData


class CalculatePriceResponseData(APIResponseSchema):
    price: CalculatePriceResponseDataPrice | None = Field(default=None)


class UpdateActivationResponse(APIResponseSchema):
    status: str
    data: UpdateActivationResponseData


class GetB2bPricesResponseData(APIResponseSchema):
    active: bool | None = Field(default=None)
    buckets: list[GetB2bPricesResponseDataBucketsItem] | None = Field(default=None)


class UpdateB2bPricesRequest(RequestSchema):
    active: bool
    b2b_prices: list[UpdateB2bPricesRequestB2bPricesItem]


class GetSellerStockResponse(APIResponseSchema):
    status: int | str
    data: GetSellerStockResponseData


class UpdateSellerStockResponse(APIResponseSchema):
    status: str
    data: UpdateSellerStockResponseData


class UpdateSellingPriceResponse(APIResponseSchema):
    status: str
    data: UpdateSellingPriceResponseData


class ListResponseDataItemsItemThemeValuesItem(APIResponseSchema):
    theme_id: int | None = Field(
        default=None, validation_alias="themeId", serialization_alias="themeId"
    )
    theme_label: str | None = Field(
        default=None, validation_alias="themeLabel", serialization_alias="themeLabel"
    )
    active: bool | None = Field(default=None)
    theme_type: str | None = Field(
        default=None, validation_alias="themeType", serialization_alias="themeType"
    )
    theme_value: ListResponseDataItemsItemThemeValuesItemThemeValue | None = Field(
        default=None, validation_alias="themeValue", serialization_alias="themeValue"
    )


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    main_category_title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_url: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_moderation_status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    product_title: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    price_list: int | None = Field(default=None)
    market_price_last_update: str | None = Field(default=None)
    price_type: str | None = Field(default=None)
    selling_channel_site: str | None = Field(default=None)
    price_sale: int | None = Field(default=None)
    cash_selling_price: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    price_limit: int | None = Field(default=None)
    initial_limit: int | None = Field(default=None)
    credit_increase_percentage: float | int | None = Field(default=None)
    maximum_credit_increase_percentage: float | int | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    reservation: int | None = Field(default=None)
    left_consumer: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    allowed_count: int | None = Field(default=None)
    ovl_selling_active: bool | None = Field(default=None)
    created_at: str | ListResponseDataItemsItemCreatedAt1 | None = Field(default=None)
    pol_active: bool | None = Field(default=None)
    b2b_params: ListResponseDataItemsItemB2bParams | None = Field(default=None)
    max_lead_time: int | None = Field(default=None)
    buy_box_price: int | None = Field(default=None)
    buy_box_badge_label: str | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    is_sku_winner: bool | None = Field(default=None)
    sku_config: ListResponseDataItemsItemSkuConfig | None = Field(default=None)
    is_seller_buy_box_winner: bool | None = Field(default=None)
    is_in_buy_box_challenge: bool | None = Field(default=None)
    suppressed_until: str | None = Field(default=None)
    suppression_reason: str | None = Field(default=None)
    product_selling_chanel: ListResponseDataItemsItemProductSellingChanel | None = Field(
        default=None
    )
    variant_selling_chanel: ListResponseDataItemsItemVariantSellingChanel | None = Field(
        default=None
    )
    is_in_incredible_promotion: bool | None = Field(default=None)
    is_in_periodic_promotion: bool | None = Field(default=None)
    is_in_promotion: bool | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    default_selling_chanel_code: int | None = Field(default=None)
    rating: float | None = Field(default=None)
    is_promotion_management_visible_for_seller: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    fulfilment_and_delivery_cost: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)
    seller_shipping_lead_time: int | None = Field(default=None)
    theme_values: list[ListResponseDataItemsItemThemeValuesItem] | None = Field(default=None)
    shipping_options: ListResponseDataItemsItemShippingOptions | None = Field(default=None)


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class CalculatePriceResponse(APIResponseSchema):
    status: int | str
    data: CalculatePriceResponseData


class GetB2bPricesResponse(APIResponseSchema):
    status: int | str
    data: GetB2bPricesResponseData


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
    seller_id: int | None = Field(default=None)
    main_category_title: str | None = Field(default=None)
    category_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_url: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    product_moderation_status: str | None = Field(default=None)
    title: str | None = Field(default=None)
    product_title: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    price_list: int | None = Field(default=None)
    market_price_last_update: str | None = Field(default=None)
    price_type: str | None = Field(default=None)
    selling_channel_site: str | None = Field(default=None)
    price_sale: int | None = Field(default=None)
    cash_selling_price: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    price_limit: int | None = Field(default=None)
    initial_limit: int | None = Field(default=None)
    credit_increase_percentage: float | int | None = Field(default=None)
    maximum_credit_increase_percentage: float | int | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    warehouse_stock: int | None = Field(default=None)
    on_the_way_stock: int | None = Field(default=None)
    reservation: int | None = Field(default=None)
    left_consumer: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    allowed_count: int | None = Field(default=None)
    ovl_selling_active: bool | None = Field(default=None)
    created_at: str | ListResponseDataItemsItemCreatedAt1 | None = Field(default=None)
    pol_active: bool | None = Field(default=None)
    b2b_params: ListResponseDataItemsItemB2bParams | None = Field(default=None)
    max_lead_time: int | None = Field(default=None)
    buy_box_price: int | None = Field(default=None)
    buy_box_badge_label: str | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    is_sku_winner: bool | None = Field(default=None)
    sku_config: ListResponseDataItemsItemSkuConfig | None = Field(default=None)
    is_seller_buy_box_winner: bool | None = Field(default=None)
    is_in_buy_box_challenge: bool | None = Field(default=None)
    suppressed_until: str | None = Field(default=None)
    suppression_reason: str | None = Field(default=None)
    product_selling_chanel: ListResponseDataItemsItemProductSellingChanel | None = Field(
        default=None
    )
    variant_selling_chanel: ListResponseDataItemsItemVariantSellingChanel | None = Field(
        default=None
    )
    is_in_incredible_promotion: bool | None = Field(default=None)
    is_in_periodic_promotion: bool | None = Field(default=None)
    is_in_promotion: bool | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    shipping_nature_id: int | None = Field(default=None)
    default_selling_chanel_code: int | None = Field(default=None)
    rating: float | None = Field(default=None)
    is_promotion_management_visible_for_seller: bool | None = Field(default=None)
    is_archived: bool | None = Field(default=None)
    fulfilment_and_delivery_cost: int | None = Field(default=None)
    seller_reservation: int | None = Field(default=None)
    digikala_reservation: int | None = Field(default=None)
    seller_shipping_lead_time: int | None = Field(default=None)
    theme_values: list[ListResponseDataItemsItemThemeValuesItem] | None = Field(default=None)
    shipping_options: ListResponseDataItemsItemShippingOptions | None = Field(default=None)


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
    "ArchiveRequest",
    "ArchiveResponse",
    "CalculatePriceQuery",
    "CalculatePriceResponse",
    "CalculatePriceResponseData",
    "CalculatePriceResponseDataPrice",
    "ExportRequest",
    "ExportResponse",
    "ExportResponseData",
    "GetB2bPricesResponse",
    "GetB2bPricesResponseData",
    "GetB2bPricesResponseDataBucketsItem",
    "GetGoldResponse",
    "GetGoldResponseData",
    "GetResponse",
    "GetResponseData",
    "GetSellerStockResponse",
    "GetSellerStockResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemB2bParams",
    "ListResponseDataItemsItemCreatedAt1",
    "ListResponseDataItemsItemProductSellingChanel",
    "ListResponseDataItemsItemShippingOptions",
    "ListResponseDataItemsItemSkuConfig",
    "ListResponseDataItemsItemThemeValuesItem",
    "ListResponseDataItemsItemThemeValuesItemThemeValue",
    "ListResponseDataItemsItemThemeValuesItemThemeValueValue",
    "ListResponseDataItemsItemVariantSellingChanel",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "UpdateActivationRequest",
    "UpdateActivationResponse",
    "UpdateActivationResponseData",
    "UpdateB2bActivationRequest",
    "UpdateB2bActivationResponse",
    "UpdateB2bActivationResponseData",
    "UpdateB2bPricesRequest",
    "UpdateB2bPricesRequestB2bPricesItem",
    "UpdateB2bPricesResponse",
    "UpdateGoldRequest",
    "UpdateGoldResponse",
    "UpdateGoldResponseData",
    "UpdateRequest",
    "UpdateResponse",
    "UpdateResponseData",
    "UpdateResponseDataShippingOptions",
    "UpdateSellerStockRequest",
    "UpdateSellerStockResponse",
    "UpdateSellerStockResponseData",
    "UpdateSellingPriceRequest",
    "UpdateSellingPriceResponse",
    "UpdateSellingPriceResponseData",
]
