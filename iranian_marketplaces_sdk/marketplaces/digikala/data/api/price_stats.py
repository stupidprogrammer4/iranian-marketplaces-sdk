"""Digikala price stats: request and response models."""

from __future__ import annotations

from pydantic import Field

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
)


class BoundaryQuery(QuerySchema):
    promotion_id: int | None = Field(default=None)


class BoundaryResponseDataDefaultPriceBoundary(APIResponseSchema):
    min_allowed_price: int | None = Field(default=None)
    max_allowed_price: int | None = Field(default=None)


class BoundaryResponseDataPromotionPriceBoundary(APIResponseSchema):
    min_allowed_price: int | None = Field(default=None)
    max_allowed_price: int | None = Field(default=None)


class BoundaryResponseData(APIResponseSchema):
    default_price_boundary: BoundaryResponseDataDefaultPriceBoundary | None = Field(default=None)
    promotion_price_boundary: BoundaryResponseDataPromotionPriceBoundary | None = Field(
        default=None
    )


class BoundaryResponse(APIResponseSchema):
    status: int | str
    data: BoundaryResponseData


__all__ = [
    "BoundaryQuery",
    "BoundaryResponse",
    "BoundaryResponseData",
    "BoundaryResponseDataDefaultPriceBoundary",
    "BoundaryResponseDataPromotionPriceBoundary",
]
