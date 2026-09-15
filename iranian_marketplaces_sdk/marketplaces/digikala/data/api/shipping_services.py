"""Digikala shipping services: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class VerifyWalletRequest(RequestSchema):
    payment_id: str
    order_no: int
    error_message: str | None = Field(default=None)


class BoxesQuery(QuerySchema):
    shipment_id: int | None = Field(default=None)


class BoxesResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class BoxesResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class BoxesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    size_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    length: int | None = Field(default=None)


class BulkTrackingCodesRequest(RequestSchema):
    order_shipment_ids: list[int]
    warehouse_id: int


class ImportParcelsRequest(RequestSchema):
    order_shipment_ids: list[int]


class CalculateCostRequest(RequestSchema):
    order_shipment_ids: list[int]
    warehouse_id: int
    request_type: str | None = Field(default=None)


class OrderDetailQuery(QuerySchema):
    order_id: int


class OrderDetailResponseDataShippingNature(APIResponseSchema):
    title: str | None = Field(default=None)
    text: str | None = Field(default=None)


class OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem(
    APIResponseSchema
):
    product_variant_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    image: str | None = Field(default=None)
    quantity: int | None = Field(default=None)


class RequestLabelRequest(RequestSchema):
    shipment_ids: list[JsonValue]


class BoxesResponseData(APIResponseSchema):
    sort_data: BoxesResponseDataSortData | None = Field(default=None)
    pager: BoxesResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[BoxesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItem(APIResponseSchema):
    box_size_name: str | None = Field(default=None)
    shipping_service_order_id: int | None = Field(default=None)
    shipping_service_shipment_id: int | None = Field(default=None)
    weight: int | None = Field(default=None)
    is_fragile: bool | None = Field(default=None)
    is_liquid: bool | None = Field(default=None)
    parcel_number: str | None = Field(default=None)
    tracking_code: str | None = Field(default=None)
    price: int | None = Field(default=None)
    variants: (
        list[OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem] | None
    ) = Field(default=None)
    is_printable: bool | None = Field(default=None)


class BoxesResponse(APIResponseSchema):
    status: str
    data: BoxesResponseData


class OrderDetailResponseDataShippingServiceOrderDetail(APIResponseSchema):
    service: str | None = Field(default=None)
    status: str | None = Field(default=None)
    shipping_service_status: str | None = Field(default=None)
    parcel_info: list[OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItem] | None = (
        Field(default=None)
    )
    pickup_start_date: str | None = Field(default=None)
    pickup_end_date: str | None = Field(default=None)
    total_price: int | None = Field(default=None)


class OrderDetailResponseData(APIResponseSchema):
    order_id: int | None = Field(default=None)
    order_shipment_id: int | None = Field(default=None)
    created_at: str | None = Field(default=None)
    promise_date: str | None = Field(default=None)
    city_name: str | None = Field(default=None)
    state_name: str | None = Field(default=None)
    shipment_type: str | None = Field(default=None)
    count_variants_in_shipment: int | None = Field(default=None)
    order_shipment_price: int | None = Field(default=None)
    shipment_status: str | None = Field(default=None)
    shipping_nature: OrderDetailResponseDataShippingNature | None = Field(default=None)
    shipping_service_order_detail: OrderDetailResponseDataShippingServiceOrderDetail | None = Field(
        default=None
    )


class OrderDetailResponse(APIResponseSchema):
    status: int | str
    data: OrderDetailResponseData


__all__ = [
    "BoxesQuery",
    "BoxesResponse",
    "BoxesResponseData",
    "BoxesResponseDataItemsItem",
    "BoxesResponseDataPager",
    "BoxesResponseDataSortData",
    "BulkTrackingCodesRequest",
    "CalculateCostRequest",
    "ImportParcelsRequest",
    "OrderDetailQuery",
    "OrderDetailResponse",
    "OrderDetailResponseData",
    "OrderDetailResponseDataShippingNature",
    "OrderDetailResponseDataShippingServiceOrderDetail",
    "OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItem",
    "OrderDetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem",
    "RequestLabelRequest",
    "VerifyWalletRequest",
]
