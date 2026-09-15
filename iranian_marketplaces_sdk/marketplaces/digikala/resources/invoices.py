"""Digikala invoices: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import invoices as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/invoices"
DETAILS_PATH = "/invoices/{invoice_id}/details"
ITEMS_PATH = "/invoices/{invoice_id}/items/{financial_notation_id}/{calculation_type}"
SUBMIT_VAT_PATH = "/invoices/vat"


class InvoicesSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /invoices. Scopes => invoice."""
        response = self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    def details(self, invoice_id: int) -> models.DetailsResponse:
        """GET /invoices/{invoice_id}/details. Scopes => invoice."""
        response = self._request("GET", DETAILS_PATH.format(invoice_id=path_value(invoice_id)))
        return parse_response(models.DetailsResponse, response)

    def items(
        self,
        invoice_id: int,
        financial_notation_id: int,
        calculation_type: str,
        *,
        query: models.ItemsQuery | None = None,
    ) -> models.ItemsResponse:
        """GET /invoices/{invoice_id}/items/{financial_notation_id}/{calculation_type}. Scopes
        => invoice."""
        response = self._request(
            "GET",
            ITEMS_PATH.format(
                invoice_id=path_value(invoice_id),
                financial_notation_id=path_value(financial_notation_id),
                calculation_type=path_value(calculation_type),
            ),
            query=query,
        )
        return parse_response(models.ItemsResponse, response)

    def submit_vat(self, *, body: models.SubmitVatRequest) -> RawResponse:
        """POST /invoices/vat. Scopes => invoice. Response schema is undocumented; returns
        original bytes and headers."""
        response = self._request("POST", SUBMIT_VAT_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class InvoicesAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /invoices. Scopes => invoice."""
        response = await self._request("GET", LIST_PATH, query=query)
        return parse_response(models.ListResponse, response)

    async def details(self, invoice_id: int) -> models.DetailsResponse:
        """GET /invoices/{invoice_id}/details. Scopes => invoice."""
        response = await self._request(
            "GET", DETAILS_PATH.format(invoice_id=path_value(invoice_id))
        )
        return parse_response(models.DetailsResponse, response)

    async def items(
        self,
        invoice_id: int,
        financial_notation_id: int,
        calculation_type: str,
        *,
        query: models.ItemsQuery | None = None,
    ) -> models.ItemsResponse:
        """GET /invoices/{invoice_id}/items/{financial_notation_id}/{calculation_type}. Scopes
        => invoice."""
        response = await self._request(
            "GET",
            ITEMS_PATH.format(
                invoice_id=path_value(invoice_id),
                financial_notation_id=path_value(financial_notation_id),
                calculation_type=path_value(calculation_type),
            ),
            query=query,
        )
        return parse_response(models.ItemsResponse, response)

    async def submit_vat(self, *, body: models.SubmitVatRequest) -> RawResponse:
        """POST /invoices/vat. Scopes => invoice. Response schema is undocumented; returns
        original bytes and headers."""
        response = await self._request("POST", SUBMIT_VAT_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
