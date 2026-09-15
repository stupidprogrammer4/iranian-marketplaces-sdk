"""Digikala webhooks: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from iranian_marketplaces_sdk.common.data import RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class EventTypesResponseData(APIResponseSchema):
    all_event_types: ObjectMap[str] | None = Field(default=None)
    allowed_event_types: list[str] | None = Field(default=None)
    active_event_types: list[str] | None = Field(default=None)
    activation_status: str | None = Field(default=None)


class SubscribeRequest(RequestSchema):
    event_types: (
        list[
            Literal[
                "product_variant_status_change",
                "order_shipment",
                "seller_package_status_change",
                "commission_change",
                "product_moderation",
                "brand_request_moderation",
                "warranty_request_moderation",
                "color_request_moderation",
                "size_request_moderation",
                "order_processed",
                "order_item_cancellation",
                "order_return",
            ]
        ]
        | None
    ) = Field(default=None)


class SubscribeResponseData(APIResponseSchema):
    status: str | None = Field(default=None)


class UnsubscribeRequest(RequestSchema):
    event_types: (
        list[
            Literal[
                "product_variant_status_change",
                "order_shipment",
                "seller_package_status_change",
                "commission_change",
                "product_moderation",
                "brand_request_moderation",
                "warranty_request_moderation",
                "color_request_moderation",
                "size_request_moderation",
                "order_processed",
                "order_item_cancellation",
                "order_return",
            ]
        ]
        | None
    ) = Field(default=None)


class UnsubscribeResponseData(APIResponseSchema):
    status: str | None = Field(default=None)


class ChangeActivationRequest(RequestSchema):
    activation: bool | None = Field(default=None)


class ChangeActivationResponseData(APIResponseSchema):
    status: str | None = Field(default=None)


class EventTypesResponse(APIResponseSchema):
    status: int | str
    data: EventTypesResponseData


class SubscribeResponse(APIResponseSchema):
    status: str
    data: SubscribeResponseData


class UnsubscribeResponse(APIResponseSchema):
    status: str
    data: UnsubscribeResponseData


class ChangeActivationResponse(APIResponseSchema):
    status: str
    data: ChangeActivationResponseData


__all__ = [
    "ChangeActivationRequest",
    "ChangeActivationResponse",
    "ChangeActivationResponseData",
    "EventTypesResponse",
    "EventTypesResponseData",
    "SubscribeRequest",
    "SubscribeResponse",
    "SubscribeResponseData",
    "UnsubscribeRequest",
    "UnsubscribeResponse",
    "UnsubscribeResponseData",
]
