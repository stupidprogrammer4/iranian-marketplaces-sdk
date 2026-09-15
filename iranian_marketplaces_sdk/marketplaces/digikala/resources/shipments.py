"""Digikala shipments: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import shipments as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/shipments/dk"
CREATE_PATH = "/shipments/dk"
PACKAGES_PATH = "/shipments/dk/packages"
GET_PATH = "/shipments/dk/{shipment_id}"
DELETE_PATH = "/shipments/dk/{shipment_id}"


class ShipmentsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /shipments/dk. Scopes => shipment."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def create(self, *, body: models.CreateRequest | None = None) -> models.CreateResponse:
        """POST /shipments/dk. Scopes => shipment."""
        response = self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    def packages(self, *, query: models.PackagesQuery | None = None) -> models.PackagesResponse:
        """GET /shipments/dk/packages. Scopes => shipment."""
        response = self._request("GET", PACKAGES_PATH, query=query, separators={"package_ids": ","})
        return parse_response(models.PackagesResponse, response)

    def get(self, shipment_id: int) -> models.GetResponse:
        """GET /shipments/dk/{shipment_id}. Scopes => shipment."""
        response = self._request("GET", GET_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.GetResponse, response)

    def delete(self, shipment_id: int) -> RawResponse:
        """DELETE /shipments/dk/{shipment_id}. Scopes => shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("DELETE", DELETE_PATH.format(shipment_id=path_value(shipment_id)))
        return RawResponse(response.status_code, response.headers, response.content)


class ShipmentsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /shipments/dk. Scopes => shipment."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def create(self, *, body: models.CreateRequest | None = None) -> models.CreateResponse:
        """POST /shipments/dk. Scopes => shipment."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return parse_response(models.CreateResponse, response)

    async def packages(
        self, *, query: models.PackagesQuery | None = None
    ) -> models.PackagesResponse:
        """GET /shipments/dk/packages. Scopes => shipment."""
        response = await self._request(
            "GET", PACKAGES_PATH, query=query, separators={"package_ids": ","}
        )
        return parse_response(models.PackagesResponse, response)

    async def get(self, shipment_id: int) -> models.GetResponse:
        """GET /shipments/dk/{shipment_id}. Scopes => shipment."""
        response = await self._request("GET", GET_PATH.format(shipment_id=path_value(shipment_id)))
        return parse_response(models.GetResponse, response)

    async def delete(self, shipment_id: int) -> RawResponse:
        """DELETE /shipments/dk/{shipment_id}. Scopes => shipment. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request(
            "DELETE", DELETE_PATH.format(shipment_id=path_value(shipment_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)
