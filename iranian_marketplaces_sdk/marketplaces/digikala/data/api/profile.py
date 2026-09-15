"""Digikala profile: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class GetResponseDataVerification(APIResponseSchema):
    hoda_modal: str | None = Field(default=None)
    is_under_18: bool | None = Field(default=None)
    emta_modal: str | None = Field(default=None)


class GetResponseDataRegisterPhone(APIResponseSchema):
    submitted: bool | None = Field(default=None)
    seen_warning_at: str | None = Field(default=None)
    restricted: bool | None = Field(default=None)


class GetResponseDataContractStatus(APIResponseSchema):
    signed: bool | None = Field(default=None)
    expired: bool | None = Field(default=None)
    restricted: bool | None = Field(default=None)


class GetResponseDataRegistrationMetadata(APIResponseSchema):
    is_rural: bool | None = Field(default=None)
    is_brand: bool | None = Field(default=None)
    is_instagram_shop: bool | None = Field(default=None)


class GetResponseDataMetadata(APIResponseSchema):
    tier: str | None = Field(default=None)
    register_status: str | None = Field(default=None)
    status: str | None = Field(default=None)
    supply_categories: list[int] | None = Field(default=None)
    open_api_token_status: str | None = Field(default=None)
    has_sbs_setting: bool | None = Field(default=None)
    has_nearby_setting: bool | None = Field(default=None)
    city_id: int | None = Field(default=None)
    platform: str | None = Field(default=None)


class GetResponseDataSubscription(APIResponseSchema):
    plan_name: str | None = Field(default=None)
    status: str | None = Field(default=None)
    is_trial: bool | None = Field(default=None)


class BusinessResponseDataVerificationStatus(APIResponseSchema):
    national_id: bool | None = Field(default=None)
    mobile_phone: bool | None = Field(default=None)
    register_phone: bool | None = Field(default=None)
    email: bool | None = Field(default=None)
    company_name: bool | None = Field(default=None)
    company_type: bool | None = Field(default=None)
    company_registration_number: bool | None = Field(default=None)
    company_national_id_number: bool | None = Field(default=None)
    company_economic_number: bool | None = Field(default=None)
    company_authorized_representative: bool | None = Field(default=None)


class BusinessResponseDataCompanyType(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class UpdateBusinessRequest(RequestSchema):
    type: str
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    national_id: str | None = Field(default=None)
    company_name: str | None = Field(default=None)
    company_type: str | None = Field(default=None)
    company_registration_number: str | None = Field(default=None)
    company_national_id_number: str | None = Field(default=None)
    company_economic_number: str | None = Field(default=None)
    company_authorized_representative: str | None = Field(default=None)


class UpdateBusinessResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class StoreResponseDataDescription(APIResponseSchema):
    description: str | None = Field(default=None)
    status: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)


class StoreResponseDataHolidaysItemDate(APIResponseSchema):
    date: str | None = Field(default=None)
    timezone_type: int | None = Field(default=None)
    timezone: str | None = Field(default=None)


class StoreResponseDataWorkdaysItemDate(APIResponseSchema):
    date: str | None = Field(default=None)
    timezone_type: int | None = Field(default=None)
    timezone: str | None = Field(default=None)


class StoreResponseDataLogo(APIResponseSchema):
    file: str | None = Field(default=None)
    status: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)


class StoreResponseDataRegistrationStatus(APIResponseSchema):
    is_logo_approved: bool | None = Field(default=None)
    is_description_approved: bool | None = Field(default=None)
    is_phone_valid: bool | None = Field(default=None)
    is_business_name_valid: bool | None = Field(default=None)


class StoreResponseDataBusinessNameValidationStatus(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class AddressesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class AddressesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class AddressesResponseDataItemsItemCity(APIResponseSchema):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)


class AddressesResponseDataItemsItemState(APIResponseSchema):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)


class AddressesResponseDataMetaData(APIResponseSchema):
    can_delete_address: bool | None = Field(default=None)


class WarehousesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class WarehousesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class WarehousesResponseDataItemsItemState(APIResponseSchema):
    id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)


class DocumentsResponseDataTypesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    text: str | None = Field(default=None)
    has_expired_date: bool | None = Field(default=None)


class DocumentsResponseDataFilesItemStatus(APIResponseSchema):
    key: str | None = Field(default=None)
    title: str | None = Field(default=None)


class TrainingResponseDataTutorialVideosItem(APIResponseSchema):
    title: str | None = Field(default=None)
    link: str | None = Field(default=None)
    duration: str | None = Field(default=None)


class PerformanceResponseDataCustomerStatisfaction(APIResponseSchema):
    rate: int | None = Field(default=None)
    rate_count: int | None = Field(default=None)


class PerformanceResponseDataSummary(APIResponseSchema):
    delivered_on_time_percentage: float | None = Field(default=None)
    not_canceled_percentage: float | None = Field(default=None)
    not_returned_percentage: float | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    seller_id: int | None = Field(default=None)
    hashed_seller_id: str | None = Field(default=None)
    wallet_credit: int | None = Field(default=None)
    seller_name: str | None = Field(default=None)
    secondary_business_name: str | None = Field(default=None)
    seller_rating: float | None = Field(default=None)
    is_private: bool | None = Field(default=None)
    new_notifications: int | None = Field(default=None)
    new_questions: int | None = Field(default=None)
    verification: GetResponseDataVerification | None = Field(default=None)
    registration_status: str | None = Field(default=None)
    rejection_reasons: list[str] | None = Field(default=None)
    rejection_reasons_extra_message: str | None = Field(default=None)
    logo_rejection_reason: str | None = Field(default=None)
    description_rejection_reason: str | None = Field(default=None)
    register_phone: GetResponseDataRegisterPhone | None = Field(default=None)
    contract_status: GetResponseDataContractStatus | None = Field(default=None)
    has_password_expired: bool | None = Field(default=None)
    is_shipment_list_visible: bool | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    email: str | None = Field(default=None)
    phone: str | int | None = Field(default=None)
    state: str | None = Field(default=None)
    city: str | None = Field(default=None)
    birthday: str | None = Field(default=None)
    company: str | None = Field(default=None)
    is_new_seller: bool | None = Field(
        default=None, validation_alias="isNewSeller", serialization_alias="isNewSeller"
    )
    national_id: str | None = Field(default=None)
    registration_metadata: GetResponseDataRegistrationMetadata | None = Field(default=None)
    metadata: GetResponseDataMetadata | None = Field(default=None)
    subscription: GetResponseDataSubscription | None = Field(default=None)


class BusinessResponseData(APIResponseSchema):
    business_type: str | None = Field(default=None)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    national_id: str | None = Field(default=None)
    register_phone: str | None = Field(default=None)
    mobile_phone: str | None = Field(default=None)
    email: str | None = Field(default=None)
    verification_status: BusinessResponseDataVerificationStatus | None = Field(default=None)
    company_name: str | None = Field(default=None)
    company_type: BusinessResponseDataCompanyType | None = Field(default=None)
    company_registration_number: str | None = Field(default=None)
    company_national_id_number: str | None = Field(default=None)
    company_economic_number: str | None = Field(default=None)
    company_authorized_representative: str | None = Field(default=None)


class UpdateBusinessResponse(APIResponseSchema):
    status: str
    data: UpdateBusinessResponseData


class StoreResponseDataHolidaysItem(APIResponseSchema):
    id: int | None = Field(default=None)
    date: StoreResponseDataHolidaysItemDate | None = Field(default=None)
    active: bool | None = Field(default=None)
    live: bool | None = Field(default=None)


class StoreResponseDataWorkdaysItem(APIResponseSchema):
    id: int | None = Field(default=None)
    date: StoreResponseDataWorkdaysItemDate | None = Field(default=None)
    type: str | None = Field(default=None)
    active: bool | None = Field(default=None)
    is_not_passed: bool | None = Field(default=None)
    applied: bool | None = Field(default=None)


class AddressesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    city: AddressesResponseDataItemsItemCity | None = Field(default=None)
    state: AddressesResponseDataItemsItemState | None = Field(default=None)
    title: str | None = Field(default=None)
    address: str | None = Field(default=None)
    house_number: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)
    postal_code: str | int | None = Field(default=None)


class WarehousesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    latitude: float | None = Field(default=None)
    longitude: float | None = Field(default=None)
    description: str | None = Field(default=None)
    postal_code: str | int | None = Field(default=None)
    address: str | None = Field(default=None)
    house_number: str | int | None = Field(default=None)
    city: AddressesResponseDataItemsItemCity | None = Field(default=None)
    state: WarehousesResponseDataItemsItemState | None = Field(default=None)
    phone: str | None = Field(default=None)
    is_return_address: bool | None = Field(default=None)


class DocumentsResponseDataFilesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    document_title: str | None = Field(default=None)
    image_src: str | None = Field(default=None)
    status: DocumentsResponseDataFilesItemStatus | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    expires_at_persian: str | None = Field(default=None)
    document_id: int | None = Field(default=None)
    unlimited: bool | None = Field(default=None)


class TrainingResponseData(APIResponseSchema):
    status: str | None = Field(default=None)
    date: StoreResponseDataWorkdaysItemDate | None = Field(default=None)
    type: str | None = Field(default=None)
    has_finished_survey: bool | None = Field(default=None)
    has_one_more_person: bool | None = Field(default=None)
    has_sales_experience: bool | None = Field(default=None)
    class_link: str | None = Field(default=None)
    tutorial_videos: list[TrainingResponseDataTutorialVideosItem] | None = Field(default=None)


class PerformanceResponseData(APIResponseSchema):
    five_start_rate: float | None = Field(default=None)
    customer_statisfaction: PerformanceResponseDataCustomerStatisfaction | None = Field(
        default=None
    )
    summary: PerformanceResponseDataSummary | None = Field(default=None)


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class BusinessResponse(APIResponseSchema):
    status: int | str
    data: BusinessResponseData


class StoreResponseData(APIResponseSchema):
    seller_type: str | None = Field(default=None)
    seller_code: int | None = Field(default=None)
    business_name: str | None = Field(default=None)
    secondary_business_name: str | None = Field(default=None)
    page_slug: str | None = Field(default=None)
    cover_color_top: str | None = Field(default=None)
    cover_color_bottom: str | None = Field(default=None)
    description: StoreResponseDataDescription | None = Field(default=None)
    holidays: list[StoreResponseDataHolidaysItem] | None = Field(default=None)
    workdays: list[StoreResponseDataWorkdaysItem] | None = Field(default=None)
    phone: str | None = Field(default=None)
    website: str | None = Field(default=None)
    logo: StoreResponseDataLogo | None = Field(default=None)
    registration_status: StoreResponseDataRegistrationStatus | None = Field(default=None)
    business_name_changed_at: str | None = Field(default=None)
    brand_name: str | None = Field(default=None)
    ig_handle: str | None = Field(default=None)
    business_name_validation_status: StoreResponseDataBusinessNameValidationStatus | None = Field(
        default=None
    )


class AddressesResponseData(APIResponseSchema):
    sort_data: AddressesResponseDataSortData | None = Field(default=None)
    pager: AddressesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[AddressesResponseDataItemsItem] | None = Field(default=None)
    meta_data: AddressesResponseDataMetaData | None = Field(default=None)


class WarehousesResponseData(APIResponseSchema):
    sort_data: WarehousesResponseDataSortData | None = Field(default=None)
    pager: WarehousesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[WarehousesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class DocumentsResponseData(APIResponseSchema):
    business_type: str | None = Field(default=None)
    types: list[DocumentsResponseDataTypesItem] | None = Field(default=None)
    files: list[DocumentsResponseDataFilesItem] | None = Field(default=None)


class TrainingResponse(APIResponseSchema):
    status: int | str
    data: TrainingResponseData


class PerformanceResponse(APIResponseSchema):
    status: int | str
    data: PerformanceResponseData


class StoreResponse(APIResponseSchema):
    status: int | str
    data: StoreResponseData


class AddressesResponse(APIResponseSchema):
    status: str
    data: AddressesResponseData


class WarehousesResponse(APIResponseSchema):
    status: str
    data: WarehousesResponseData


class DocumentsResponse(APIResponseSchema):
    status: int | str
    data: DocumentsResponseData


__all__ = [
    "AddressesResponse",
    "AddressesResponseData",
    "AddressesResponseDataItemsItem",
    "AddressesResponseDataItemsItemCity",
    "AddressesResponseDataItemsItemState",
    "AddressesResponseDataMetaData",
    "AddressesResponseDataPager",
    "AddressesResponseDataSortData",
    "BusinessResponse",
    "BusinessResponseData",
    "BusinessResponseDataCompanyType",
    "BusinessResponseDataVerificationStatus",
    "DocumentsResponse",
    "DocumentsResponseData",
    "DocumentsResponseDataFilesItem",
    "DocumentsResponseDataFilesItemStatus",
    "DocumentsResponseDataTypesItem",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataContractStatus",
    "GetResponseDataMetadata",
    "GetResponseDataRegisterPhone",
    "GetResponseDataRegistrationMetadata",
    "GetResponseDataSubscription",
    "GetResponseDataVerification",
    "PerformanceResponse",
    "PerformanceResponseData",
    "PerformanceResponseDataCustomerStatisfaction",
    "PerformanceResponseDataSummary",
    "StoreResponse",
    "StoreResponseData",
    "StoreResponseDataBusinessNameValidationStatus",
    "StoreResponseDataDescription",
    "StoreResponseDataHolidaysItem",
    "StoreResponseDataHolidaysItemDate",
    "StoreResponseDataLogo",
    "StoreResponseDataRegistrationStatus",
    "StoreResponseDataWorkdaysItem",
    "StoreResponseDataWorkdaysItemDate",
    "TrainingResponse",
    "TrainingResponseData",
    "TrainingResponseDataTutorialVideosItem",
    "UpdateBusinessRequest",
    "UpdateBusinessResponse",
    "UpdateBusinessResponseData",
    "WarehousesResponse",
    "WarehousesResponseData",
    "WarehousesResponseDataItemsItem",
    "WarehousesResponseDataItemsItemState",
    "WarehousesResponseDataPager",
    "WarehousesResponseDataSortData",
]
