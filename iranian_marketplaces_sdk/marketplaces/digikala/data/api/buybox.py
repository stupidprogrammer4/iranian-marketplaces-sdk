"""Digikala buybox: request and response models."""

from __future__ import annotations

from pydantic import Field

from iranian_marketplaces_sdk.common.data import QuerySchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
)


class WinningPriceQuery(QuerySchema):
    product_variant_id: int


class WinningPriceResponseData(APIResponseSchema):
    suggested_price: int | None = Field(default=None)


class RankedWinningPriceQuery(QuerySchema):
    product_variant_id: int
    target_rank: int


class RankedWinningPriceResponse(APIResponseSchema):
    status: int | str
    data: WinningPriceResponseData


class WinningPriceResponse(APIResponseSchema):
    status: int | str
    data: WinningPriceResponseData


__all__ = [
    "RankedWinningPriceQuery",
    "RankedWinningPriceResponse",
    "WinningPriceQuery",
    "WinningPriceResponse",
    "WinningPriceResponseData",
]
