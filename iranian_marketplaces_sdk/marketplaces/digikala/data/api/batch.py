"""Digikala batch: request and response models."""

from __future__ import annotations

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class InquiryRequest(RequestSchema):
    batch_id: int


class InquiryResponseDataItemsItem(APIResponseSchema):
    key: int | None = Field(default=None)
    status: str | None = Field(default=None)
    errors: ObjectMap[JsonValue] | None = Field(default=None)


class UpdateVariantsRequestItemsItemPayload(RequestSchema):
    seller_stock: int | None = Field(default=None)
    maximum_per_order: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    shipping_type: str | None = Field(default=None)
    lead_time: int | None = Field(default=None)
    seller_lead_time: int | None = Field(default=None)
    three_hour_delivery: bool | None = Field(default=None)


class UpdateVariantsResponseData(APIResponseSchema):
    batch_id: int | None = Field(default=None)
    status: str | None = Field(default=None)


class UpdateActivationRequestItemsItemPayload(RequestSchema):
    activation: bool


class UpdateActivationResponse(APIResponseSchema):
    status: str
    data: UpdateVariantsResponseData


class UpdateStockRequestItemsItemPayload(RequestSchema):
    seller_stock: int


class UpdateStockResponse(APIResponseSchema):
    status: str
    data: UpdateVariantsResponseData


class InquiryResponseData(APIResponseSchema):
    batch_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    items: list[InquiryResponseDataItemsItem] | None = Field(default=None)


class UpdateVariantsRequestItemsItem(RequestSchema):
    variant_id: int | None = Field(default=None)
    payload: UpdateVariantsRequestItemsItemPayload | None = Field(default=None)


class UpdateVariantsResponse(APIResponseSchema):
    status: str
    data: UpdateVariantsResponseData


class UpdateActivationRequestItemsItem(RequestSchema):
    variant_id: int | None = Field(default=None)
    payload: UpdateActivationRequestItemsItemPayload | None = Field(default=None)


class UpdateStockRequestItemsItem(RequestSchema):
    variant_id: int | None = Field(default=None)
    payload: UpdateStockRequestItemsItemPayload | None = Field(default=None)


class InquiryResponse(APIResponseSchema):
    status: str
    data: InquiryResponseData


class UpdateVariantsRequest(RequestSchema):
    deadline: int | None = Field(default=None)
    items: list[UpdateVariantsRequestItemsItem]


class UpdateActivationRequest(RequestSchema):
    deadline: int | None = Field(default=None)
    items: list[UpdateActivationRequestItemsItem]


class UpdateStockRequest(RequestSchema):
    deadline: int | None = Field(default=None)
    items: list[UpdateStockRequestItemsItem]


__all__ = [
    "InquiryRequest",
    "InquiryResponse",
    "InquiryResponseData",
    "InquiryResponseDataItemsItem",
    "UpdateActivationRequest",
    "UpdateActivationRequestItemsItem",
    "UpdateActivationRequestItemsItemPayload",
    "UpdateActivationResponse",
    "UpdateStockRequest",
    "UpdateStockRequestItemsItem",
    "UpdateStockRequestItemsItemPayload",
    "UpdateStockResponse",
    "UpdateVariantsRequest",
    "UpdateVariantsRequestItemsItem",
    "UpdateVariantsRequestItemsItemPayload",
    "UpdateVariantsResponse",
    "UpdateVariantsResponseData",
]
