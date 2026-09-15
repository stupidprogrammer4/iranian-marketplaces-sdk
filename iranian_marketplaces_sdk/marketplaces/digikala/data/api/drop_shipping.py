"""Digikala drop shipping: request and response models."""

from __future__ import annotations

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema


class SendOtpRequest(RequestSchema):
    phone_number: str


class TotalWeightQuery(QuerySchema):
    variant_ids: list[int]
    quantities: list[int]


class RegisterUserRequest(RequestSchema):
    otp: int


__all__ = ["RegisterUserRequest", "SendOtpRequest", "TotalWeightQuery"]
