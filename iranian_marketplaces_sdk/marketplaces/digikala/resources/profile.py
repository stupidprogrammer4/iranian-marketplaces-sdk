"""Digikala profile: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import profile as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
)

GET_PATH = "/profile"
BUSINESS_PATH = "/profile/business"
UPDATE_BUSINESS_PATH = "/profile/business"
STORE_PATH = "/profile/store"
ADDRESSES_PATH = "/profile/address"
WAREHOUSES_PATH = "/profile/warehouse"
DOCUMENTS_PATH = "/profile/document"
TRAINING_PATH = "/profile/training"
PERFORMANCE_PATH = "/profile/performance"


class ProfileSync(SyncResource):
    def get(self) -> models.GetResponse:
        """GET /profile. Scopes => profile."""
        response = self._request("GET", GET_PATH)
        return parse_response(models.GetResponse, response)

    def business(self) -> models.BusinessResponse:
        """GET /profile/business. Scopes => profile."""
        response = self._request("GET", BUSINESS_PATH)
        return parse_response(models.BusinessResponse, response)

    def update_business(
        self, *, body: models.UpdateBusinessRequest
    ) -> models.UpdateBusinessResponse:
        """PATCH /profile/business. Scopes => profile."""
        response = self._request("PATCH", UPDATE_BUSINESS_PATH, body=body)
        return parse_response(models.UpdateBusinessResponse, response)

    def store(self) -> models.StoreResponse:
        """GET /profile/store. Scopes => profile."""
        response = self._request("GET", STORE_PATH)
        return parse_response(models.StoreResponse, response)

    def addresses(self) -> models.AddressesResponse:
        """GET /profile/address. Scopes => profile."""
        response = self._request("GET", ADDRESSES_PATH)
        return parse_response(models.AddressesResponse, response)

    def warehouses(self) -> models.WarehousesResponse:
        """GET /profile/warehouse. Scopes => profile."""
        response = self._request("GET", WAREHOUSES_PATH)
        return parse_response(models.WarehousesResponse, response)

    def documents(self) -> models.DocumentsResponse:
        """GET /profile/document. Scopes => profile."""
        response = self._request("GET", DOCUMENTS_PATH)
        return parse_response(models.DocumentsResponse, response)

    def training(self) -> models.TrainingResponse:
        """GET /profile/training. Scopes => profile."""
        response = self._request("GET", TRAINING_PATH)
        return parse_response(models.TrainingResponse, response)

    def performance(self) -> models.PerformanceResponse:
        """GET /profile/performance. Scopes => profile."""
        response = self._request("GET", PERFORMANCE_PATH)
        return parse_response(models.PerformanceResponse, response)


class ProfileAsync(AsyncResource):
    async def get(self) -> models.GetResponse:
        """GET /profile. Scopes => profile."""
        response = await self._request("GET", GET_PATH)
        return parse_response(models.GetResponse, response)

    async def business(self) -> models.BusinessResponse:
        """GET /profile/business. Scopes => profile."""
        response = await self._request("GET", BUSINESS_PATH)
        return parse_response(models.BusinessResponse, response)

    async def update_business(
        self, *, body: models.UpdateBusinessRequest
    ) -> models.UpdateBusinessResponse:
        """PATCH /profile/business. Scopes => profile."""
        response = await self._request("PATCH", UPDATE_BUSINESS_PATH, body=body)
        return parse_response(models.UpdateBusinessResponse, response)

    async def store(self) -> models.StoreResponse:
        """GET /profile/store. Scopes => profile."""
        response = await self._request("GET", STORE_PATH)
        return parse_response(models.StoreResponse, response)

    async def addresses(self) -> models.AddressesResponse:
        """GET /profile/address. Scopes => profile."""
        response = await self._request("GET", ADDRESSES_PATH)
        return parse_response(models.AddressesResponse, response)

    async def warehouses(self) -> models.WarehousesResponse:
        """GET /profile/warehouse. Scopes => profile."""
        response = await self._request("GET", WAREHOUSES_PATH)
        return parse_response(models.WarehousesResponse, response)

    async def documents(self) -> models.DocumentsResponse:
        """GET /profile/document. Scopes => profile."""
        response = await self._request("GET", DOCUMENTS_PATH)
        return parse_response(models.DocumentsResponse, response)

    async def training(self) -> models.TrainingResponse:
        """GET /profile/training. Scopes => profile."""
        response = await self._request("GET", TRAINING_PATH)
        return parse_response(models.TrainingResponse, response)

    async def performance(self) -> models.PerformanceResponse:
        """GET /profile/performance. Scopes => profile."""
        response = await self._request("GET", PERFORMANCE_PATH)
        return parse_response(models.PerformanceResponse, response)
