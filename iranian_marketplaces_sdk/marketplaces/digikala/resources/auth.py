"""Digikala auth: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import auth as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

LIST_SCOPES_PATH = "/auth/scopes"
GET_CLIENT_SCOPES_PATH = "/auth/scopes/{client_code}"
REVOKE_PATH = "/auth/revoke"


class AuthSync(SyncResource):
    def list_scopes(self) -> models.ListScopesResponse:
        """GET /auth/scopes."""
        response = self._request("GET", LIST_SCOPES_PATH)
        return parse_response(models.ListScopesResponse, response)

    def get_client_scopes(self, client_code: str) -> models.GetClientScopesResponse:
        """GET /auth/scopes/{client_code}."""
        response = self._request(
            "GET", GET_CLIENT_SCOPES_PATH.format(client_code=path_value(client_code))
        )
        return parse_response(models.GetClientScopesResponse, response)

    def revoke(self) -> models.RevokeResponse:
        """POST /auth/revoke. Scopes => self_settings."""
        response = self._request("POST", REVOKE_PATH)
        return parse_response(models.RevokeResponse, response)


class AuthAsync(AsyncResource):
    async def list_scopes(self) -> models.ListScopesResponse:
        """GET /auth/scopes."""
        response = await self._request("GET", LIST_SCOPES_PATH)
        return parse_response(models.ListScopesResponse, response)

    async def get_client_scopes(self, client_code: str) -> models.GetClientScopesResponse:
        """GET /auth/scopes/{client_code}."""
        response = await self._request(
            "GET", GET_CLIENT_SCOPES_PATH.format(client_code=path_value(client_code))
        )
        return parse_response(models.GetClientScopesResponse, response)

    async def revoke(self) -> models.RevokeResponse:
        """POST /auth/revoke. Scopes => self_settings."""
        response = await self._request("POST", REVOKE_PATH)
        return parse_response(models.RevokeResponse, response)
