"""Digikala themes: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import themes as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_VALUES_PATH = "/variants/creation/themes/{theme_id}/theme-values"


class ThemesSync(SyncResource):
    def list_values(
        self, theme_id: int, *, query: models.ListValuesQuery | None = None
    ) -> models.ListValuesResponse:
        """GET /variants/creation/themes/{theme_id}/theme-values. Scopes => variant."""
        response = self._request(
            "GET", LIST_VALUES_PATH.format(theme_id=path_value(theme_id)), query=query
        )
        return parse_response(models.ListValuesResponse, response)


class ThemesAsync(AsyncResource):
    async def list_values(
        self, theme_id: int, *, query: models.ListValuesQuery | None = None
    ) -> models.ListValuesResponse:
        """GET /variants/creation/themes/{theme_id}/theme-values. Scopes => variant."""
        response = await self._request(
            "GET", LIST_VALUES_PATH.format(theme_id=path_value(theme_id)), query=query
        )
        return parse_response(models.ListValuesResponse, response)
