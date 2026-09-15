"""Digikala packages: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import packages as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/packages"
CREATE_PATH = "/packages"
WAREHOUSES_PATH = "/packages/warehouses"
WAREHOUSE_CAPACITIES_PATH = "/packages/warehouses/{warehouse_id}/capacities"
CALCULATE_WAREHOUSE_CAPACITIES_PATH = "/packages/warehouses/{warehouse_id}/capacities"
GET_PATH = "/packages/{package_id}"
DELETE_PATH = "/packages/{package_id}"
EXPORT_PATH = "/packages/{package_id}/excel/export"
CONSIGNMENT_VARIANTS_PATH = "/packages/consignment/variants"
FULFILMENT_VARIANTS_PATH = "/packages/order-fulfilment/variants"
FILTER_FULFILMENT_VARIANTS_PATH = "/packages/order-fulfilment/variants"
CONSIGNMENT_PATH = "/variants/packages/consignment"


class PackagesSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /packages. Scopes => package."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def create(self, *, body: models.CreateRequest) -> RawResponse:
        """POST /packages. Scopes => package. Response schema is undocumented; returns original
        bytes and headers."""
        response = self._request("POST", CREATE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def warehouses(
        self, *, query: models.WarehousesQuery | None = None
    ) -> models.WarehousesResponse:
        """GET /packages/warehouses. Scopes => package."""
        response = self._request("GET", WAREHOUSES_PATH, query=query)
        return parse_response(models.WarehousesResponse, response)

    def warehouse_capacities(
        self, warehouse_id: int, *, query: models.WarehouseCapacitiesQuery
    ) -> models.WarehouseCapacitiesResponse:
        """GET /packages/warehouses/{warehouse_id}/capacities. Scopes => package."""
        response = self._request(
            "GET",
            WAREHOUSE_CAPACITIES_PATH.format(warehouse_id=path_value(warehouse_id)),
            query=query,
            separators={"variants": ",", "counts": ","},
        )
        return parse_response(models.WarehouseCapacitiesResponse, response)

    def calculate_warehouse_capacities(
        self, warehouse_id: int, *, body: models.CalculateWarehouseCapacitiesRequest | None = None
    ) -> models.CalculateWarehouseCapacitiesResponse:
        """POST /packages/warehouses/{warehouse_id}/capacities. Scopes => package."""
        response = self._request(
            "POST",
            CALCULATE_WAREHOUSE_CAPACITIES_PATH.format(warehouse_id=path_value(warehouse_id)),
            body=body,
        )
        return parse_response(models.CalculateWarehouseCapacitiesResponse, response)

    def get(self, package_id: int, *, query: models.GetQuery | None = None) -> models.GetResponse:
        """GET /packages/{package_id}. Scopes => package."""
        response = self._request(
            "GET",
            GET_PATH.format(package_id=path_value(package_id)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.GetResponse, response)

    def delete(self, package_id: int) -> RawResponse:
        """DELETE /packages/{package_id}. Scopes => package. Response schema is undocumented;
        returns original bytes and headers."""
        response = self._request("DELETE", DELETE_PATH.format(package_id=path_value(package_id)))
        return RawResponse(response.status_code, response.headers, response.content)

    def export(
        self, package_id: int, *, query: models.ExportQuery | None = None
    ) -> models.ExportResponse:
        """GET /packages/{package_id}/excel/export. Scopes => package."""
        response = self._request(
            "GET",
            EXPORT_PATH.format(package_id=path_value(package_id)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.ExportResponse, response)

    def consignment_variants(
        self, *, query: models.ConsignmentVariantsQuery | None = None
    ) -> models.ConsignmentVariantsResponse:
        """GET /packages/consignment/variants. Scopes => package."""
        response = self._request(
            "GET", CONSIGNMENT_VARIANTS_PATH, query=query, separators={"variant_ids": ","}
        )
        return parse_response(models.ConsignmentVariantsResponse, response)

    def fulfilment_variants(
        self, *, query: models.FulfilmentVariantsQuery | None = None
    ) -> models.FulfilmentVariantsResponse:
        """GET /packages/order-fulfilment/variants. Scopes => package."""
        response = self._request(
            "GET", FULFILMENT_VARIANTS_PATH, query=query, separators={"[order_item_ids]": ","}
        )
        return parse_response(models.FulfilmentVariantsResponse, response)

    def filter_fulfilment_variants(
        self, *, body: models.FilterFulfilmentVariantsRequest | None = None
    ) -> models.FilterFulfilmentVariantsResponse:
        """POST /packages/order-fulfilment/variants. Scopes => package."""
        response = self._request("POST", FILTER_FULFILMENT_VARIANTS_PATH, body=body)
        return parse_response(models.FilterFulfilmentVariantsResponse, response)

    def consignment(
        self, *, query: models.ConsignmentQuery | None = None
    ) -> models.ConsignmentResponse:
        """GET /variants/packages/consignment. Scopes => package."""
        response = self._request(
            "GET", CONSIGNMENT_PATH, query=query, separators={"search[selected_variant_ids]": ","}
        )
        return parse_response(models.ConsignmentResponse, response)


class PackagesAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /packages. Scopes => package."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def create(self, *, body: models.CreateRequest) -> RawResponse:
        """POST /packages. Scopes => package. Response schema is undocumented; returns original
        bytes and headers."""
        response = await self._request("POST", CREATE_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def warehouses(
        self, *, query: models.WarehousesQuery | None = None
    ) -> models.WarehousesResponse:
        """GET /packages/warehouses. Scopes => package."""
        response = await self._request("GET", WAREHOUSES_PATH, query=query)
        return parse_response(models.WarehousesResponse, response)

    async def warehouse_capacities(
        self, warehouse_id: int, *, query: models.WarehouseCapacitiesQuery
    ) -> models.WarehouseCapacitiesResponse:
        """GET /packages/warehouses/{warehouse_id}/capacities. Scopes => package."""
        response = await self._request(
            "GET",
            WAREHOUSE_CAPACITIES_PATH.format(warehouse_id=path_value(warehouse_id)),
            query=query,
            separators={"variants": ",", "counts": ","},
        )
        return parse_response(models.WarehouseCapacitiesResponse, response)

    async def calculate_warehouse_capacities(
        self, warehouse_id: int, *, body: models.CalculateWarehouseCapacitiesRequest | None = None
    ) -> models.CalculateWarehouseCapacitiesResponse:
        """POST /packages/warehouses/{warehouse_id}/capacities. Scopes => package."""
        response = await self._request(
            "POST",
            CALCULATE_WAREHOUSE_CAPACITIES_PATH.format(warehouse_id=path_value(warehouse_id)),
            body=body,
        )
        return parse_response(models.CalculateWarehouseCapacitiesResponse, response)

    async def get(
        self, package_id: int, *, query: models.GetQuery | None = None
    ) -> models.GetResponse:
        """GET /packages/{package_id}. Scopes => package."""
        response = await self._request(
            "GET",
            GET_PATH.format(package_id=path_value(package_id)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.GetResponse, response)

    async def delete(self, package_id: int) -> RawResponse:
        """DELETE /packages/{package_id}. Scopes => package. Response schema is undocumented;
        returns original bytes and headers."""
        response = await self._request(
            "DELETE", DELETE_PATH.format(package_id=path_value(package_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def export(
        self, package_id: int, *, query: models.ExportQuery | None = None
    ) -> models.ExportResponse:
        """GET /packages/{package_id}/excel/export. Scopes => package."""
        response = await self._request(
            "GET",
            EXPORT_PATH.format(package_id=path_value(package_id)),
            query=query,
            separators={"search[status]": ","},
        )
        return parse_response(models.ExportResponse, response)

    async def consignment_variants(
        self, *, query: models.ConsignmentVariantsQuery | None = None
    ) -> models.ConsignmentVariantsResponse:
        """GET /packages/consignment/variants. Scopes => package."""
        response = await self._request(
            "GET", CONSIGNMENT_VARIANTS_PATH, query=query, separators={"variant_ids": ","}
        )
        return parse_response(models.ConsignmentVariantsResponse, response)

    async def fulfilment_variants(
        self, *, query: models.FulfilmentVariantsQuery | None = None
    ) -> models.FulfilmentVariantsResponse:
        """GET /packages/order-fulfilment/variants. Scopes => package."""
        response = await self._request(
            "GET", FULFILMENT_VARIANTS_PATH, query=query, separators={"[order_item_ids]": ","}
        )
        return parse_response(models.FulfilmentVariantsResponse, response)

    async def filter_fulfilment_variants(
        self, *, body: models.FilterFulfilmentVariantsRequest | None = None
    ) -> models.FilterFulfilmentVariantsResponse:
        """POST /packages/order-fulfilment/variants. Scopes => package."""
        response = await self._request("POST", FILTER_FULFILMENT_VARIANTS_PATH, body=body)
        return parse_response(models.FilterFulfilmentVariantsResponse, response)

    async def consignment(
        self, *, query: models.ConsignmentQuery | None = None
    ) -> models.ConsignmentResponse:
        """GET /variants/packages/consignment. Scopes => package."""
        response = await self._request(
            "GET", CONSIGNMENT_PATH, query=query, separators={"search[selected_variant_ids]": ","}
        )
        return parse_response(models.ConsignmentResponse, response)
