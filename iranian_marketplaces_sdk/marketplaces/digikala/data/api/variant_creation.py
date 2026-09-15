"""Digikala variant creation: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class GetResponseDataWarrantyOptionsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class GetResponseDataThemesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    label: str | None = Field(default=None)
    theme_type: str | None = Field(
        default=None, validation_alias="themeType", serialization_alias="themeType"
    )


class GetResponseDataDimensionConfigLength(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class GetResponseDataDimensionConfigWidth(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class GetResponseDataDimensionConfigHeight(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class GetResponseDataDimensionConfigWeight(APIResponseSchema):
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class GetResponseDataGoldPriceData(APIResponseSchema):
    live_gold_price: int | None = Field(default=None)
    tax: float | None = Field(default=None)
    gold_wage_max_margin: float | None = Field(default=None)
    profit_max_margin: float | None = Field(default=None)
    is_pure_gold: bool | None = Field(default=None)


class GetResponseDataSizeGuideConfigItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    unit: str | None = Field(default=None)
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class GetResponseDataVariantPhotoUpload(APIResponseSchema):
    can_upload: str | None = Field(default=None)
    main_image_mandatory: bool | None = Field(default=None)


class CreateRequestGoldPriceParameters(RequestSchema):
    gold_wage: int | None = Field(default=None)
    gold_profit: int | None = Field(default=None)
    non_gold_parts_wage: int | None = Field(default=None)
    non_gold_parts_profit: int | None = Field(default=None)


class CreateRequestSizesItem(RequestSchema):
    id: str | None = Field(default=None)
    value: int | None = Field(default=None)


class CreateRequestPhotosDetailItem(RequestSchema):
    id: str | None = Field(default=None)
    is_main: bool | None = Field(default=None)


class CreateRequestThemeValuesItem(RequestSchema):
    theme_id: int | None = Field(default=None)
    theme_value_id: int | None = Field(default=None)


class CreateResponseDataGoldPriceParameters(APIResponseSchema):
    gold_wage: int | None = Field(default=None)
    gold_profit: int | None = Field(default=None)
    non_gold_parts_wage: int | None = Field(default=None)
    non_gold_parts_profit: int | None = Field(default=None)


class CreateResponseDataSizeAttributesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    unit: str | None = Field(default=None)
    value: int | None = Field(default=None)
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class CreateResponseDataThemeValuesItemThemeValue(APIResponseSchema):
    id: int | None = Field(default=None)
    value: str | None = Field(default=None)
    meta: ObjectMap[JsonValue] | None = Field(default=None)


class UpdateQuery(QuerySchema):
    force_marketplace_seller_id: int | None = Field(default=None)


class UpdateRequestGoldPriceParameters(RequestSchema):
    gold_wage: float | None = Field(default=None)
    gold_profit: float | None = Field(default=None)
    non_gold_parts_wage: float | None = Field(default=None)
    non_gold_parts_cost: float | None = Field(default=None)


class UpdateRequestAutoPricingParameters(RequestSchema):
    non_parts_wage: int | None = Field(default=None)
    non_parts_cost: int | None = Field(default=None)
    wage: int | None = Field(default=None)
    wage_pct: float | None = Field(default=None)
    profit: float | None = Field(default=None)


class UpdateRequestSizesItem(RequestSchema):
    id: str | None = Field(default=None)
    value: int | None = Field(default=None)


class UpdateRequestPhotosDetailItem(RequestSchema):
    id: str | None = Field(default=None)
    is_main: bool | None = Field(default=None)


class UpdateResponseDataGoldPriceParameters(APIResponseSchema):
    gold_wage: float | None = Field(default=None)
    gold_profit: float | None = Field(default=None)
    non_gold_parts_wage: float | None = Field(default=None)
    non_gold_parts_cost: float | None = Field(default=None)


class UpdateResponseDataAutoPricingParameters(APIResponseSchema):
    carat: float | int | None = Field(default=None)
    non_parts_cost: int | None = Field(default=None)
    non_parts_wage: int | None = Field(default=None)
    wage: int | None = Field(default=None)
    wage_pct: float | None = Field(default=None)
    profit: float | None = Field(default=None)
    size: float | None = Field(default=None)
    tax: float | int | None = Field(default=None)
    trigger_price: int | None = Field(default=None)
    is_pure: bool | None = Field(default=None)


class UpdateResponseDataSizeAttributesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    unit: str | None = Field(default=None)
    min: int | None = Field(default=None)
    max: int | None = Field(default=None)


class ListSizeTypesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ListSizeTypesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListSizeTypesResponseDataItemsItem(APIResponseSchema):
    size_type: str | None = Field(
        default=None, validation_alias="sizeType", serialization_alias="sizeType"
    )


class RequestSizeRequest(RequestSchema):
    product_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    theme_id: int | None = Field(default=None)


class RequestSizeResponseData(APIResponseSchema):
    id: int | None = Field(default=None)


class RequestColorRequest(RequestSchema):
    product_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    product_image_id: str | None = Field(default=None)
    hex_code: str | None = Field(default=None)
    theme_id: int | None = Field(default=None)


class RequestColorResponseData(APIResponseSchema):
    id: int | None = Field(default=None)


class RequestWarrantyRequest(RequestSchema):
    product_id: int | None = Field(default=None)
    warranty_title: str
    warranty_period: int
    warranty_image_id_1: str
    warranty_image_id_2: str | None = Field(default=None)
    has_insurance: bool
    insurance_title: str | None = Field(default=None)
    insurance_period: int | None = Field(default=None)
    insurance_image_id_1: str | None = Field(default=None)
    insurance_image_id_2: str | None = Field(default=None)


class RequestWarrantyResponseData(APIResponseSchema):
    id: int | None = Field(default=None)


class GetResponseDataDimensionConfig(APIResponseSchema):
    length: GetResponseDataDimensionConfigLength | None = Field(default=None)
    width: GetResponseDataDimensionConfigWidth | None = Field(default=None)
    height: GetResponseDataDimensionConfigHeight | None = Field(default=None)
    weight: GetResponseDataDimensionConfigWeight | None = Field(default=None)


class GetResponseDataSizeGuide(APIResponseSchema):
    config: list[GetResponseDataSizeGuideConfigItem] | None = Field(default=None)
    is_required_on_create: bool | None = Field(default=None)
    is_required_on_edit: bool | None = Field(default=None)


class CreateRequest(RequestSchema):
    is_active: bool
    order_limit: int
    marketplace_seller_stock: int
    supplier_code: str | None = Field(default=None)
    price: int | None = Field(default=None)
    warranty_id: int
    site: str
    shipping_type: str
    lead_time: int | None = Field(default=None)
    fbs_lead_time: int | None = Field(default=None)
    three_hour_delivery: bool | None = Field(default=None)
    color_id: int | None = Field(default=None)
    size_id: int | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    gold_price_parameters: CreateRequestGoldPriceParameters | None = Field(default=None)
    sizes: list[CreateRequestSizesItem] | None = Field(default=None)
    photos_detail: list[CreateRequestPhotosDetailItem] | None = Field(default=None)
    theme_values: list[CreateRequestThemeValuesItem] | None = Field(default=None)


class CreateResponseDataThemeValuesItem(APIResponseSchema):
    theme_id: int | None = Field(default=None)
    theme_value_id: int | None = Field(default=None)
    theme_label: str | None = Field(default=None)
    theme_value: CreateResponseDataThemeValuesItemThemeValue | None = Field(
        default=None, validation_alias="themeValue", serialization_alias="themeValue"
    )


class UpdateRequest(RequestSchema):
    is_active: bool
    order_limit: int
    marketplace_seller_stock: int
    supplier_code: str | None = Field(default=None)
    price: int | None = Field(default=None)
    site: str
    shipping_type: str
    lead_time: int | None = Field(default=None)
    fbs_lead_time: int | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    gold_price_parameters: UpdateRequestGoldPriceParameters | None = Field(default=None)
    auto_pricing_parameters: UpdateRequestAutoPricingParameters | None = Field(default=None)
    sizes: list[UpdateRequestSizesItem] | None = Field(default=None)
    photos_detail: list[UpdateRequestPhotosDetailItem] | None = Field(default=None)
    three_hour_delivery: bool | None = Field(default=None)


class UpdateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    site: str | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    price: int | None = Field(default=None)
    reference_price: int | None = Field(default=None)
    shipping_type: str | None = Field(default=None)
    shipping_type_seller: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    fbs_lead_time: int | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    color_id: int | None = Field(default=None)
    size_id: int | None = Field(default=None)
    warranty_id: int | None = Field(default=None)
    theme_values: list[ObjectMap[JsonValue]] | None = Field(default=None)
    gold_price_parameters: UpdateResponseDataGoldPriceParameters | None = Field(default=None)
    auto_pricing_parameters: UpdateResponseDataAutoPricingParameters | None = Field(default=None)
    size_attributes: list[UpdateResponseDataSizeAttributesItem] | None = Field(default=None)
    is_three_hour_delivery_active: bool | None = Field(default=None)
    is_three_hour_checkbox_active: bool | None = Field(default=None)
    seller_lead_times: list[int] | None = Field(default=None)
    photos_detail: list[ObjectMap[JsonValue]] | None = Field(default=None)


class ListSizeTypesResponseData(APIResponseSchema):
    sort_data: ListSizeTypesResponseDataSortData | None = Field(default=None)
    pager: ListSizeTypesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListSizeTypesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class RequestSizeResponse(APIResponseSchema):
    status: str
    data: RequestSizeResponseData


class RequestColorResponse(APIResponseSchema):
    status: str
    data: RequestColorResponseData


class RequestWarrantyResponse(APIResponseSchema):
    status: str
    data: RequestWarrantyResponseData


class GetResponseData(APIResponseSchema):
    warranty_options: list[GetResponseDataWarrantyOptionsItem] | None = Field(default=None)
    lead_time_max: int | None = Field(default=None)
    variant_theme: str | None = Field(default=None)
    global_error_message: str | None = Field(default=None)
    is_ship_by_seller_module_active: bool | None = Field(default=None)
    is_only_sbs: bool | None = Field(default=None)
    themes: list[GetResponseDataThemesItem] | None = Field(default=None)
    dimension_config: GetResponseDataDimensionConfig | None = Field(default=None)
    gold_price_data: GetResponseDataGoldPriceData | None = Field(default=None)
    price: int | None = Field(default=None)
    size_guide: GetResponseDataSizeGuide | None = Field(default=None)
    variant_photo_upload: GetResponseDataVariantPhotoUpload | None = Field(default=None)


class CreateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    is_active: bool | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    site: str | None = Field(default=None)
    marketplace_seller_stock: int | None = Field(default=None)
    supplier_code: str | None = Field(default=None)
    price: int | None = Field(default=None)
    reference_price: int | None = Field(default=None)
    warranty_id: int | None = Field(default=None)
    shipping_type: str | None = Field(default=None)
    shipping_type_seller: bool | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    fbs_lead_time: int | None = Field(default=None)
    color_id: int | None = Field(default=None)
    size_id: int | None = Field(default=None)
    package_width: int | None = Field(default=None)
    package_height: int | None = Field(default=None)
    package_length: int | None = Field(default=None)
    package_weight: int | None = Field(default=None)
    gold_price_parameters: CreateResponseDataGoldPriceParameters | None = Field(default=None)
    size_attributes: list[CreateResponseDataSizeAttributesItem] | None = Field(default=None)
    theme_values: list[CreateResponseDataThemeValuesItem] | None = Field(default=None)


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class ListSizeTypesResponse(APIResponseSchema):
    status: str
    data: ListSizeTypesResponseData


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


__all__ = [
    "CreateRequest",
    "CreateRequestGoldPriceParameters",
    "CreateRequestPhotosDetailItem",
    "CreateRequestSizesItem",
    "CreateRequestThemeValuesItem",
    "CreateResponse",
    "CreateResponseData",
    "CreateResponseDataGoldPriceParameters",
    "CreateResponseDataSizeAttributesItem",
    "CreateResponseDataThemeValuesItem",
    "CreateResponseDataThemeValuesItemThemeValue",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataDimensionConfig",
    "GetResponseDataDimensionConfigHeight",
    "GetResponseDataDimensionConfigLength",
    "GetResponseDataDimensionConfigWeight",
    "GetResponseDataDimensionConfigWidth",
    "GetResponseDataGoldPriceData",
    "GetResponseDataSizeGuide",
    "GetResponseDataSizeGuideConfigItem",
    "GetResponseDataThemesItem",
    "GetResponseDataVariantPhotoUpload",
    "GetResponseDataWarrantyOptionsItem",
    "ListSizeTypesResponse",
    "ListSizeTypesResponseData",
    "ListSizeTypesResponseDataItemsItem",
    "ListSizeTypesResponseDataPager",
    "ListSizeTypesResponseDataSortData",
    "RequestColorRequest",
    "RequestColorResponse",
    "RequestColorResponseData",
    "RequestSizeRequest",
    "RequestSizeResponse",
    "RequestSizeResponseData",
    "RequestWarrantyRequest",
    "RequestWarrantyResponse",
    "RequestWarrantyResponseData",
    "UpdateQuery",
    "UpdateRequest",
    "UpdateRequestAutoPricingParameters",
    "UpdateRequestGoldPriceParameters",
    "UpdateRequestPhotosDetailItem",
    "UpdateRequestSizesItem",
    "UpdateResponse",
    "UpdateResponseData",
    "UpdateResponseDataAutoPricingParameters",
    "UpdateResponseDataGoldPriceParameters",
    "UpdateResponseDataSizeAttributesItem",
]
