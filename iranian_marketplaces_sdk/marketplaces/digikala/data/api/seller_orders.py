"""Digikala seller orders: request and response models."""

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
    sort: Literal["id", "order_date", "promise_date", "order_id", "shipment_id"] | None = Field(
        default=None
    )
    order: str | None = Field(default=None)
    search_status: Literal["pending", "processed", "processing", "edited", "rejected"] | None = (
        Field(default=None, validation_alias="search[status]", serialization_alias="search[status]")
    )
    search_search_term: str | None = Field(
        default=None,
        validation_alias="search[search_term]",
        serialization_alias="search[search_term]",
    )
    search_shipping_provider: Literal["seller", "seller_post"] | None = Field(
        default=None,
        validation_alias="search[shipping_provider]",
        serialization_alias="search[shipping_provider]",
    )
    search_past: Literal[True, False] | None = Field(
        default=None, validation_alias="search[past]", serialization_alias="search[past]"
    )
    search_future: str | None = Field(
        default=None, validation_alias="search[future]", serialization_alias="search[future]"
    )
    search_time_scope_id: int | None = Field(
        default=None,
        validation_alias="search[time_scope_id]",
        serialization_alias="search[time_scope_id]",
    )
    search_category_ids: list[int] | None = Field(
        default=None,
        validation_alias="search[category_ids]",
        serialization_alias="search[category_ids]",
    )
    search_is_b2b: Literal[True, False] | None = Field(
        default=None, validation_alias="search[is_b2b]", serialization_alias="search[is_b2b]"
    )
    search_critical_only: Literal[True, False] | None = Field(
        default=None,
        validation_alias="search[critical_only]",
        serialization_alias="search[critical_only]",
    )
    search_min_shipment_id: int | None = Field(
        default=None,
        validation_alias="search[min_shipment_id]",
        serialization_alias="search[min_shipment_id]",
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


class ListResponseDataItemsItemAddress(APIResponseSchema):
    state: str | None = Field(default=None)
    city: str | None = Field(default=None)
    district: str | None = Field(default=None)


class ListResponseDataItemsItemShippingNature(APIResponseSchema):
    title: str | int | None = Field(default=None)
    text: str | None = Field(default=None)
    type: str | None = Field(default=None)


class ListResponseDataItemsItemStatus(APIResponseSchema):
    text: str | None = Field(default=None)
    text_fa: str | None = Field(default=None)
    level: str | None = Field(default=None)


class ListResponseDataItemsItemVariantsItemShippingNature(APIResponseSchema):
    title: str | int | None = Field(default=None)
    text: str | None = Field(default=None)
    type: str | None = Field(default=None)


class ListResponseDataItemsItemVariantsItemCancellationReasonsOptionItem(APIResponseSchema):
    text: str | None = Field(default=None)
    value: int | None = Field(default=None)


class ListResponseDataItemsItemItemRejectionOptionsItem(APIResponseSchema):
    text: str | None = Field(default=None)
    value: int | None = Field(default=None)


class ListResponseDataItemsItemShipmentRejectionOptionsItem(APIResponseSchema):
    text: str | None = Field(default=None)
    value: int | None = Field(default=None)


class ListResponseDataItemsItemFailedShipmentOptionsItem(APIResponseSchema):
    text: str | None = Field(default=None)
    value: int | None = Field(default=None)


class StatisticsResponseDataShipmentsPerDay(APIResponseSchema):
    yyyy_mm_dd: int | None = Field(
        default=None, validation_alias="YYYY-MM-DD", serialization_alias="YYYY-MM-DD"
    )


class CustomerResponseData(APIResponseSchema):
    name: str | None = Field(default=None)
    state: str | None = Field(default=None)
    city: str | None = Field(default=None)
    address: str | None = Field(default=None)
    postal_code: str | None = Field(
        default=None, validation_alias="postalCode", serialization_alias="postalCode"
    )
    phone_number: str | None = Field(
        default=None, validation_alias="phoneNumber", serialization_alias="phoneNumber"
    )
    shipping_cost: int | None = Field(
        default=None, validation_alias="shippingCost", serialization_alias="shippingCost"
    )


class PostDataResponseDataAddress(APIResponseSchema):
    state: str | None = Field(default=None)
    city: str | None = Field(default=None)


class TimeScopesResponseData(APIResponseSchema):
    value: int | None = Field(default=None)
    text: str | None = Field(default=None)


class FailedDeliveryTimeScopesResponseDataTimescopesItem(APIResponseSchema):
    id: int | None = Field(default=None)
    text: str | None = Field(default=None)


class CancelItemRequest(RequestSchema):
    order_shipment_id: int
    item_id: int
    reason_id: int
    count: int | None = Field(default=None)


class CancelShipmentRequest(RequestSchema):
    order_shipment_id: int
    reason_id: int


class UpdateTrackingCodeRequestTrackingCodesItem(RequestSchema):
    id: int | None = Field(default=None)
    tracking_code: str | None = Field(default=None)


class UpdateStatusRequest(RequestSchema):
    order_shipment_id: int
    new_status: str
    verification_code: int | None = Field(default=None)


class MarkDeliveredRequest(RequestSchema):
    order_shipment_id: int
    tracking_codes: list[str]


class UpdateEditedRequest(RequestSchema):
    order_shipment_id: int


class ReportFailedDeliveryRequest(RequestSchema):
    order_shipment_id: int
    reason_id: int
    capacity_id: int


class ChangeTimeScopeRequest(RequestSchema):
    order_shipment_id: int
    capacity_id: int


class PostOrderResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)


class BatchUpdateStatusRequest(RequestSchema):
    order_shipment_ids: list[JsonValue] | None = Field(default=None)
    new_status: str
    select_all: bool | None = Field(default=None)


class ListResponseDataItemsItemVariantsItem(APIResponseSchema):
    image_url: str | None = Field(default=None)
    title: str | None = Field(default=None)
    theme: str | None = Field(default=None)
    size: str | None = Field(default=None)
    product_id: int | str | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    product_url: str | None = Field(
        default=None, validation_alias="productUrl", serialization_alias="productUrl"
    )
    variant_id: int | None = Field(
        default=None, validation_alias="variantId", serialization_alias="variantId"
    )
    seller_code: int | None = Field(
        default=None, validation_alias="sellerCode", serialization_alias="sellerCode"
    )
    lead_time: int | None = Field(
        default=None, validation_alias="leadTime", serialization_alias="leadTime"
    )
    shipping_nature: ListResponseDataItemsItemVariantsItemShippingNature | None = Field(
        default=None, validation_alias="shippingNature", serialization_alias="shippingNature"
    )
    count: int | None = Field(default=None)
    price: int | None = Field(default=None)
    order_item_id: int | None = Field(
        default=None, validation_alias="orderItemId", serialization_alias="orderItemId"
    )
    cancellation_id: int | None = Field(default=None)
    cancellation_reason: str | None = Field(default=None)
    cancellation_status: bool | None = Field(default=None)
    cancellation_reasons_option: (
        list[ListResponseDataItemsItemVariantsItemCancellationReasonsOptionItem] | None
    ) = Field(default=None)


class StatisticsResponseData(APIResponseSchema):
    shipments_per_day: StatisticsResponseDataShipmentsPerDay | None = Field(default=None)
    latest_shipment_diff: int | None = Field(default=None)


class GetResponseData(APIResponseSchema):
    row_index: int | None = Field(
        default=None, validation_alias="rowIndex", serialization_alias="rowIndex"
    )
    order_id: int | None = Field(
        default=None, validation_alias="orderId", serialization_alias="orderId"
    )
    shipment_id: int | None = Field(
        default=None, validation_alias="shipmentId", serialization_alias="shipmentId"
    )
    order_date: str | None = Field(
        default=None, validation_alias="orderDate", serialization_alias="orderDate"
    )
    post_promise_date: str | None = Field(
        default=None, validation_alias="postPromiseDate", serialization_alias="postPromiseDate"
    )
    digiexpress_allowed_date: str | None = Field(default=None)
    digiexpress_promise_date: str | None = Field(
        default=None,
        validation_alias="digiexpressPromiseDate",
        serialization_alias="digiexpressPromiseDate",
    )
    delivery_date: str | None = Field(
        default=None, validation_alias="deliveryDate", serialization_alias="deliveryDate"
    )
    promise_date: str | None = Field(
        default=None, validation_alias="promiseDate", serialization_alias="promiseDate"
    )
    address: ListResponseDataItemsItemAddress | None = Field(default=None)
    shipping_provider: str | None = Field(
        default=None, validation_alias="shippingProvider", serialization_alias="shippingProvider"
    )
    tracking_code: str | None = Field(
        default=None, validation_alias="trackingCode", serialization_alias="trackingCode"
    )
    tracking_code_status: str | None = Field(
        default=None,
        validation_alias="trackingCodeStatus",
        serialization_alias="trackingCodeStatus",
    )
    post_or_digiexpress_status: list[JsonValue] | None = Field(
        default=None,
        validation_alias="postOrDigiexpressStatus",
        serialization_alias="postOrDigiexpressStatus",
    )
    shipping_nature: ListResponseDataItemsItemShippingNature | None = Field(
        default=None, validation_alias="shippingNature", serialization_alias="shippingNature"
    )
    item_count: int | None = Field(
        default=None, validation_alias="itemCount", serialization_alias="itemCount"
    )
    shipping_cost: int | None = Field(
        default=None, validation_alias="shippingCost", serialization_alias="shippingCost"
    )
    status: ListResponseDataItemsItemStatus | None = Field(default=None)
    edited: bool | None = Field(default=None)
    is_cancelled: bool | None = Field(
        default=None, validation_alias="isCancelled", serialization_alias="isCancelled"
    )
    has_failed_delivery_before: bool | None = Field(
        default=None,
        validation_alias="hasFailedDeliveryBefore",
        serialization_alias="hasFailedDeliveryBefore",
    )
    next_status: str | None = Field(
        default=None, validation_alias="nextStatus", serialization_alias="nextStatus"
    )
    variants: list[ListResponseDataItemsItemVariantsItem] | None = Field(default=None)
    is_delayed: bool | None = Field(
        default=None, validation_alias="isDelayed", serialization_alias="isDelayed"
    )
    is_order_locked: bool | None = Field(
        default=None, validation_alias="isOrderLocked", serialization_alias="isOrderLocked"
    )
    item_rejection_options: list[ListResponseDataItemsItemItemRejectionOptionsItem] | None = Field(
        default=None,
        validation_alias="itemRejectionOptions",
        serialization_alias="itemRejectionOptions",
    )
    shipment_rejection_options: (
        list[ListResponseDataItemsItemShipmentRejectionOptionsItem] | None
    ) = Field(
        default=None,
        validation_alias="shipmentRejectionOptions",
        serialization_alias="shipmentRejectionOptions",
    )
    is_failed_delivery_available: bool | None = Field(
        default=None,
        validation_alias="isFailedDeliveryAvailable",
        serialization_alias="isFailedDeliveryAvailable",
    )
    is_failed_delivery_button_active: bool | None = Field(
        default=None,
        validation_alias="isFailedDeliveryButtonActive",
        serialization_alias="isFailedDeliveryButtonActive",
    )
    failed_shipment_options: list[ListResponseDataItemsItemFailedShipmentOptionsItem] | None = (
        Field(
            default=None,
            validation_alias="failedShipmentOptions",
            serialization_alias="failedShipmentOptions",
        )
    )
    is_cancelling: bool | None = Field(
        default=None, validation_alias="isCancelling", serialization_alias="isCancelling"
    )
    verification_code: str | None = Field(
        default=None, validation_alias="verificationCode", serialization_alias="verificationCode"
    )
    edit_reasons: str | None = Field(
        default=None, validation_alias="editReasons", serialization_alias="editReasons"
    )
    digiexpress_ability: bool | None = Field(default=None)
    digiexpress_data: list[JsonValue] | None = Field(
        default=None, validation_alias="digiexpressData", serialization_alias="digiexpressData"
    )
    business_type: str | None = Field(default=None)
    is_digi_express: bool | None = Field(
        default=None, validation_alias="isDigiExpress", serialization_alias="isDigiExpress"
    )
    customer_name: str | None = Field(default=None)
    customer_address: str | None = Field(default=None)
    customer_postal_code: str | None = Field(default=None)
    customer_phone_number: str | None = Field(default=None)
    is_digiexpress_shipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isDigiexpressShippingServiceActive",
        serialization_alias="isDigiexpressShippingServiceActive",
    )
    is_postex_shipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isPostexShippingServiceActive",
        serialization_alias="isPostexShippingServiceActive",
    )
    is_fbmshipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isFBMShippingServiceActive",
        serialization_alias="isFBMShippingServiceActive",
    )
    show_parcel_data: bool | None = Field(
        default=None, validation_alias="showParcelData", serialization_alias="showParcelData"
    )


class CustomerResponse(APIResponseSchema):
    status: int | str
    data: CustomerResponseData


class PostDataResponseData(APIResponseSchema):
    address: PostDataResponseDataAddress | None = Field(default=None)
    weight: int | None = Field(default=None)


class TimeScopesResponse(APIResponseSchema):
    status: int | str
    data: TimeScopesResponseData


class FailedDeliveryTimeScopesResponseData(APIResponseSchema):
    timescopes: list[FailedDeliveryTimeScopesResponseDataTimescopesItem] | None = Field(
        default=None
    )


class UpdateTrackingCodeRequest(RequestSchema):
    order_shipment_id: int
    tracking_codes: list[UpdateTrackingCodeRequestTrackingCodesItem]
    infra_type: str | None = Field(default=None)
    service_name: str | None = Field(default=None)


class PostOrderResponse(APIResponseSchema):
    status: int | str
    data: PostOrderResponseData


class ListResponseDataItemsItem(APIResponseSchema):
    row_index: int | None = Field(
        default=None, validation_alias="rowIndex", serialization_alias="rowIndex"
    )
    order_id: int | None = Field(
        default=None, validation_alias="orderId", serialization_alias="orderId"
    )
    shipment_id: int | None = Field(
        default=None, validation_alias="shipmentId", serialization_alias="shipmentId"
    )
    order_date: str | None = Field(
        default=None, validation_alias="orderDate", serialization_alias="orderDate"
    )
    post_promise_date: str | None = Field(
        default=None, validation_alias="postPromiseDate", serialization_alias="postPromiseDate"
    )
    digiexpress_allowed_date: str | None = Field(default=None)
    digiexpress_promise_date: str | None = Field(
        default=None,
        validation_alias="digiexpressPromiseDate",
        serialization_alias="digiexpressPromiseDate",
    )
    delivery_date: str | None = Field(
        default=None, validation_alias="deliveryDate", serialization_alias="deliveryDate"
    )
    promise_date: str | None = Field(
        default=None, validation_alias="promiseDate", serialization_alias="promiseDate"
    )
    address: ListResponseDataItemsItemAddress | None = Field(default=None)
    shipping_provider: str | None = Field(
        default=None, validation_alias="shippingProvider", serialization_alias="shippingProvider"
    )
    tracking_code: str | None = Field(
        default=None, validation_alias="trackingCode", serialization_alias="trackingCode"
    )
    tracking_code_status: str | None = Field(
        default=None,
        validation_alias="trackingCodeStatus",
        serialization_alias="trackingCodeStatus",
    )
    post_or_digiexpress_status: list[JsonValue] | None = Field(
        default=None,
        validation_alias="postOrDigiexpressStatus",
        serialization_alias="postOrDigiexpressStatus",
    )
    shipping_nature: ListResponseDataItemsItemShippingNature | None = Field(
        default=None, validation_alias="shippingNature", serialization_alias="shippingNature"
    )
    item_count: int | None = Field(
        default=None, validation_alias="itemCount", serialization_alias="itemCount"
    )
    shipping_cost: int | None = Field(
        default=None, validation_alias="shippingCost", serialization_alias="shippingCost"
    )
    status: ListResponseDataItemsItemStatus | None = Field(default=None)
    edited: bool | None = Field(default=None)
    is_cancelled: bool | None = Field(
        default=None, validation_alias="isCancelled", serialization_alias="isCancelled"
    )
    has_failed_delivery_before: bool | None = Field(
        default=None,
        validation_alias="hasFailedDeliveryBefore",
        serialization_alias="hasFailedDeliveryBefore",
    )
    next_status: str | None = Field(
        default=None, validation_alias="nextStatus", serialization_alias="nextStatus"
    )
    variants: list[ListResponseDataItemsItemVariantsItem] | None = Field(default=None)
    is_delayed: bool | None = Field(
        default=None, validation_alias="isDelayed", serialization_alias="isDelayed"
    )
    is_order_locked: bool | None = Field(
        default=None, validation_alias="isOrderLocked", serialization_alias="isOrderLocked"
    )
    item_rejection_options: list[ListResponseDataItemsItemItemRejectionOptionsItem] | None = Field(
        default=None,
        validation_alias="itemRejectionOptions",
        serialization_alias="itemRejectionOptions",
    )
    shipment_rejection_options: (
        list[ListResponseDataItemsItemShipmentRejectionOptionsItem] | None
    ) = Field(
        default=None,
        validation_alias="shipmentRejectionOptions",
        serialization_alias="shipmentRejectionOptions",
    )
    is_failed_delivery_available: bool | None = Field(
        default=None,
        validation_alias="isFailedDeliveryAvailable",
        serialization_alias="isFailedDeliveryAvailable",
    )
    is_failed_delivery_button_active: bool | None = Field(
        default=None,
        validation_alias="isFailedDeliveryButtonActive",
        serialization_alias="isFailedDeliveryButtonActive",
    )
    failed_shipment_options: list[ListResponseDataItemsItemFailedShipmentOptionsItem] | None = (
        Field(
            default=None,
            validation_alias="failedShipmentOptions",
            serialization_alias="failedShipmentOptions",
        )
    )
    is_cancelling: bool | None = Field(
        default=None, validation_alias="isCancelling", serialization_alias="isCancelling"
    )
    verification_code: str | None = Field(
        default=None, validation_alias="verificationCode", serialization_alias="verificationCode"
    )
    edit_reasons: str | None = Field(
        default=None, validation_alias="editReasons", serialization_alias="editReasons"
    )
    digiexpress_ability: bool | None = Field(default=None)
    digiexpress_data: list[JsonValue] | None = Field(
        default=None, validation_alias="digiexpressData", serialization_alias="digiexpressData"
    )
    business_type: str | None = Field(default=None)
    is_digi_express: bool | None = Field(
        default=None, validation_alias="isDigiExpress", serialization_alias="isDigiExpress"
    )
    customer_name: str | None = Field(default=None)
    customer_address: str | None = Field(default=None)
    customer_postal_code: str | None = Field(default=None)
    customer_phone_number: str | None = Field(default=None)
    is_digiexpress_shipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isDigiexpressShippingServiceActive",
        serialization_alias="isDigiexpressShippingServiceActive",
    )
    is_postex_shipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isPostexShippingServiceActive",
        serialization_alias="isPostexShippingServiceActive",
    )
    is_fbmshipping_service_active: bool | None = Field(
        default=None,
        validation_alias="isFBMShippingServiceActive",
        serialization_alias="isFBMShippingServiceActive",
    )
    show_parcel_data: bool | None = Field(
        default=None, validation_alias="showParcelData", serialization_alias="showParcelData"
    )


class StatisticsResponse(APIResponseSchema):
    status: int | str
    data: StatisticsResponseData


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


class PostDataResponse(APIResponseSchema):
    status: int | str
    data: PostDataResponseData


class FailedDeliveryTimeScopesResponse(APIResponseSchema):
    status: int | str
    data: FailedDeliveryTimeScopesResponseData


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
    "BatchUpdateStatusRequest",
    "CancelItemRequest",
    "CancelShipmentRequest",
    "ChangeTimeScopeRequest",
    "CustomerResponse",
    "CustomerResponseData",
    "FailedDeliveryTimeScopesResponse",
    "FailedDeliveryTimeScopesResponseData",
    "FailedDeliveryTimeScopesResponseDataTimescopesItem",
    "GetResponse",
    "GetResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemAddress",
    "ListResponseDataItemsItemFailedShipmentOptionsItem",
    "ListResponseDataItemsItemItemRejectionOptionsItem",
    "ListResponseDataItemsItemShipmentRejectionOptionsItem",
    "ListResponseDataItemsItemShippingNature",
    "ListResponseDataItemsItemStatus",
    "ListResponseDataItemsItemVariantsItem",
    "ListResponseDataItemsItemVariantsItemCancellationReasonsOptionItem",
    "ListResponseDataItemsItemVariantsItemShippingNature",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "MarkDeliveredRequest",
    "PostDataResponse",
    "PostDataResponseData",
    "PostDataResponseDataAddress",
    "PostOrderResponse",
    "PostOrderResponseData",
    "ReportFailedDeliveryRequest",
    "StatisticsResponse",
    "StatisticsResponseData",
    "StatisticsResponseDataShipmentsPerDay",
    "TimeScopesResponse",
    "TimeScopesResponseData",
    "UpdateEditedRequest",
    "UpdateStatusRequest",
    "UpdateTrackingCodeRequest",
    "UpdateTrackingCodeRequestTrackingCodesItem",
]
