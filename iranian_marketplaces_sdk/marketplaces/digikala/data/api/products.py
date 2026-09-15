"""Digikala products: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class SearchQuery(QuerySchema):
    search_keyword: str = Field(
        validation_alias="search[keyword]", serialization_alias="search[keyword]"
    )
    search_categories: str | int | None = Field(
        default=None,
        validation_alias="search[categories]",
        serialization_alias="search[categories]",
    )
    search_brands: str | int | None = Field(
        default=None, validation_alias="search[brands]", serialization_alias="search[brands]"
    )
    search_types: str | int | None = Field(
        default=None, validation_alias="search[types]", serialization_alias="search[types]"
    )
    search_color_palettes: str | int | None = Field(
        default=None,
        validation_alias="search[colorPalettes]",
        serialization_alias="search[colorPalettes]",
    )
    search_statuses: Literal["marketable", "coming_soon", "stop_production"] | None = Field(
        default=None, validation_alias="search[statuses]", serialization_alias="search[statuses]"
    )
    search_fake: bool | None = Field(
        default=None, validation_alias="search[fake]", serialization_alias="search[fake]"
    )


class SearchResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class SearchResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class SearchResponseDataItemsItemCommission(APIResponseSchema):
    can_sell: bool | None = Field(
        default=None, validation_alias="canSell", serialization_alias="canSell"
    )
    type: str | None = Field(default=None)
    commission: float | None = Field(default=None)
    message: list[str] | None = Field(default=None)


class SearchResponseDataItemsItemPriceType(APIResponseSchema):
    recommended: str | None = Field(default=None)


class SuggestionsQuery(QuerySchema):
    search_keyword: str | None = Field(
        default=None, validation_alias="search[keyword]", serialization_alias="search[keyword]"
    )


class SuggestionsResponseDataItemsItemCategoriesItemCategory(APIResponseSchema):
    id: int | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    code: str | None = Field(default=None)


class SuggestionsResponseDataItemsItemAutoCompleteItem(APIResponseSchema):
    keyword: str | None = Field(default=None)


class SellerPermissionResponseDataCommission(APIResponseSchema):
    can_sell: bool | None = Field(
        default=None, validation_alias="canSell", serialization_alias="canSell"
    )
    commission: float | None = Field(default=None)


class SellerPermissionResponseDataFulfillmentAndDeliveryCost(APIResponseSchema):
    factor: int | None = Field(default=None)
    minimum_cost: int | None = Field(default=None)
    maximum_cost: int | None = Field(default=None)


class SellerPermissionResponseDataCategoryThemesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    label: str | None = Field(default=None)
    theme_type: str | None = Field(
        default=None, validation_alias="themeType", serialization_alias="themeType"
    )


class SellerPermissionResponseDataProductDimension(APIResponseSchema):
    width: int | None = Field(default=None)
    length: int | None = Field(default=None)
    height: int | None = Field(default=None)
    weight: int | None = Field(default=None)


class SearchCategoriesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class SearchCategoriesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class SearchCategoriesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    text: str | None = Field(default=None)
    leaf: bool | None = Field(default=None)


class ValidateCategoryResponseDataBindBrandsItem(APIResponseSchema):
    id: str | int | None = Field(default=None)
    text: str | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    logo_id: str | None = Field(default=None)


class ValidateCategoryResponseDataBindCategoryProductTypesItem(APIResponseSchema):
    value: str | None = Field(default=None)
    text: str | None = Field(default=None)


class ValidateCategoryResponseDataBindProductClassesItem(APIResponseSchema):
    value: str | None = Field(default=None)
    text: str | None = Field(default=None)


class ValidateCategoryResponseDataBindGuidelineCategorySelection(APIResponseSchema):
    video: str | None = Field(default=None)
    short_description: str | None = Field(default=None)


class ValidateCategoryResponseDataBindGuidelineAttributesItemsItem(APIResponseSchema):
    title: str | None = Field(default=None)
    content: str | None = Field(default=None)


class ValidateCategoryResponseDataBindGuidelineProductInfoItemsItem(APIResponseSchema):
    title: str | None = Field(default=None)
    content: str | None = Field(default=None)


class ValidateCategoryResponseDataBindGuidelineMediaItemsItem(APIResponseSchema):
    title: str | None = Field(default=None)
    content: str | None = Field(default=None)


class ValidateCategoryResponseDataBindCategoryData(APIResponseSchema):
    category_theme: str | None = Field(
        default=None, validation_alias="categoryTheme", serialization_alias="categoryTheme"
    )
    category_theme_translated: str | None = Field(
        default=None,
        validation_alias="categoryThemeTranslated",
        serialization_alias="categoryThemeTranslated",
    )
    category_title: str | None = Field(
        default=None, validation_alias="categoryTitle", serialization_alias="categoryTitle"
    )


class ValidateCategoryResponseDataBindDimensionConfigLength(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ValidateCategoryResponseDataBindDimensionConfigWidth(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ValidateCategoryResponseDataBindDimensionConfigHeight(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ValidateCategoryResponseDataBindDimensionConfigWeight(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ValidateCategoryResponseDataBindGeneralMefaGeneralMefaId(APIResponseSchema):
    value: int | None = Field(default=None)
    text: str | None = Field(default=None)
    general_id: str | int | None = Field(default=None)


class ValidateCategoryResponseDataBindStatusesItem(APIResponseSchema):
    value: str | None = Field(default=None)
    text: str | None = Field(default=None)
    selected: bool | None = Field(default=None)


class ValidateCategoryResponseDataBindPlatformsItem(APIResponseSchema):
    value: str | None = Field(default=None)
    text: str | None = Field(default=None)
    selected: bool | None = Field(default=None)


class ValidateDetailsRequest(RequestSchema):
    category_id: int
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int
    product_type_ids: list[int] | None = Field(default=None)
    color_id: int | None = Field(default=None)
    is_iranian: bool
    product_classes: list[int] | None = Field(default=None)
    fake: bool | None = Field(default=None)
    fake_reasons: list[int] | None = Field(default=None)
    general_mefa_id: str | None = Field(default=None)
    exclusive_mefa_id: str | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    description: str | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    draft_product_id: int | None = Field(default=None)


class ValidateDetailsResponseDataBind(APIResponseSchema):
    vat: int | None = Field(default=None)
    product_nature: str | None = Field(default=None)
    sensitivity: str | None = Field(default=None)
    status: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    active_digistyle: bool | None = Field(default=None)
    product_type: str | None = Field(default=None)
    site: str | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    fake_reasons: list[str] | None = Field(default=None)
    category_id: int | None = Field(default=None)
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    product_type_ids: list[int] | None = Field(default=None)
    is_iranian: bool | None = Field(default=None)
    fake: bool | None = Field(default=None)
    general_mefa_id: int | None = Field(default=None)
    exclusive_mefa_id: str | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    description: str | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)


class CountDraftsResponseData(APIResponseSchema):
    number_of_drafts: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsCategory(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsBrand(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsType(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsModel(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsOriginality(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsDivision(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsMefa(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsDescription(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsAdvantage(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsDisadvantage(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsAttribute1597(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsTitleFa(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsTitleEn(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetDraftResponseDataScoreScoreDetailsPhoto(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class GetAutoTitleResponseDataHint(APIResponseSchema):
    hint_fa: str | None = Field(default=None)
    hint_en: str | None = Field(default=None)


class SaveAutoTitleRequest(RequestSchema):
    draft_product_id: int
    title_fa: str
    title_en: str | None = Field(default=None)
    description: str | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)


class SaveAutoTitleResponseDataData(APIResponseSchema):
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    suggested_title_fa: str | None = Field(default=None)
    suggested_title_en: str | None = Field(default=None)
    url_code: str | None = Field(default=None)


class GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue0(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    code: str | None = Field(default=None)
    postfix: str | None = Field(default=None)
    unit: str | None = Field(default=None)
    type: str | None = Field(default=None)
    required: bool | None = Field(default=None)
    value: JsonValue = Field(default=None)
    values: list[JsonValue] | None = Field(default=None)
    hint: str | None = Field(default=None)


class GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1ValuesValue0(
    APIResponseSchema
):
    text: str | None = Field(default=None)
    code: str | int | None = Field(default=None)
    selected: bool | None = Field(default=None)


class SaveAttributesRequestAttributesItemItem(RequestSchema):
    id: int | None = Field(default=None)
    value: JsonValue = Field(default=None)


class UploadBrandLogoResponseDataData(APIResponseSchema):
    id: str | None = Field(default=None)
    url: str | None = Field(default=None)
    temp_file: bool | None = Field(
        default=None, validation_alias="tempFile", serialization_alias="tempFile"
    )


class GenerateImageRequest(RequestSchema):
    image_id: str
    is_main: bool


class GenerateImageResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )
    data: list[str] | None = Field(default=None)


class SaveRequestPhotosDetailImagesItem(RequestSchema):
    encrypted_id: str | None = Field(default=None)
    active: bool | None = Field(default=None)


class SaveResponseDataData(APIResponseSchema):
    product_id: int | None = Field(default=None)


class AssignRequest(RequestSchema):
    product_id: int = Field(validation_alias="productId", serialization_alias="productId")


class AssignResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )


class RequestBrandRequest(RequestSchema):
    brand_origin: str
    description: str
    logo_id: str
    name_en: str
    name_fa: str
    iranian_registration_url: str | None = Field(default=None)
    category_id: str


class RequestBrandResponseDataData(APIResponseSchema):
    id: int | None = Field(default=None)


class ListBrandsQuery(QuerySchema):
    search_title_fa: str | None = Field(
        default=None, validation_alias="search[title_fa]", serialization_alias="search[title_fa]"
    )
    search_title_en: str | None = Field(
        default=None, validation_alias="search[title_en]", serialization_alias="search[title_en]"
    )


class ListBrandsResponseDataItemsItemValue(APIResponseSchema):
    id: int | None = Field(default=None)
    keyword: str | None = Field(default=None)
    name_fa: str | None = Field(default=None)
    name_en: str | None = Field(default=None)
    description: str | None = Field(default=None)
    is_iranian: bool | None = Field(default=None)
    logo: str | None = Field(default=None)


class ListDraftsQuery(QuerySchema):
    search_brand_ids: list[int] | None = Field(
        default=None, validation_alias="search[brand_ids]", serialization_alias="search[brand_ids]"
    )
    search_category_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[category_ids]",
        serialization_alias="search[category_ids]",
    )
    search_near_expiration: bool | None = Field(
        default=None,
        validation_alias="search[near_expiration]",
        serialization_alias="search[near_expiration]",
    )


class ListSellerQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_multi_search: str | None = Field(
        default=None,
        validation_alias="search[multi_search]",
        serialization_alias="search[multi_search]",
    )
    search_category_id: str | int | None = Field(
        default=None,
        validation_alias="search[category_id]",
        serialization_alias="search[category_id]",
    )
    search_brand_id: str | int | None = Field(
        default=None, validation_alias="search[brand_id]", serialization_alias="search[brand_id]"
    )
    search_moderation_status: (
        Literal[
            "draft",
            "in_review",
            "waiting_for_confirm",
            "edit_after_approved",
            "approved",
            "in_review_after_approved",
            "removed",
            "duplicate",
        ]
        | None
    ) = Field(
        default=None,
        validation_alias="search[moderation_status]",
        serialization_alias="search[moderation_status]",
    )
    search_fake_status: Literal["fake", "real"] | None = Field(
        default=None,
        validation_alias="search[fake_status]",
        serialization_alias="search[fake_status]",
    )


class ListSellerResponseDataItemsItemModerationStatus(APIResponseSchema):
    title: str | None = Field(default=None)
    status: str | None = Field(default=None)


class ScoreResponseDataScore(APIResponseSchema):
    max: int | None = Field(default=None)
    current: int | None = Field(default=None)


class ScoreResponseDataScoresScoreDetails(APIResponseSchema):
    category: GetDraftResponseDataScoreScoreDetailsCategory | None = Field(default=None)
    brand: GetDraftResponseDataScoreScoreDetailsBrand | None = Field(default=None)
    type: GetDraftResponseDataScoreScoreDetailsType | None = Field(default=None)
    model: GetDraftResponseDataScoreScoreDetailsModel | None = Field(default=None)
    originality: GetDraftResponseDataScoreScoreDetailsOriginality | None = Field(default=None)
    division: GetDraftResponseDataScoreScoreDetailsDivision | None = Field(default=None)
    mefa: GetDraftResponseDataScoreScoreDetailsMefa | None = Field(default=None)
    description: GetDraftResponseDataScoreScoreDetailsDescription | None = Field(default=None)
    advantage: GetDraftResponseDataScoreScoreDetailsAdvantage | None = Field(default=None)
    disadvantage: GetDraftResponseDataScoreScoreDetailsDisadvantage | None = Field(default=None)
    attribute_1597: GetDraftResponseDataScoreScoreDetailsAttribute1597 | None = Field(default=None)
    title_fa: GetDraftResponseDataScoreScoreDetailsTitleFa | None = Field(default=None)
    title_en: GetDraftResponseDataScoreScoreDetailsTitleEn | None = Field(default=None)
    photo: GetDraftResponseDataScoreScoreDetailsPhoto | None = Field(default=None)


class PublishRequest(RequestSchema):
    force_marketplace_seller_id: int | None = Field(default=None)


class PublishResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )


class GetEditResponseDataProductDataImagesItemOptions(APIResponseSchema):
    type: str | None = Field(default=None)
    watermark: bool | None = Field(default=None)
    copyright: bool | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    sort: int | None = Field(default=None)


class GetEditResponseDataModerationResponse(APIResponseSchema):
    images: list[str] | None = Field(default=None)


class GetEditResponseDataStepsModerationStatus(APIResponseSchema):
    step_title: bool | None = Field(default=None)
    step_category: bool | None = Field(default=None)
    step_basic_info: bool | None = Field(default=None)
    step_attribute: bool | None = Field(default=None)
    step_image: bool | None = Field(default=None)


class UpdateRequestAttributesValue0(RequestSchema):
    id: int | None = Field(default=None)
    value: JsonValue = Field(default=None)


class GenerateTitleRequest(RequestSchema):
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int
    product_type_ids: list[int] | None = Field(default=None)
    attributes: dict[str, UpdateRequestAttributesValue0] | None = Field(default=None)


class GenerateTitleResponseData(APIResponseSchema):
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    hint: GetAutoTitleResponseDataHint | None = Field(default=None)
    enable_edit: bool | None = Field(default=None)


class SearchResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    status: str | None = Field(default=None)
    min_price: int | None = Field(default=None)
    commission: SearchResponseDataItemsItemCommission | None = Field(default=None)
    market_price: int | None = Field(default=None)
    image_src: str | None = Field(default=None)
    price_type: SearchResponseDataItemsItemPriceType | None = Field(default=None)
    color_type: str | None = Field(default=None)
    number_of_sellers: int | None = Field(default=None)
    is_selling: bool | None = Field(default=None)
    site: str | None = Field(default=None)


class SuggestionsResponseDataItemsItemCategoriesItem(APIResponseSchema):
    keyword: str | None = Field(default=None)
    category: SuggestionsResponseDataItemsItemCategoriesItemCategory | None = Field(default=None)


class SellerPermissionResponseDataCategory(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    themes: list[SellerPermissionResponseDataCategoryThemesItem] | None = Field(default=None)


class SearchCategoriesResponseData(APIResponseSchema):
    sort_data: SearchCategoriesResponseDataSortData | None = Field(default=None)
    pager: SearchCategoriesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SearchCategoriesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ValidateCategoryResponseDataBindGuidelineAttributes(APIResponseSchema):
    video: str | None = Field(default=None)
    short_description: str | None = Field(default=None)
    items: list[ValidateCategoryResponseDataBindGuidelineAttributesItemsItem] | None = Field(
        default=None
    )


class ValidateCategoryResponseDataBindGuidelineProductInfo(APIResponseSchema):
    video: str | None = Field(default=None)
    short_description: str | None = Field(default=None)
    items: list[ValidateCategoryResponseDataBindGuidelineProductInfoItemsItem] | None = Field(
        default=None
    )


class ValidateCategoryResponseDataBindGuidelineMedia(APIResponseSchema):
    video: str | None = Field(default=None)
    short_description: str | None = Field(default=None)
    items: list[ValidateCategoryResponseDataBindGuidelineMediaItemsItem] | None = Field(
        default=None
    )


class ValidateCategoryResponseDataBindDimensionConfig(APIResponseSchema):
    length: ValidateCategoryResponseDataBindDimensionConfigLength | None = Field(default=None)
    width: ValidateCategoryResponseDataBindDimensionConfigWidth | None = Field(default=None)
    height: ValidateCategoryResponseDataBindDimensionConfigHeight | None = Field(default=None)
    weight: ValidateCategoryResponseDataBindDimensionConfigWeight | None = Field(default=None)


class ValidateCategoryResponseDataBindGeneralMefa(APIResponseSchema):
    general_mefa_id: ValidateCategoryResponseDataBindGeneralMefaGeneralMefaId | None = Field(
        default=None
    )


class ValidateDetailsResponseData(APIResponseSchema):
    is_valid: bool | None = Field(default=None)
    errors: list[str] | None = Field(default=None)
    bind: ValidateDetailsResponseDataBind | None = Field(default=None)
    draft_product_id: int | None = Field(default=None)


class CountDraftsResponse(APIResponseSchema):
    status: int | str
    data: CountDraftsResponseData


class GetDraftResponseDataScoreScoreDetails(APIResponseSchema):
    category: GetDraftResponseDataScoreScoreDetailsCategory | None = Field(default=None)
    brand: GetDraftResponseDataScoreScoreDetailsBrand | None = Field(default=None)
    type: GetDraftResponseDataScoreScoreDetailsType | None = Field(default=None)
    model: GetDraftResponseDataScoreScoreDetailsModel | None = Field(default=None)
    originality: GetDraftResponseDataScoreScoreDetailsOriginality | None = Field(default=None)
    division: GetDraftResponseDataScoreScoreDetailsDivision | None = Field(default=None)
    mefa: GetDraftResponseDataScoreScoreDetailsMefa | None = Field(default=None)
    description: GetDraftResponseDataScoreScoreDetailsDescription | None = Field(default=None)
    advantage: GetDraftResponseDataScoreScoreDetailsAdvantage | None = Field(default=None)
    disadvantage: GetDraftResponseDataScoreScoreDetailsDisadvantage | None = Field(default=None)
    attribute_1597: GetDraftResponseDataScoreScoreDetailsAttribute1597 | None = Field(default=None)
    title_fa: GetDraftResponseDataScoreScoreDetailsTitleFa | None = Field(default=None)
    title_en: GetDraftResponseDataScoreScoreDetailsTitleEn | None = Field(default=None)
    photo: GetDraftResponseDataScoreScoreDetailsPhoto | None = Field(default=None)


class GetAutoTitleResponseData(APIResponseSchema):
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    hint: GetAutoTitleResponseDataHint | None = Field(default=None)
    enable_edit: bool | None = Field(default=None)


class SaveAutoTitleResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )
    data: SaveAutoTitleResponseDataData | None = Field(default=None)


class GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    code: str | None = Field(default=None)
    postfix: str | None = Field(default=None)
    unit: str | None = Field(default=None)
    type: str | None = Field(default=None)
    required: bool | None = Field(default=None)
    value: JsonValue = Field(default=None)
    values: (
        ObjectMap[
            GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1ValuesValue0
        ]
        | None
    ) = Field(default=None)
    hint: str | None = Field(default=None)


class SaveAttributesRequest(RequestSchema):
    draft_product_id: int
    length: float | None = Field(default=None)
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)
    weight: float | None = Field(default=None)
    attributes: list[list[SaveAttributesRequestAttributesItemItem]] | None = Field(default=None)


class UploadBrandLogoResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )
    data: UploadBrandLogoResponseDataData | None = Field(default=None)


class UploadRequestImageResponse(APIResponseSchema):
    status: str
    data: UploadBrandLogoResponseData


class UploadImageResponse(APIResponseSchema):
    status: str
    data: UploadBrandLogoResponseData


class GenerateImageResponse(APIResponseSchema):
    status: str
    data: GenerateImageResponseData


class SaveRequestPhotosDetail(RequestSchema):
    main_image: str | None = Field(default=None)
    order: str | None = Field(default=None)
    images: list[SaveRequestPhotosDetailImagesItem] | None = Field(default=None)


class SaveResponseData(APIResponseSchema):
    data: SaveResponseDataData | None = Field(default=None)


class AssignResponse(APIResponseSchema):
    status: str
    data: AssignResponseData


class RequestBrandResponseData(APIResponseSchema):
    data: RequestBrandResponseDataData | None = Field(default=None)


class ListBrandsResponseDataItemsItem(APIResponseSchema):
    value: ListBrandsResponseDataItemsItemValue | None = Field(
        default=None, validation_alias="شیائومی", serialization_alias="شیائومی"
    )


class ListSellerResponseDataItemsItem(APIResponseSchema):
    variants_count: int | None = Field(default=None)
    site: str | None = Field(default=None)
    title: str | None = Field(default=None)
    status: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    fake: bool | None = Field(default=None)
    status_data: str | None = Field(default=None)
    is_owner: bool | None = Field(default=None)
    main_category_title: ObjectMap[str] | None = Field(default=None)
    active: bool | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    brand_title_en: str | None = Field(default=None)
    brand_title_fa: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    image_src: str | None = Field(default=None)
    dimension_level: str | None = Field(default=None)
    brand_title: str | None = Field(default=None)
    moderation_status: ListSellerResponseDataItemsItemModerationStatus | None = Field(default=None)
    adverge_url: str | None = Field(default=None)
    product_dimension: SellerPermissionResponseDataProductDimension | None = Field(default=None)


class ScoreResponseDataScores(APIResponseSchema):
    score_details: ScoreResponseDataScoresScoreDetails | None = Field(default=None)
    total: int | None = Field(default=None)
    max: int | None = Field(default=None)
    percent: int | None = Field(default=None)


class PublishResponse(APIResponseSchema):
    status: str
    data: PublishResponseData


class GetEditResponseDataProductDataImagesItem(APIResponseSchema):
    encrypted_id: str | None = Field(default=None)
    image_url: str | None = Field(default=None)
    image_max_url: str | None = Field(default=None)
    is_main: bool | None = Field(default=None)
    options: GetEditResponseDataProductDataImagesItemOptions | None = Field(default=None)
    order: int | None = Field(default=None)


class UpdateRequest(RequestSchema):
    category_id: int
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int
    product_type_ids: list[int] | None = Field(default=None)
    color_id: int | None = Field(default=None)
    is_iranian: bool
    product_classes: list[int] | None = Field(default=None)
    fake: bool | None = Field(default=None)
    general_mefa_id: str | None = Field(default=None)
    exclusive_mefa_id: str | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    description: str | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    length: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    attributes: dict[str, UpdateRequestAttributesValue0] | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    title_en: str | None = Field(default=None)
    use_temp_images: bool | None = Field(default=None)
    photos_detail: SaveRequestPhotosDetail | None = Field(default=None)
    video_ids: list[str] | None = Field(default=None)


class GenerateTitleResponse(APIResponseSchema):
    status: str
    data: GenerateTitleResponseData


class SearchResponseData(APIResponseSchema):
    sort_data: SearchResponseDataSortData | None = Field(default=None)
    pager: SearchResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SearchResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class SuggestionsResponseDataItemsItem(APIResponseSchema):
    categories: list[SuggestionsResponseDataItemsItemCategoriesItem] | None = Field(default=None)
    auto_complete: list[SuggestionsResponseDataItemsItemAutoCompleteItem] | None = Field(
        default=None
    )


class SellerPermissionResponseData(APIResponseSchema):
    name: str | None = Field(default=None)
    brand: str | None = Field(default=None)
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    commission: SellerPermissionResponseDataCommission | None = Field(default=None)
    product_url: str | None = Field(
        default=None, validation_alias="productURL", serialization_alias="productURL"
    )
    reference_price: int | None = Field(
        default=None, validation_alias="referencePrice", serialization_alias="referencePrice"
    )
    product_image: str | None = Field(
        default=None, validation_alias="productImage", serialization_alias="productImage"
    )
    fulfillment_and_delivery_cost: SellerPermissionResponseDataFulfillmentAndDeliveryCost | None = (
        Field(
            default=None,
            validation_alias="fulfillmentAndDeliveryCost",
            serialization_alias="fulfillmentAndDeliveryCost",
        )
    )
    category: SellerPermissionResponseDataCategory | None = Field(default=None)
    site: str | None = Field(default=None)
    product_dimension: SellerPermissionResponseDataProductDimension | None = Field(default=None)
    price_type: str | None = Field(default=None)


class SearchCategoriesResponse(APIResponseSchema):
    status: str
    data: SearchCategoriesResponseData


class ValidateCategoryResponseDataBindGuideline(APIResponseSchema):
    category_selection: ValidateCategoryResponseDataBindGuidelineCategorySelection | None = Field(
        default=None
    )
    attributes: ValidateCategoryResponseDataBindGuidelineAttributes | None = Field(default=None)
    product_info: ValidateCategoryResponseDataBindGuidelineProductInfo | None = Field(default=None)
    media: ValidateCategoryResponseDataBindGuidelineMedia | None = Field(default=None)


class ValidateDetailsResponse(APIResponseSchema):
    status: str
    data: ValidateDetailsResponseData


class GetDraftResponseDataScore(APIResponseSchema):
    score_details: GetDraftResponseDataScoreScoreDetails | None = Field(default=None)
    total: int | None = Field(default=None)
    max: int | None = Field(default=None)
    percent: int | None = Field(default=None)


class GetAutoTitleResponse(APIResponseSchema):
    status: int | str
    data: GetAutoTitleResponseData


class SaveAutoTitleResponse(APIResponseSchema):
    status: str
    data: SaveAutoTitleResponseData


class GetAttributesResponseDataCategoryGroupAttributesValue0(APIResponseSchema):
    group_title: str | None = Field(default=None)
    attributes: (
        ObjectMap[
            GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue0
            | GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1
        ]
        | None
    ) = Field(default=None)


class UploadBrandLogoResponse(APIResponseSchema):
    status: str
    data: UploadBrandLogoResponseData


class SaveRequest(RequestSchema):
    category_id: int | None = Field(default=None)
    draft_product_id: int | None = Field(default=None)
    use_temp_images: bool | None = Field(default=None)
    only_b2b: bool | None = Field(default=None)
    photos_detail: SaveRequestPhotosDetail | None = Field(default=None)


class SaveResponse(APIResponseSchema):
    status: str
    data: SaveResponseData


class RequestBrandResponse(APIResponseSchema):
    status: str
    data: RequestBrandResponseData


class ListBrandsResponseData(APIResponseSchema):
    sort_data: SearchCategoriesResponseDataSortData | None = Field(default=None)
    pager: SearchCategoriesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListBrandsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListDraftsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    category_name: str | None = Field(default=None)
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    brand_name: str | None = Field(default=None)
    product_type_ids: list[int] | None = Field(default=None)
    is_iranian: bool | None = Field(default=None)
    product_classes: list[str | int] | None = Field(default=None)
    fake: bool | None = Field(default=None)
    general_mefa_id: int | None = Field(default=None)
    exclusive_mefa_id: str | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)
    title_en: str | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    length: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    remaining_day: int | None = Field(default=None)
    site: str | None = Field(default=None)
    status: str | None = Field(default=None)
    product_type: str | None = Field(default=None)
    product_nature: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    active_digistyle: bool | None = Field(default=None)
    sensitivity: str | None = Field(default=None)
    vat: int | None = Field(default=None)
    next_step: list[str] | None = Field(default=None)
    step: str | None = Field(default=None)
    score: GetDraftResponseDataScore | None = Field(default=None)


class ListSellerResponseData(APIResponseSchema):
    sort_data: SearchResponseDataSortData | None = Field(default=None)
    pager: SearchResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListSellerResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ScoreResponseData(APIResponseSchema):
    score: ScoreResponseDataScore | None = Field(default=None)
    scores: ScoreResponseDataScores | None = Field(default=None)


class GetEditResponseDataProductData(APIResponseSchema):
    id: int | None = Field(default=None)
    marketplace_seller_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    product_type_ids: list[int] | None = Field(default=None)
    product_type: str | None = Field(default=None)
    show_colors: bool | None = Field(default=None)
    is_iranian: bool | None = Field(default=None)
    product_classes: list[str | int] | None = Field(default=None)
    fake: bool | None = Field(default=None)
    general_mefa_id: int | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)
    title_en: str | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    attributes: ObjectMap[ObjectMap[str]] | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    length: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    brand_name: str | None = Field(default=None)
    moderation_status: str | None = Field(default=None)
    images: list[GetEditResponseDataProductDataImagesItem] | None = Field(default=None)


class SearchResponse(APIResponseSchema):
    status: str
    data: SearchResponseData


class SuggestionsResponseData(APIResponseSchema):
    sort_data: SearchResponseDataSortData | None = Field(default=None)
    pager: SearchResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[SuggestionsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class SellerPermissionResponse(APIResponseSchema):
    status: int | str
    data: SellerPermissionResponseData


class ValidateCategoryResponseDataBind(APIResponseSchema):
    brands: list[ValidateCategoryResponseDataBindBrandsItem] | None = Field(default=None)
    category_product_types: (
        list[ValidateCategoryResponseDataBindCategoryProductTypesItem] | None
    ) = Field(default=None)
    product_classes: list[ValidateCategoryResponseDataBindProductClassesItem] | None = Field(
        default=None
    )
    divisions: list[str] | None = Field(default=None)
    guideline: ValidateCategoryResponseDataBindGuideline | None = Field(default=None)
    category_data: ValidateCategoryResponseDataBindCategoryData | None = Field(default=None)
    allow_fake: bool | None = Field(default=None)
    brand_other_id: int | None = Field(default=None)
    show_colors: bool | None = Field(default=None)
    dimension_level: str | None = Field(default=None)
    dimension_config: ValidateCategoryResponseDataBindDimensionConfig | None = Field(default=None)
    general_mefa: ValidateCategoryResponseDataBindGeneralMefa | None = Field(default=None)
    category_mefa_type: str | None = Field(default=None)
    statuses: list[ValidateCategoryResponseDataBindStatusesItem] | None = Field(default=None)
    platforms: list[ValidateCategoryResponseDataBindPlatformsItem] | None = Field(default=None)


class GetDraftResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    category_name: str | None = Field(default=None)
    division_id: int | None = Field(default=None)
    model: str | None = Field(default=None)
    brand_id: int | None = Field(default=None)
    brand_name: str | None = Field(default=None)
    product_type_ids: list[int] | None = Field(default=None)
    is_iranian: bool | None = Field(default=None)
    product_classes: list[str | int] | None = Field(default=None)
    fake: bool | None = Field(default=None)
    general_mefa_id: int | None = Field(default=None)
    exclusive_mefa_id: str | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    platforms: list[str] | None = Field(default=None)
    description: str | None = Field(default=None)
    advantages: list[str] | None = Field(default=None)
    disadvantages: list[str] | None = Field(default=None)
    title_en: str | None = Field(default=None)
    title_fa: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    length: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    remaining_day: int | None = Field(default=None)
    site: str | None = Field(default=None)
    status: str | None = Field(default=None)
    product_type: str | None = Field(default=None)
    product_nature: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    active_digistyle: bool | None = Field(default=None)
    sensitivity: str | None = Field(default=None)
    vat: int | None = Field(default=None)
    next_step: list[str] | None = Field(default=None)
    step: str | None = Field(default=None)
    score: GetDraftResponseDataScore | None = Field(default=None)


class GetAttributesResponseData(APIResponseSchema):
    category_group_attributes: (
        ObjectMap[GetAttributesResponseDataCategoryGroupAttributesValue0] | None
    ) = Field(default=None)
    attribute_dimensions: bool | None = Field(default=None)
    dimensions_attribute_postfix: str | None = Field(default=None)
    has_height: bool | None = Field(default=None)
    dimensions_attribute: bool | None = Field(default=None)
    weight_attribute: bool | None = Field(default=None)
    weight_attribute_postfix: str | None = Field(default=None)
    weight_attribute_required: bool | None = Field(default=None)
    weight_attribute_reasons: bool | None = Field(default=None)
    weight_attribute_hint: str | None = Field(default=None)
    dimensions_attribute_required: bool | None = Field(default=None)
    dimensions_attribute_hint: str | None = Field(default=None)
    dimension_attribute_multiplier: int | None = Field(default=None)
    weight_attribute_multiplier: int | None = Field(default=None)


class ListBrandsResponse(APIResponseSchema):
    status: str
    data: ListBrandsResponseData


class ListDraftsResponseData(APIResponseSchema):
    sort_data: SearchResponseDataSortData | None = Field(default=None)
    pager: SearchResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListDraftsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListSellerResponse(APIResponseSchema):
    status: str
    data: ListSellerResponseData


class ScoreResponse(APIResponseSchema):
    status: int | str
    data: ScoreResponseData


class GetEditResponseData(APIResponseSchema):
    product_data: GetEditResponseDataProductData | None = Field(default=None)
    moderation_response: GetEditResponseDataModerationResponse | None = Field(default=None)
    enabled_fields: list[str] | None = Field(default=None)
    steps_moderation_status: GetEditResponseDataStepsModerationStatus | None = Field(default=None)
    locked_for_moderation: bool | None = Field(default=None)
    multi_seller_product: bool | None = Field(default=None)
    edit_status: str | None = Field(default=None)


class SuggestionsResponse(APIResponseSchema):
    status: str
    data: SuggestionsResponseData


class ValidateCategoryResponseData(APIResponseSchema):
    is_valid: bool | None = Field(
        default=None, validation_alias="isValid", serialization_alias="isValid"
    )
    errors: list[str] | None = Field(default=None)
    bind: ValidateCategoryResponseDataBind | None = Field(default=None)


class GetDraftResponse(APIResponseSchema):
    status: int | str
    data: GetDraftResponseData


class GetAttributesResponse(APIResponseSchema):
    status: int | str
    data: GetAttributesResponseData


class ListDraftsResponse(APIResponseSchema):
    status: str
    data: ListDraftsResponseData


class GetEditResponse(APIResponseSchema):
    status: int | str
    data: GetEditResponseData


class ValidateCategoryResponse(APIResponseSchema):
    status: int | str
    data: ValidateCategoryResponseData


__all__ = [
    "AssignRequest",
    "AssignResponse",
    "AssignResponseData",
    "CountDraftsResponse",
    "CountDraftsResponseData",
    "GenerateImageRequest",
    "GenerateImageResponse",
    "GenerateImageResponseData",
    "GenerateTitleRequest",
    "GenerateTitleResponse",
    "GenerateTitleResponseData",
    "GetAttributesResponse",
    "GetAttributesResponseData",
    "GetAttributesResponseDataCategoryGroupAttributesValue0",
    "GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue0",
    "GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1",
    "GetAttributesResponseDataCategoryGroupAttributesValue0AttributesValue1ValuesValue0",
    "GetAutoTitleResponse",
    "GetAutoTitleResponseData",
    "GetAutoTitleResponseDataHint",
    "GetDraftResponse",
    "GetDraftResponseData",
    "GetDraftResponseDataScore",
    "GetDraftResponseDataScoreScoreDetails",
    "GetDraftResponseDataScoreScoreDetailsAdvantage",
    "GetDraftResponseDataScoreScoreDetailsAttribute1597",
    "GetDraftResponseDataScoreScoreDetailsBrand",
    "GetDraftResponseDataScoreScoreDetailsCategory",
    "GetDraftResponseDataScoreScoreDetailsDescription",
    "GetDraftResponseDataScoreScoreDetailsDisadvantage",
    "GetDraftResponseDataScoreScoreDetailsDivision",
    "GetDraftResponseDataScoreScoreDetailsMefa",
    "GetDraftResponseDataScoreScoreDetailsModel",
    "GetDraftResponseDataScoreScoreDetailsOriginality",
    "GetDraftResponseDataScoreScoreDetailsPhoto",
    "GetDraftResponseDataScoreScoreDetailsTitleEn",
    "GetDraftResponseDataScoreScoreDetailsTitleFa",
    "GetDraftResponseDataScoreScoreDetailsType",
    "GetEditResponse",
    "GetEditResponseData",
    "GetEditResponseDataModerationResponse",
    "GetEditResponseDataProductData",
    "GetEditResponseDataProductDataImagesItem",
    "GetEditResponseDataProductDataImagesItemOptions",
    "GetEditResponseDataStepsModerationStatus",
    "ListBrandsQuery",
    "ListBrandsResponse",
    "ListBrandsResponseData",
    "ListBrandsResponseDataItemsItem",
    "ListBrandsResponseDataItemsItemValue",
    "ListDraftsQuery",
    "ListDraftsResponse",
    "ListDraftsResponseData",
    "ListDraftsResponseDataItemsItem",
    "ListSellerQuery",
    "ListSellerResponse",
    "ListSellerResponseData",
    "ListSellerResponseDataItemsItem",
    "ListSellerResponseDataItemsItemModerationStatus",
    "PublishRequest",
    "PublishResponse",
    "PublishResponseData",
    "RequestBrandRequest",
    "RequestBrandResponse",
    "RequestBrandResponseData",
    "RequestBrandResponseDataData",
    "SaveAttributesRequest",
    "SaveAttributesRequestAttributesItemItem",
    "SaveAutoTitleRequest",
    "SaveAutoTitleResponse",
    "SaveAutoTitleResponseData",
    "SaveAutoTitleResponseDataData",
    "SaveRequest",
    "SaveRequestPhotosDetail",
    "SaveRequestPhotosDetailImagesItem",
    "SaveResponse",
    "SaveResponseData",
    "SaveResponseDataData",
    "ScoreResponse",
    "ScoreResponseData",
    "ScoreResponseDataScore",
    "ScoreResponseDataScores",
    "ScoreResponseDataScoresScoreDetails",
    "SearchCategoriesResponse",
    "SearchCategoriesResponseData",
    "SearchCategoriesResponseDataItemsItem",
    "SearchCategoriesResponseDataPager",
    "SearchCategoriesResponseDataSortData",
    "SearchQuery",
    "SearchResponse",
    "SearchResponseData",
    "SearchResponseDataItemsItem",
    "SearchResponseDataItemsItemCommission",
    "SearchResponseDataItemsItemPriceType",
    "SearchResponseDataPager",
    "SearchResponseDataSortData",
    "SellerPermissionResponse",
    "SellerPermissionResponseData",
    "SellerPermissionResponseDataCategory",
    "SellerPermissionResponseDataCategoryThemesItem",
    "SellerPermissionResponseDataCommission",
    "SellerPermissionResponseDataFulfillmentAndDeliveryCost",
    "SellerPermissionResponseDataProductDimension",
    "SuggestionsQuery",
    "SuggestionsResponse",
    "SuggestionsResponseData",
    "SuggestionsResponseDataItemsItem",
    "SuggestionsResponseDataItemsItemAutoCompleteItem",
    "SuggestionsResponseDataItemsItemCategoriesItem",
    "SuggestionsResponseDataItemsItemCategoriesItemCategory",
    "UpdateRequest",
    "UpdateRequestAttributesValue0",
    "UploadBrandLogoResponse",
    "UploadBrandLogoResponseData",
    "UploadBrandLogoResponseDataData",
    "UploadImageResponse",
    "UploadRequestImageResponse",
    "ValidateCategoryResponse",
    "ValidateCategoryResponseData",
    "ValidateCategoryResponseDataBind",
    "ValidateCategoryResponseDataBindBrandsItem",
    "ValidateCategoryResponseDataBindCategoryData",
    "ValidateCategoryResponseDataBindCategoryProductTypesItem",
    "ValidateCategoryResponseDataBindDimensionConfig",
    "ValidateCategoryResponseDataBindDimensionConfigHeight",
    "ValidateCategoryResponseDataBindDimensionConfigLength",
    "ValidateCategoryResponseDataBindDimensionConfigWeight",
    "ValidateCategoryResponseDataBindDimensionConfigWidth",
    "ValidateCategoryResponseDataBindGeneralMefa",
    "ValidateCategoryResponseDataBindGeneralMefaGeneralMefaId",
    "ValidateCategoryResponseDataBindGuideline",
    "ValidateCategoryResponseDataBindGuidelineAttributes",
    "ValidateCategoryResponseDataBindGuidelineAttributesItemsItem",
    "ValidateCategoryResponseDataBindGuidelineCategorySelection",
    "ValidateCategoryResponseDataBindGuidelineMedia",
    "ValidateCategoryResponseDataBindGuidelineMediaItemsItem",
    "ValidateCategoryResponseDataBindGuidelineProductInfo",
    "ValidateCategoryResponseDataBindGuidelineProductInfoItemsItem",
    "ValidateCategoryResponseDataBindPlatformsItem",
    "ValidateCategoryResponseDataBindProductClassesItem",
    "ValidateCategoryResponseDataBindStatusesItem",
    "ValidateDetailsRequest",
    "ValidateDetailsResponse",
    "ValidateDetailsResponseData",
    "ValidateDetailsResponseDataBind",
]
