"""Digikala finance: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import finance as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

OVERVIEW_PATH = "/finance/overview/v2"
TRANSACTIONS_PATH = "/finance/transactions"
TRANSACTION_ROWS_PATH = "/finance/transactions/rows"
TRANSACTION_SUMMARY_PATH = "/finance/transactions/summary"
GET_TRANSACTION_PATH = "/finance/transactions/{transaction_id}"
PAYOUTS_PATH = "/finance/payouts"
GET_PAYOUT_PATH = "/finance/payouts/{payout_id}"
SELLER_INVOICES_PATH = "/finance/seller-invoices"
EXPORT_TRANSACTIONS_PATH = "/finance/transactions/export/excel"


class FinanceSync(SyncResource):
    def overview(self, *, query: models.OverviewQuery) -> models.OverviewResponse:
        """GET /finance/overview/v2. Scopes => invoice."""
        response = self._request("GET", OVERVIEW_PATH, query=query)
        return parse_response(models.OverviewResponse, response)

    def transactions(
        self, *, query: models.TransactionsQuery | None = None
    ) -> models.TransactionsResponse:
        """GET /finance/transactions. Scopes => invoice."""
        response = self._request(
            "GET",
            TRANSACTIONS_PATH,
            query=query,
            separators={"search[status]": ",", "search[aggregation_type]": ","},
        )
        return parse_response(models.TransactionsResponse, response)

    def transaction_rows(
        self, *, query: models.TransactionRowsQuery | None = None
    ) -> models.TransactionRowsResponse:
        """GET /finance/transactions/rows. Scopes => invoice."""
        response = self._request(
            "GET",
            TRANSACTION_ROWS_PATH,
            query=query,
            separators={"search[status]": ",", "search[notations]": ","},
        )
        return parse_response(models.TransactionRowsResponse, response)

    def transaction_summary(self) -> models.TransactionSummaryResponse:
        """GET /finance/transactions/summary. Scopes => invoice."""
        response = self._request("GET", TRANSACTION_SUMMARY_PATH)
        return parse_response(models.TransactionSummaryResponse, response)

    def get_transaction(self, transaction_id: int) -> models.GetTransactionResponse:
        """GET /finance/transactions/{transaction_id}. Scopes => invoice."""
        response = self._request(
            "GET", GET_TRANSACTION_PATH.format(transaction_id=path_value(transaction_id))
        )
        return parse_response(models.GetTransactionResponse, response)

    def payouts(self, *, query: models.PayoutsQuery | None = None) -> models.PayoutsResponse:
        """GET /finance/payouts. Scopes => invoice."""
        response = self._request(
            "GET", PAYOUTS_PATH, query=query, separators={"search[status]": ","}
        )
        return parse_response(models.PayoutsResponse, response)

    def get_payout(self, payout_id: int) -> models.GetPayoutResponse:
        """GET /finance/payouts/{payout_id}. Scopes => invoice."""
        response = self._request("GET", GET_PAYOUT_PATH.format(payout_id=path_value(payout_id)))
        return parse_response(models.GetPayoutResponse, response)

    def seller_invoices(
        self, *, query: models.SellerInvoicesQuery | None = None
    ) -> models.SellerInvoicesResponse:
        """GET /finance/seller-invoices. Scopes => invoice."""
        response = self._request("GET", SELLER_INVOICES_PATH, query=query)
        return parse_response(models.SellerInvoicesResponse, response)

    def export_transactions(
        self,
        *,
        body: models.ExportTransactionsRequest | None = None,
        query: models.ExportTransactionsQuery | None = None,
    ) -> RawResponse:
        """POST /finance/transactions/export/excel. Scopes => invoice. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", EXPORT_TRANSACTIONS_PATH, query=query, body=body)
        return RawResponse(response.status_code, response.headers, response.content)


class FinanceAsync(AsyncResource):
    async def overview(self, *, query: models.OverviewQuery) -> models.OverviewResponse:
        """GET /finance/overview/v2. Scopes => invoice."""
        response = await self._request("GET", OVERVIEW_PATH, query=query)
        return parse_response(models.OverviewResponse, response)

    async def transactions(
        self, *, query: models.TransactionsQuery | None = None
    ) -> models.TransactionsResponse:
        """GET /finance/transactions. Scopes => invoice."""
        response = await self._request(
            "GET",
            TRANSACTIONS_PATH,
            query=query,
            separators={"search[status]": ",", "search[aggregation_type]": ","},
        )
        return parse_response(models.TransactionsResponse, response)

    async def transaction_rows(
        self, *, query: models.TransactionRowsQuery | None = None
    ) -> models.TransactionRowsResponse:
        """GET /finance/transactions/rows. Scopes => invoice."""
        response = await self._request(
            "GET",
            TRANSACTION_ROWS_PATH,
            query=query,
            separators={"search[status]": ",", "search[notations]": ","},
        )
        return parse_response(models.TransactionRowsResponse, response)

    async def transaction_summary(self) -> models.TransactionSummaryResponse:
        """GET /finance/transactions/summary. Scopes => invoice."""
        response = await self._request("GET", TRANSACTION_SUMMARY_PATH)
        return parse_response(models.TransactionSummaryResponse, response)

    async def get_transaction(self, transaction_id: int) -> models.GetTransactionResponse:
        """GET /finance/transactions/{transaction_id}. Scopes => invoice."""
        response = await self._request(
            "GET", GET_TRANSACTION_PATH.format(transaction_id=path_value(transaction_id))
        )
        return parse_response(models.GetTransactionResponse, response)

    async def payouts(self, *, query: models.PayoutsQuery | None = None) -> models.PayoutsResponse:
        """GET /finance/payouts. Scopes => invoice."""
        response = await self._request(
            "GET", PAYOUTS_PATH, query=query, separators={"search[status]": ","}
        )
        return parse_response(models.PayoutsResponse, response)

    async def get_payout(self, payout_id: int) -> models.GetPayoutResponse:
        """GET /finance/payouts/{payout_id}. Scopes => invoice."""
        response = await self._request(
            "GET", GET_PAYOUT_PATH.format(payout_id=path_value(payout_id))
        )
        return parse_response(models.GetPayoutResponse, response)

    async def seller_invoices(
        self, *, query: models.SellerInvoicesQuery | None = None
    ) -> models.SellerInvoicesResponse:
        """GET /finance/seller-invoices. Scopes => invoice."""
        response = await self._request("GET", SELLER_INVOICES_PATH, query=query)
        return parse_response(models.SellerInvoicesResponse, response)

    async def export_transactions(
        self,
        *,
        body: models.ExportTransactionsRequest | None = None,
        query: models.ExportTransactionsQuery | None = None,
    ) -> RawResponse:
        """POST /finance/transactions/export/excel. Scopes => invoice. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", EXPORT_TRANSACTIONS_PATH, query=query, body=body)
        return RawResponse(response.status_code, response.headers, response.content)
