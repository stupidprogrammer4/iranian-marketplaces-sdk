"""Digikala variant creation: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import variant_creation as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    SyncResource,
    parse_response,
    path_value,
)

GET_PATH = "/variants/creation/{product_id}"
CREATE_PATH = "/variants/creation/{product_id}"
UPDATE_PATH = "/variants/creation/{product_id}/{variant_id}"
LIST_SIZE_TYPES_PATH = "/variants/creation/size/types"
REQUEST_SIZE_PATH = "/variants/creation/size/request"
REQUEST_COLOR_PATH = "/variants/creation/color/request"
REQUEST_WARRANTY_PATH = "/variants/creation/warranty/request"


class VariantCreationSync(SyncResource):
    def get(self, product_id: int) -> models.GetResponse:
        """GET /variants/creation/{product_id}. Scopes => variant."""
        response = self._request("GET", GET_PATH.format(product_id=path_value(product_id)))
        return parse_response(models.GetResponse, response)

    def create(self, product_id: int, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /variants/creation/{product_id}. Scopes => variant."""
        response = self._request(
            "POST", CREATE_PATH.format(product_id=path_value(product_id)), body=body
        )
        return parse_response(models.CreateResponse, response)

    def update(
        self,
        product_id: int,
        variant_id: int,
        *,
        body: models.UpdateRequest,
        query: models.UpdateQuery | None = None,
    ) -> models.UpdateResponse:
        """PUT /variants/creation/{product_id}/{variant_id}. Scopes => variant."""
        response = self._request(
            "PUT",
            UPDATE_PATH.format(
                product_id=path_value(product_id), variant_id=path_value(variant_id)
            ),
            query=query,
            body=body,
        )
        return parse_response(models.UpdateResponse, response)

    def list_size_types(self) -> models.ListSizeTypesResponse:
        """GET /variants/creation/size/types. Scopes => variant."""
        response = self._request("GET", LIST_SIZE_TYPES_PATH)
        return parse_response(models.ListSizeTypesResponse, response)

    def request_size(
        self, *, body: models.RequestSizeRequest | None = None
    ) -> models.RequestSizeResponse:
        """POST /variants/creation/size/request. Scopes => variant."""
        response = self._request("POST", REQUEST_SIZE_PATH, body=body)
        return parse_response(models.RequestSizeResponse, response)

    def request_color(
        self, *, body: models.RequestColorRequest | None = None
    ) -> models.RequestColorResponse:
        """POST /variants/creation/color/request. Scopes => variant."""
        response = self._request("POST", REQUEST_COLOR_PATH, body=body)
        return parse_response(models.RequestColorResponse, response)

    def request_warranty(
        self, *, body: models.RequestWarrantyRequest
    ) -> models.RequestWarrantyResponse:
        """POST /variants/creation/warranty/request. Scopes => variant."""
        response = self._request("POST", REQUEST_WARRANTY_PATH, body=body)
        return parse_response(models.RequestWarrantyResponse, response)


class VariantCreationAsync(AsyncResource):
    async def get(self, product_id: int) -> models.GetResponse:
        """GET /variants/creation/{product_id}. Scopes => variant."""
        response = await self._request("GET", GET_PATH.format(product_id=path_value(product_id)))
        return parse_response(models.GetResponse, response)

    async def create(self, product_id: int, *, body: models.CreateRequest) -> models.CreateResponse:
        """POST /variants/creation/{product_id}. Scopes => variant."""
        response = await self._request(
            "POST", CREATE_PATH.format(product_id=path_value(product_id)), body=body
        )
        return parse_response(models.CreateResponse, response)

    async def update(
        self,
        product_id: int,
        variant_id: int,
        *,
        body: models.UpdateRequest,
        query: models.UpdateQuery | None = None,
    ) -> models.UpdateResponse:
        """PUT /variants/creation/{product_id}/{variant_id}. Scopes => variant."""
        response = await self._request(
            "PUT",
            UPDATE_PATH.format(
                product_id=path_value(product_id), variant_id=path_value(variant_id)
            ),
            query=query,
            body=body,
        )
        return parse_response(models.UpdateResponse, response)

    async def list_size_types(self) -> models.ListSizeTypesResponse:
        """GET /variants/creation/size/types. Scopes => variant."""
        response = await self._request("GET", LIST_SIZE_TYPES_PATH)
        return parse_response(models.ListSizeTypesResponse, response)

    async def request_size(
        self, *, body: models.RequestSizeRequest | None = None
    ) -> models.RequestSizeResponse:
        """POST /variants/creation/size/request. Scopes => variant."""
        response = await self._request("POST", REQUEST_SIZE_PATH, body=body)
        return parse_response(models.RequestSizeResponse, response)

    async def request_color(
        self, *, body: models.RequestColorRequest | None = None
    ) -> models.RequestColorResponse:
        """POST /variants/creation/color/request. Scopes => variant."""
        response = await self._request("POST", REQUEST_COLOR_PATH, body=body)
        return parse_response(models.RequestColorResponse, response)

    async def request_warranty(
        self, *, body: models.RequestWarrantyRequest
    ) -> models.RequestWarrantyResponse:
        """POST /variants/creation/warranty/request. Scopes => variant."""
        response = await self._request("POST", REQUEST_WARRANTY_PATH, body=body)
        return parse_response(models.RequestWarrantyResponse, response)
