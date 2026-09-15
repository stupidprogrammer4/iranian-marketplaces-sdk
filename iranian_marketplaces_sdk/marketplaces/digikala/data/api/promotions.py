"""Digikala promotions: request and response models."""

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
    sort: Literal["promotion_id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_nature: list[str] | None = Field(
        default=None, validation_alias="search[nature]", serialization_alias="search[nature]"
    )
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_search_keyword: str | None = Field(
        default=None,
        validation_alias="search[searchKeyword]",
        serialization_alias="search[searchKeyword]",
    )
    search_start_at: str | None = Field(
        default=None, validation_alias="search[startAt]", serialization_alias="search[startAt]"
    )
    search_end_at: str | None = Field(
        default=None, validation_alias="search[endAt]", serialization_alias="search[endAt]"
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


class ListResponseDataItemsItemCategoriesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)


class ListResponseDataItemsItemVariantsStats(APIResponseSchema):
    approved: int | None = Field(default=None)
    draft: int | None = Field(default=None)
    rejected: int | None = Field(default=None)


class ListResponseDataItemsItemBadge(APIResponseSchema):
    icon: str | None = Field(default=None)
    title: str | None = Field(default=None)
    color: str | None = Field(default=None)


class ConfigsResponseData(APIResponseSchema):
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    title: str | None = Field(default=None)
    dashboard_landing_banner_section: list[JsonValue] | None = Field(default=None)
    smart_discount_landing_banner_section: list[JsonValue] | None = Field(default=None)
    landing_svg_image_url: str | None = Field(default=None)
    variants_count: int | None = Field(default=None)
    sellers_count: int | None = Field(default=None)
    extra_data: ObjectMap[JsonValue] | None = Field(default=None)


class RecommendedQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)


class RecommendedResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class RecommendedResponseDataItemsItemRecommendedPromotionsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    badge_icon: str | None = Field(default=None)
    badge_title: str | None = Field(default=None)
    badge_color: str | None = Field(default=None)
    cmp_link: str | None = Field(default=None)
    is_extra: bool | None = Field(default=None)


class EligibleQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id", "start_at", "end_at", "join_deadline"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_nature: list[str] | None = Field(
        default=None, validation_alias="search[nature]", serialization_alias="search[nature]"
    )
    search_label_ids: list[int] | None = Field(
        default=None, validation_alias="search[label_ids]", serialization_alias="search[label_ids]"
    )
    search_exclude_joined: bool | None = Field(
        default=None,
        validation_alias="search[excludeJoined]",
        serialization_alias="search[excludeJoined]",
    )
    search_title: str | None = Field(
        default=None, validation_alias="search[title]", serialization_alias="search[title]"
    )
    search_start_at: str | None = Field(
        default=None, validation_alias="search[startAt]", serialization_alias="search[startAt]"
    )
    search_end_at: str | None = Field(
        default=None, validation_alias="search[endAt]", serialization_alias="search[endAt]"
    )
    search_last_seconds: bool | None = Field(
        default=None,
        validation_alias="search[lastSeconds]",
        serialization_alias="search[lastSeconds]",
    )


class EligibleResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class EligibleResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class EligibleResponseDataItemsItem(APIResponseSchema):
    badge_color: None = Field(default=None)
    badge_icon: None = Field(default=None)
    badge_title: None = Field(default=None)
    categories: list[int] | None = Field(default=None)
    cmp_link: str | None = Field(default=None)
    conditions: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    has_already_joined: bool | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    id: int | None = Field(default=None)
    incentive: bool | None = Field(default=None)
    join_deadline: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    number_of_potential_variants: int | None = Field(default=None)
    participants: int | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    promotion_min_discount: int | None = Field(default=None)
    start_at: str | None = Field(default=None)
    supply_categories: list[int] | None = Field(default=None)
    title: str | None = Field(default=None)


class MinimumDiscountsRequest(RequestSchema):
    variant_ids: list[int]
    promotion_nature: str


class MinimumDiscountsResponseData(APIResponseSchema):
    category_id: int | None = Field(default=None)
    min_discount: float | None = Field(default=None)


class UnjoinedQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_nature: list[str] | None = Field(
        default=None, validation_alias="search[nature]", serialization_alias="search[nature]"
    )


class UnjoinedResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    badge_title: str | None = Field(default=None)
    badge_color: str | None = Field(default=None)
    badge_icon: str | None = Field(default=None)
    cmp_link: str | None = Field(default=None)
    conditions: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    categories: list[str] | None = Field(default=None)
    supply_categories: list[str] | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    join_deadline: str | None = Field(default=None)
    number_of_potential_variants: int | None = Field(default=None)
    participants: int | None = Field(default=None)
    has_already_joined: bool | None = Field(default=None)
    promotion_min_discount: int | None = Field(default=None)
    incentive: bool | None = Field(default=None)


class CurrentForVariantQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["promotion_id"] | None = Field(default=None)
    order: str | None = Field(default=None)


class CurrentForVariantResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class CurrentForVariantResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class CurrentForVariantResponseDataItemsItemItemStartAt(APIResponseSchema):
    date: str | None = Field(default=None)
    timezone_type: int | None = Field(default=None)
    timezone: str | None = Field(default=None)


class CurrentForVariantResponseDataItemsItemItemEndAt(APIResponseSchema):
    date: str | None = Field(default=None)
    timezone_type: int | None = Field(default=None)
    timezone: str | None = Field(default=None)


class VariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_promotion_status: (
        Literal[
            "d",
            "r",
            "a",
            "f",
            "t",
            ",",
            "p",
            "e",
            "n",
            "d",
            "i",
            "n",
            "g",
            ",",
            "a",
            "p",
            "p",
            "r",
            "o",
            "v",
            "e",
            "d",
            ",",
            "r",
            "e",
            "j",
            "e",
            "c",
            "t",
            "e",
            "d",
            ",",
            "a",
            "c",
            "t",
            "i",
            "v",
            "e",
            ",",
            "e",
            "n",
            "d",
            "e",
            "d",
        ]
        | None
    ) = Field(
        default=None,
        validation_alias="search[promotionStatus]",
        serialization_alias="search[promotionStatus]",
    )
    search_promotion_variant_status: (
        Literal[
            "d",
            "r",
            "a",
            "f",
            "t",
            ",",
            "r",
            "e",
            "j",
            "e",
            "c",
            "t",
            "e",
            "d",
            ",",
            "a",
            "p",
            "p",
            "r",
            "o",
            "v",
            "e",
            "d",
            ",",
            "p",
            "a",
            "r",
            "t",
            "i",
            "a",
            "l",
            "l",
            "y",
            "_",
            "a",
            "p",
            "p",
            "r",
            "o",
            "v",
            "e",
            "d",
            ",",
            "p",
            "a",
            "r",
            "t",
            "i",
            "a",
            "l",
            "l",
            "y",
            "_",
            "r",
            "e",
            "j",
            "e",
            "c",
            "t",
            "e",
            "d",
        ]
        | None
    ) = Field(
        default=None,
        validation_alias="search[promotionVariantStatus]",
        serialization_alias="search[promotionVariantStatus]",
    )
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )


class VariantsResponseDataItemsItemPromotionVariantsItemPromotion(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    status: str | None = Field(default=None)
    tag: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    commission_discount: bool | None = Field(default=None)


class GetVariantQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)


class GetVariantResponseDataItemsItemPromotionVariantsItemPromotion(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    status: str | None = Field(default=None)
    tag: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    commission_discount: bool | None = Field(default=None)


class RejectionReasonQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_promotion_variant_id: int | None = Field(
        default=None,
        validation_alias="search[promotion_variant_id]",
        serialization_alias="search[promotion_variant_id]",
    )


class RejectionReasonResponseDataItemsItemResultItem(APIResponseSchema):
    title: str | None = Field(default=None)
    priority: int | None = Field(default=None)


class GetResponseDataConditionSchema(APIResponseSchema):
    promotion_id: int | None = Field(default=None)
    min_discount_percent: str | None = Field(default=None)
    max_discount_percent: str | None = Field(default=None)
    max_price: str | None = Field(default=None)
    min_price: str | None = Field(default=None)
    min_discount_amount: str | None = Field(default=None)


class GetResponseDataStats(APIResponseSchema):
    approved: int | None = Field(default=None)
    draft: int | None = Field(default=None)
    rejected: int | None = Field(default=None)
    auto_joined_variants_count: int | None = Field(default=None)


class ListVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_selected_ids: str | None = Field(
        default=None,
        validation_alias="search[selectedIds]",
        serialization_alias="search[selectedIds]",
    )
    search_search_keyword: str | None = Field(
        default=None,
        validation_alias="search[searchKeyword]",
        serialization_alias="search[searchKeyword]",
    )
    search_status: str | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_only_auto_joined: str | None = Field(
        default=None,
        validation_alias="search[onlyAutoJoined]",
        serialization_alias="search[onlyAutoJoined]",
    )


class ListVariantsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    parent_id: int | None = Field(default=None)
    image: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_price_in_promotion: int | None = Field(default=None)
    min_sku_selling_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    commission: int | None = Field(default=None)
    selling_stock: int | None = Field(default=None)
    promotion_limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    status: str | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_sales_count: int | None = Field(default=None)
    is_highly_demanded_product: bool | None = Field(default=None)
    already_exists_in_incredible_promotion: bool | None = Field(default=None)
    already_exist_in_same_promotion: bool | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    rrp_price: int | None = Field(default=None)
    is_auto_joined: bool | None = Field(default=None)
    incentive: int | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    cash_selling_price: int | None = Field(default=None)
    cash_rrp_price: int | None = Field(default=None)
    cash_discount: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    credit_rrp_price: int | None = Field(default=None)
    credit_discount: int | None = Field(default=None)
    credit_increase_percentage: float | int | None = Field(default=None)
    category_price_configs: list[JsonValue] | None = Field(default=None)
    is_extra: bool | None = Field(default=None)
    extra_offer_min_item: int | None = Field(default=None)
    extra_offer_min_nmv: int | None = Field(default=None)


class AddVariantsRequest(RequestSchema):
    data: list[JsonValue]


class AddVariantsResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateVariantsRequest(RequestSchema):
    data: list[JsonValue]


class UpdateVariantsResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class DeleteVariantsRequest(RequestSchema):
    ids: list[int]


class DeleteVariantsResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class RejectedVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)


class RejectedVariantsResponseDataItemsItemVariantsItem(APIResponseSchema):
    promotion_variant_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    variant_title: str | None = Field(default=None)
    promotion_price: int | None = Field(default=None)


class AddVariantsBatchRequest(RequestSchema):
    data: list[JsonValue]


class AddVariantsBatchResponse(APIResponseSchema):
    status: str
    data: AddVariantsResponseData


class UpdateVariantsBatchRequest(RequestSchema):
    ids: list[int]
    discount: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    price_limit: int | None = Field(default=None)


class UpdateVariantsBatchResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class EligibleVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: str | None = Field(default=None)
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )
    search_only_buy_box_winner: bool | None = Field(
        default=None,
        validation_alias="search[onlyBuyBoxWinner]",
        serialization_alias="search[onlyBuyBoxWinner]",
    )
    search_categories: str | None = Field(
        default=None,
        validation_alias="search[categories]",
        serialization_alias="search[categories]",
    )
    search_highly_demanded: bool | None = Field(
        default=None,
        validation_alias="search[highlyDemanded]",
        serialization_alias="search[highlyDemanded]",
    )


class EligibleVariantsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    image: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_price_in_promotion: int | None = Field(default=None)
    min_sku_selling_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    commission: int | None = Field(default=None)
    selling_stock: int | None = Field(default=None)
    promotion_limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    status: str | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_sales_count: int | None = Field(default=None)
    is_highly_demanded_product: bool | None = Field(default=None)
    already_exist_in_incredible_promotion: bool | None = Field(default=None)
    already_exist_in_same_promotion: bool | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    product_type: str | None = Field(default=None)


class EligibleVariantsV2Query(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: str | None = Field(default=None)
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )
    search_only_buy_box_winner: bool | None = Field(
        default=None,
        validation_alias="search[onlyBuyBoxWinner]",
        serialization_alias="search[onlyBuyBoxWinner]",
    )
    search_categories: str | None = Field(
        default=None,
        validation_alias="search[categories]",
        serialization_alias="search[categories]",
    )
    search_highly_demanded: bool | None = Field(
        default=None,
        validation_alias="search[highlyDemanded]",
        serialization_alias="search[highlyDemanded]",
    )
    search_is_hero: bool | None = Field(
        default=None, validation_alias="search[isHero]", serialization_alias="search[isHero]"
    )


class EligibleVariantsV2ResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    image_link: str | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_sales_count: int | None = Field(default=None)
    is_highly_demanded_product: bool | None = Field(default=None)
    already_exists_in_incredible_promotion: bool | None = Field(default=None)
    already_exist_in_same_promotion: bool | None = Field(default=None)
    incentive: bool | None = Field(default=None)
    is_hero: bool | None = Field(default=None)
    category_name: str | None = Field(default=None)
    extra_offer_eligible: bool | None = Field(default=None)


class VariantsToJoinQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_variant_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[variant_ids]",
        serialization_alias="search[variant_ids]",
    )
    search_promotion_id: int | None = Field(
        default=None,
        validation_alias="search[promotion_id]",
        serialization_alias="search[promotion_id]",
    )


class VariantsToJoinResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    selling_stock: int | None = Field(default=None)
    image_link: str | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_price_in_promotion: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    commission: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    is_hero: bool | None = Field(default=None)
    extra_offer_min_item: int | None = Field(default=None)
    extra_offer_min_nmv: int | None = Field(default=None)


class CommissionDiscountResponseDataPromotion(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    status: str | None = Field(default=None)


class CommissionDiscountResponseDataVariant(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)


class ImportExcelRequest(RequestSchema):
    file_id: int


class ImportExcelResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    import_request_id: int | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    nature: str | None = Field(default=None)
    categories: list[ListResponseDataItemsItemCategoriesItem] | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    status: str | None = Field(default=None)
    total_views: int | None = Field(default=None)
    total_sales: int | None = Field(default=None)
    auto_joined_variants_count: int | None = Field(default=None)
    variants_stats: ListResponseDataItemsItemVariantsStats | None = Field(default=None)
    badge: ListResponseDataItemsItemBadge | None = Field(default=None)
    incentive: int | None = Field(default=None)
    is_promotion_report_active: bool | None = Field(default=None)
    is_extra: bool | None = Field(default=None)


class ConfigsResponse(APIResponseSchema):
    status: int | str
    data: ConfigsResponseData


class RecommendedResponseDataItemsItem(APIResponseSchema):
    eligible_promotions_count: int | None = Field(default=None)
    eligible_product_variants_count: int | None = Field(default=None)
    recommended_promotions: (
        list[RecommendedResponseDataItemsItemRecommendedPromotionsItem] | None
    ) = Field(default=None)


class EligibleResponseData(APIResponseSchema):
    sort_data: EligibleResponseDataSortData | None = Field(default=None)
    pager: EligibleResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class MinimumDiscountsResponse(APIResponseSchema):
    status: str
    data: MinimumDiscountsResponseData


class UnjoinedResponseData(APIResponseSchema):
    sort_data: RecommendedResponseDataSortData | None = Field(default=None)
    pager: EligibleResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[UnjoinedResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CurrentForVariantResponseDataItemsItemItem(APIResponseSchema):
    promotion_id: int | None = Field(default=None)
    variant_status: str | None = Field(default=None)
    promotion_title: str | None = Field(default=None)
    promotion_type: str | None = Field(default=None)
    start_at: CurrentForVariantResponseDataItemsItemItemStartAt | None = Field(default=None)
    end_at: CurrentForVariantResponseDataItemsItemItemEndAt | None = Field(default=None)
    promotion_rrp_price: int | None = Field(default=None)
    promotion_selling_price: int | None = Field(default=None)


class VariantsResponseDataItemsItemPromotionVariantsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    status: str | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    crossed_price: int | None = Field(default=None)
    promotion_limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    promotion: VariantsResponseDataItemsItemPromotionVariantsItemPromotion | None = Field(
        default=None
    )


class GetVariantResponseDataItemsItemPromotionVariantsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    status: str | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    crossed_price: int | None = Field(default=None)
    promotion_limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    promotion: GetVariantResponseDataItemsItemPromotionVariantsItemPromotion | None = Field(
        default=None
    )


class RejectionReasonResponseDataItemsItem(APIResponseSchema):
    promotion_variant_id: int | None = Field(default=None)
    result: list[RejectionReasonResponseDataItemsItemResultItem] | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    cmp_link: str | None = Field(default=None)
    status: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    join_deadline: str | None = Field(default=None)
    is_join_active: bool | None = Field(default=None)
    is_ended: bool | None = Field(default=None)
    type: str | None = Field(default=None)
    tag: str | None = Field(default=None)
    nature: str | None = Field(default=None)
    tag_label: str | None = Field(default=None)
    campaign_details: list[JsonValue] | None = Field(default=None)
    conditions: list[str] | None = Field(default=None)
    condition_schema: GetResponseDataConditionSchema | None = Field(default=None)
    filters: list[str] | None = Field(default=None)
    categories: list[JsonValue] | None = Field(default=None)
    supply_categories: list[JsonValue] | None = Field(default=None)
    commission_discount: str | None = Field(default=None)
    is_extra: bool | None = Field(default=None)
    remaining_quota: int | None = Field(default=None)
    stats: GetResponseDataStats | None = Field(default=None)


class ListVariantsResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class AddVariantsResponse(APIResponseSchema):
    status: str
    data: AddVariantsResponseData


class UpdateVariantsResponse(APIResponseSchema):
    status: str
    data: UpdateVariantsResponseData


class DeleteVariantsResponse(APIResponseSchema):
    status: str
    data: DeleteVariantsResponseData


class RejectedVariantsResponseDataItemsItem(APIResponseSchema):
    image_link: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_title: str | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_sales_count: int | None = Field(default=None)
    variants: list[RejectedVariantsResponseDataItemsItemVariantsItem] | None = Field(default=None)


class UpdateVariantsBatchResponse(APIResponseSchema):
    status: str
    data: UpdateVariantsBatchResponseData


class EligibleVariantsResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class EligibleVariantsV2ResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleVariantsV2ResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class VariantsToJoinResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[VariantsToJoinResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CommissionDiscountResponseData(APIResponseSchema):
    has_commission_discount: bool | None = Field(default=None)
    commission_discount_percent: int | None = Field(default=None)
    commission_discount_amount: int | None = Field(default=None)
    original_commission: int | None = Field(default=None)
    final_commission: int | None = Field(default=None)
    promotion: CommissionDiscountResponseDataPromotion | None = Field(default=None)
    variant: CommissionDiscountResponseDataVariant | None = Field(default=None)


class ImportExcelResponse(APIResponseSchema):
    status: str
    data: ImportExcelResponseData


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class RecommendedResponseData(APIResponseSchema):
    sort_data: RecommendedResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[RecommendedResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class EligibleResponse(APIResponseSchema):
    status: str
    data: EligibleResponseData


class UnjoinedResponse(APIResponseSchema):
    status: str
    data: UnjoinedResponseData


class CurrentForVariantResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[list[CurrentForVariantResponseDataItemsItemItem]] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class VariantsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    category_order_limit: list[int] | None = Field(default=None)
    image: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    promotion_variants: list[VariantsResponseDataItemsItemPromotionVariantsItem] | None = Field(
        default=None
    )
    promotion_variants_count: int | None = Field(default=None)
    incentive: bool | None = Field(default=None)


class GetVariantResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    category_order_limit: list[int] | None = Field(default=None)
    image: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    promotion_variants: list[GetVariantResponseDataItemsItemPromotionVariantsItem] | None = Field(
        default=None
    )


class RejectionReasonResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[RejectionReasonResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class ListVariantsResponse(APIResponseSchema):
    status: str
    data: ListVariantsResponseData


class RejectedVariantsResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[RejectedVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class EligibleVariantsResponse(APIResponseSchema):
    status: str
    data: EligibleVariantsResponseData


class EligibleVariantsV2Response(APIResponseSchema):
    status: str
    data: EligibleVariantsV2ResponseData


class VariantsToJoinResponse(APIResponseSchema):
    status: str
    data: VariantsToJoinResponseData


class CommissionDiscountResponse(APIResponseSchema):
    status: int | str
    data: CommissionDiscountResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class RecommendedResponse(APIResponseSchema):
    status: str
    data: RecommendedResponseData


class CurrentForVariantResponse(APIResponseSchema):
    status: str
    data: CurrentForVariantResponseData


class VariantsResponseData(APIResponseSchema):
    sort_data: RecommendedResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[VariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetVariantResponseData(APIResponseSchema):
    sort_data: CurrentForVariantResponseDataSortData | None = Field(default=None)
    pager: CurrentForVariantResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetVariantResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class RejectionReasonResponse(APIResponseSchema):
    status: str
    data: RejectionReasonResponseData


class RejectedVariantsResponse(APIResponseSchema):
    status: str
    data: RejectedVariantsResponseData


class VariantsResponse(APIResponseSchema):
    status: str
    data: VariantsResponseData


class GetVariantResponse(APIResponseSchema):
    status: str
    data: GetVariantResponseData


__all__ = [
    "AddVariantsBatchRequest",
    "AddVariantsBatchResponse",
    "AddVariantsRequest",
    "AddVariantsResponse",
    "AddVariantsResponseData",
    "CommissionDiscountResponse",
    "CommissionDiscountResponseData",
    "CommissionDiscountResponseDataPromotion",
    "CommissionDiscountResponseDataVariant",
    "ConfigsResponse",
    "ConfigsResponseData",
    "CurrentForVariantQuery",
    "CurrentForVariantResponse",
    "CurrentForVariantResponseData",
    "CurrentForVariantResponseDataItemsItemItem",
    "CurrentForVariantResponseDataItemsItemItemEndAt",
    "CurrentForVariantResponseDataItemsItemItemStartAt",
    "CurrentForVariantResponseDataPager",
    "CurrentForVariantResponseDataSortData",
    "DeleteVariantsRequest",
    "DeleteVariantsResponse",
    "DeleteVariantsResponseData",
    "EligibleQuery",
    "EligibleResponse",
    "EligibleResponseData",
    "EligibleResponseDataItemsItem",
    "EligibleResponseDataPager",
    "EligibleResponseDataSortData",
    "EligibleVariantsQuery",
    "EligibleVariantsResponse",
    "EligibleVariantsResponseData",
    "EligibleVariantsResponseDataItemsItem",
    "EligibleVariantsV2Query",
    "EligibleVariantsV2Response",
    "EligibleVariantsV2ResponseData",
    "EligibleVariantsV2ResponseDataItemsItem",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataConditionSchema",
    "GetResponseDataStats",
    "GetVariantQuery",
    "GetVariantResponse",
    "GetVariantResponseData",
    "GetVariantResponseDataItemsItem",
    "GetVariantResponseDataItemsItemPromotionVariantsItem",
    "GetVariantResponseDataItemsItemPromotionVariantsItemPromotion",
    "ImportExcelRequest",
    "ImportExcelResponse",
    "ImportExcelResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemBadge",
    "ListResponseDataItemsItemCategoriesItem",
    "ListResponseDataItemsItemVariantsStats",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "ListVariantsQuery",
    "ListVariantsResponse",
    "ListVariantsResponseData",
    "ListVariantsResponseDataItemsItem",
    "MinimumDiscountsRequest",
    "MinimumDiscountsResponse",
    "MinimumDiscountsResponseData",
    "RecommendedQuery",
    "RecommendedResponse",
    "RecommendedResponseData",
    "RecommendedResponseDataItemsItem",
    "RecommendedResponseDataItemsItemRecommendedPromotionsItem",
    "RecommendedResponseDataSortData",
    "RejectedVariantsQuery",
    "RejectedVariantsResponse",
    "RejectedVariantsResponseData",
    "RejectedVariantsResponseDataItemsItem",
    "RejectedVariantsResponseDataItemsItemVariantsItem",
    "RejectionReasonQuery",
    "RejectionReasonResponse",
    "RejectionReasonResponseData",
    "RejectionReasonResponseDataItemsItem",
    "RejectionReasonResponseDataItemsItemResultItem",
    "UnjoinedQuery",
    "UnjoinedResponse",
    "UnjoinedResponseData",
    "UnjoinedResponseDataItemsItem",
    "UpdateVariantsBatchRequest",
    "UpdateVariantsBatchResponse",
    "UpdateVariantsBatchResponseData",
    "UpdateVariantsRequest",
    "UpdateVariantsResponse",
    "UpdateVariantsResponseData",
    "VariantsQuery",
    "VariantsResponse",
    "VariantsResponseData",
    "VariantsResponseDataItemsItem",
    "VariantsResponseDataItemsItemPromotionVariantsItem",
    "VariantsResponseDataItemsItemPromotionVariantsItemPromotion",
    "VariantsToJoinQuery",
    "VariantsToJoinResponse",
    "VariantsToJoinResponseData",
    "VariantsToJoinResponseDataItemsItem",
]
