"""Digikala categories: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import categories as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

TREE_PATH = "/categories/tree"


class CategoriesSync(SyncResource):
    def tree(self, *, query: models.TreeQuery | None = None) -> models.TreeResponse:
        """GET /categories/tree. Scopes => product."""
        response = self._request("GET", TREE_PATH, query=query)
        return parse_response(models.TreeResponse, response)


class CategoriesAsync(AsyncResource):
    async def tree(self, *, query: models.TreeQuery | None = None) -> models.TreeResponse:
        """GET /categories/tree. Scopes => product."""
        response = await self._request("GET", TREE_PATH, query=query)
        return parse_response(models.TreeResponse, response)
