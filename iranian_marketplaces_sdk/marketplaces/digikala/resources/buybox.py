"""Digikala buybox: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import buybox as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

WINNING_PRICE_PATH = "/pricing/buybox/price-suggestion/winning-price"
RANKED_WINNING_PRICE_PATH = "/pricing/buybox/price-suggestion/nth-rank-winning-price"


class BuyboxSync(SyncResource):
    def winning_price(self, *, query: models.WinningPriceQuery) -> models.WinningPriceResponse:
        """GET /pricing/buybox/price-suggestion/winning-price. Scopes => variant."""
        response = self._request("GET", WINNING_PRICE_PATH, query=query)
        return parse_response(models.WinningPriceResponse, response)

    def ranked_winning_price(
        self, *, query: models.RankedWinningPriceQuery
    ) -> models.RankedWinningPriceResponse:
        """GET /pricing/buybox/price-suggestion/nth-rank-winning-price. Scopes => variant."""
        response = self._request("GET", RANKED_WINNING_PRICE_PATH, query=query)
        return parse_response(models.RankedWinningPriceResponse, response)


class BuyboxAsync(AsyncResource):
    async def winning_price(
        self, *, query: models.WinningPriceQuery
    ) -> models.WinningPriceResponse:
        """GET /pricing/buybox/price-suggestion/winning-price. Scopes => variant."""
        response = await self._request("GET", WINNING_PRICE_PATH, query=query)
        return parse_response(models.WinningPriceResponse, response)

    async def ranked_winning_price(
        self, *, query: models.RankedWinningPriceQuery
    ) -> models.RankedWinningPriceResponse:
        """GET /pricing/buybox/price-suggestion/nth-rank-winning-price. Scopes => variant."""
        response = await self._request("GET", RANKED_WINNING_PRICE_PATH, query=query)
        return parse_response(models.RankedWinningPriceResponse, response)
