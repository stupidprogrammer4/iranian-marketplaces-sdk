"""Digikala bulk shipping: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
)


class CancelOrderRequest(RequestSchema):
    registration_method: str | list[JsonValue] | None = Field(default=None)
    deactivate_parcel: bool | None = Field(default=None)


class PackageRequest(RequestSchema):
    shipment_id: int
    parcel: list[JsonValue] | None = Field(default=None)


class BulkPackageRequest(RequestSchema):
    shipments_data: list[JsonValue]


class SimplePackageRequest(RequestSchema):
    shipment_ids: list[JsonValue]
    box_size_id: int
    total_weight: JsonValue
    width: float | None = Field(default=None)
    height: float | None = Field(default=None)
    length: float | None = Field(default=None)


class PickupRequest(RequestSchema):
    pickup_method: str | list[JsonValue]
    shipment_ids: list[JsonValue]
    ready_date_time: JsonValue
    warehouse_id: int
    promise_date_start: str | None = Field(default=None)
    promise_date_end: str | None = Field(default=None)


class DetailQuery(QuerySchema):
    shipment_ids: list[int]


class DetailResponseDataShippingNature(APIResponseSchema):
    title: str | None = Field(default=None)
    text: str | None = Field(default=None)


class DetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem(APIResponseSchema):
    product_variant_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    image: str | None = Field(default=None)
    product_url: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    quantity: int | None = Field(default=None)


class PromiseDateQuery(QuerySchema):
    shipment_ids: list[int]


class DetailResponseDataShippingServiceOrderDetailParcelInfoItem(APIResponseSchema):
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
        list[DetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem] | None
    ) = Field(default=None)
    is_printable: bool | None = Field(default=None)


class DetailResponseDataShippingServiceOrderDetail(APIResponseSchema):
    service: str | None = Field(default=None)
    is_cancellable: bool | None = Field(default=None)
    service_infra_type: str | None = Field(default=None)
    status: str | None = Field(default=None)
    shipping_service_status: str | None = Field(default=None)
    parcel_info: list[DetailResponseDataShippingServiceOrderDetailParcelInfoItem] | None = Field(
        default=None
    )
    pickup_start_date: str | None = Field(default=None)
    pickup_end_date: str | None = Field(default=None)
    total_price: int | None = Field(default=None)


class DetailResponseData(APIResponseSchema):
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
    shipping_nature: DetailResponseDataShippingNature | None = Field(default=None)
    shipping_service_order_detail: DetailResponseDataShippingServiceOrderDetail | None = Field(
        default=None
    )


class DetailResponse(APIResponseSchema):
    status: int | str
    data: DetailResponseData


__all__ = [
    "BulkPackageRequest",
    "CancelOrderRequest",
    "DetailQuery",
    "DetailResponse",
    "DetailResponseData",
    "DetailResponseDataShippingNature",
    "DetailResponseDataShippingServiceOrderDetail",
    "DetailResponseDataShippingServiceOrderDetailParcelInfoItem",
    "DetailResponseDataShippingServiceOrderDetailParcelInfoItemVariantsItem",
    "PackageRequest",
    "PickupRequest",
    "PromiseDateQuery",
    "SimplePackageRequest",
]
