"""Digikala multi pricing: request and response models."""

from __future__ import annotations

from pydantic import Field

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
)


class EstimateQuery(QuerySchema):
    variant_id: int
    selling_price: int
    rrp_price: int


class EstimateResponseData(APIResponseSchema):
    cash_selling_price: int | None = Field(default=None)
    cash_rrp_price: int | None = Field(default=None)
    cash_discount: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    credit_rrp_price: int | None = Field(default=None)
    credit_discount: int | None = Field(default=None)
    credit_increase_percentage: int | None = Field(default=None)


class EstimateResponse(APIResponseSchema):
    status: int | str
    data: EstimateResponseData


__all__ = ["EstimateQuery", "EstimateResponse", "EstimateResponseData"]
