"""Digikala seller shipping: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import seller_shipping as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

CREATE_PATH = "/shipments/seller/new-settings"
LIST_PATH = "/shipments/seller/new-settings"
UPDATE_PATH = "/shipments/seller/new-settings/{id}"
GET_PATH = "/shipments/seller/new-settings/{id}"
STATES_PATH = "/shipments/seller/new-settings/state"
TIME_SCOPES_PATH = "/shipments/seller/new-settings/time-scope"
DEACTIVATE_CITIES_PATH = "/shipments/seller/new-settings/deactivate-cities"


class SellerShippingSync(SyncResource):
    def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /shipments/seller/new-settings. Scopes => sbs_setting."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def list(self, *, query: models.ListQuery) -> models.ListResponse:
        """GET /shipments/seller/new-settings. Scopes => sbs_setting."""
        response = self._request("GET", LIST_PATH, query=query, separators={"search[ids]": ","})
        return parse_response(models.ListResponse, response)

    def update(self, id: int, *, body: models.UpdateRequest | None = None) -> models.UpdateResponse:
        """PATCH /shipments/seller/new-settings/{id}. Scopes => sbs_setting."""
        response = self._request("PATCH", UPDATE_PATH.format(id=path_value(id)), body=body)
        return parse_response(models.UpdateResponse, response)

    def get(self, id: int) -> models.GetResponse:
        """GET /shipments/seller/new-settings/{id}. Scopes => sbs_setting."""
        response = self._request("GET", GET_PATH.format(id=path_value(id)))
        return parse_response(models.GetResponse, response)

    def states(self, *, query: models.StatesQuery) -> models.StatesResponse:
        """GET /shipments/seller/new-settings/state. Scopes => sbs_setting."""
        response = self._request("GET", STATES_PATH, query=query)
        return parse_response(models.StatesResponse, response)

    def time_scopes(
        self, *, query: models.TimeScopesQuery | None = None
    ) -> models.TimeScopesResponse:
        """GET /shipments/seller/new-settings/time-scope. Scopes => sbs_setting."""
        response = self._request("GET", TIME_SCOPES_PATH, query=query)
        return parse_response(models.TimeScopesResponse, response)

    def deactivate_cities(self, *, body: models.DeactivateCitiesRequest) -> RawResponse:
        """POST /shipments/seller/new-settings/deactivate-cities. Scopes => sbs_setting.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request("POST", DEACTIVATE_CITIES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class SellerShippingAsync(AsyncResource):
    async def create(self, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /shipments/seller/new-settings. Scopes => sbs_setting."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def list(self, *, query: models.ListQuery) -> models.ListResponse:
        """GET /shipments/seller/new-settings. Scopes => sbs_setting."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[ids]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def update(
        self, id: int, *, body: models.UpdateRequest | None = None
    ) -> models.UpdateResponse:
        """PATCH /shipments/seller/new-settings/{id}. Scopes => sbs_setting."""
        response = await self._request("PATCH", UPDATE_PATH.format(id=path_value(id)), body=body)
        return parse_response(models.UpdateResponse, response)

    async def get(self, id: int) -> models.GetResponse:
        """GET /shipments/seller/new-settings/{id}. Scopes => sbs_setting."""
        response = await self._request("GET", GET_PATH.format(id=path_value(id)))
        return parse_response(models.GetResponse, response)

    async def states(self, *, query: models.StatesQuery) -> models.StatesResponse:
        """GET /shipments/seller/new-settings/state. Scopes => sbs_setting."""
        response = await self._request("GET", STATES_PATH, query=query)
        return parse_response(models.StatesResponse, response)

    async def time_scopes(
        self, *, query: models.TimeScopesQuery | None = None
    ) -> models.TimeScopesResponse:
        """GET /shipments/seller/new-settings/time-scope. Scopes => sbs_setting."""
        response = await self._request("GET", TIME_SCOPES_PATH, query=query)
        return parse_response(models.TimeScopesResponse, response)

    async def deactivate_cities(self, *, body: models.DeactivateCitiesRequest) -> RawResponse:
        """POST /shipments/seller/new-settings/deactivate-cities. Scopes => sbs_setting.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request("POST", DEACTIVATE_CITIES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
