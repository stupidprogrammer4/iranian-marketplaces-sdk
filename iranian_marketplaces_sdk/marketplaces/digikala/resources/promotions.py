"""Digikala promotions: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import promotions as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    parse_response,
    path_value,
)

LIST_PATH = "/pricing/promotions"
CONFIGS_PATH = "/pricing/promotions/configs"
RECOMMENDED_PATH = "/pricing/promotions/recommended"
ELIGIBLE_PATH = "/pricing/promotions/eligible"
MINIMUM_DISCOUNTS_PATH = "/pricing/promotions/eligible/min-discounts"
UNJOINED_PATH = "/pricing/promotions/unjoined"
CURRENT_FOR_VARIANT_PATH = "/pricing/promotions/variant-current-promotions/{product_variant_id}"
VARIANTS_PATH = "/pricing/promotions/variants"
GET_VARIANT_PATH = "/pricing/promotions/variants/{variant_id}"
REJECTION_REASON_PATH = "/pricing/promotions/variants/rejection-reason/{promotion_variant_id}"
GET_PATH = "/pricing/promotions/{promotion_id}"
LIST_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants"
ADD_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants"
UPDATE_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants"
DELETE_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants"
REJECTED_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants/rejected"
ADD_VARIANTS_BATCH_PATH = "/pricing/promotions/{promotion_id}/variants/batch"
UPDATE_VARIANTS_BATCH_PATH = "/pricing/promotions/{promotion_id}/variants/batch"
ELIGIBLE_VARIANTS_PATH = "/pricing/promotions/{promotion_id}/variants/eligible"
ELIGIBLE_VARIANTS_V2_PATH = "/pricing/promotions/{promotion_id}/variants/eligible_v2"
VARIANTS_TO_JOIN_PATH = "/pricing/promotions/{promotion_id}/variants/to-join"
COMMISSION_DISCOUNT_PATH = (
    "/pricing/promotions/{promotion_id}/variants/{variant_id}/commission-discount"
)
SAMPLE_EXCEL_PATH = "/pricing/promotions/{promotion_id}/variants/excel/sample"
IMPORT_EXCEL_PATH = "/pricing/promotions/{promotion_id}/variants/excel"


class PromotionsSync(SyncResource):
    def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/promotions. Scopes => promotion."""
        response = self._request(
            "GET", LIST_PATH, query=query, separators={"search[nature]": ",", "search[status]": ","}
        )
        return parse_response(models.ListResponse, response)

    def configs(self) -> models.ConfigsResponse:
        """GET /pricing/promotions/configs. Scopes => promotion."""
        response = self._request("GET", CONFIGS_PATH)
        return parse_response(models.ConfigsResponse, response)

    def recommended(
        self, *, query: models.RecommendedQuery | None = None
    ) -> models.RecommendedResponse:
        """GET /pricing/promotions/recommended. Scopes => promotion."""
        response = self._request("GET", RECOMMENDED_PATH, query=query)
        return parse_response(models.RecommendedResponse, response)

    def eligible(self, *, query: models.EligibleQuery | None = None) -> models.EligibleResponse:
        """GET /pricing/promotions/eligible. Scopes => promotion."""
        response = self._request(
            "GET",
            ELIGIBLE_PATH,
            query=query,
            separators={"search[nature]": ",", "search[label_ids]": ","},
        )
        return parse_response(models.EligibleResponse, response)

    def minimum_discounts(
        self, *, body: models.MinimumDiscountsRequest
    ) -> models.MinimumDiscountsResponse:
        """POST /pricing/promotions/eligible/min-discounts. Scopes => promotion."""
        response = self._request("POST", MINIMUM_DISCOUNTS_PATH, body=body)
        return parse_response(models.MinimumDiscountsResponse, response)

    def unjoined(self, *, query: models.UnjoinedQuery | None = None) -> models.UnjoinedResponse:
        """GET /pricing/promotions/unjoined. Scopes => promotion."""
        response = self._request(
            "GET", UNJOINED_PATH, query=query, separators={"search[nature]": ","}
        )
        return parse_response(models.UnjoinedResponse, response)

    def current_for_variant(
        self, product_variant_id: int, *, query: models.CurrentForVariantQuery | None = None
    ) -> models.CurrentForVariantResponse:
        """GET /pricing/promotions/variant-current-promotions/{product_variant_id}. Scopes =>
        promotion."""
        response = self._request(
            "GET",
            CURRENT_FOR_VARIANT_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.CurrentForVariantResponse, response)

    def variants(self, *, query: models.VariantsQuery | None = None) -> models.VariantsResponse:
        """GET /pricing/promotions/variants. Scopes => promotion."""
        response = self._request("GET", VARIANTS_PATH, query=query)
        return parse_response(models.VariantsResponse, response)

    def get_variant(
        self, variant_id: int, *, query: models.GetVariantQuery | None = None
    ) -> models.GetVariantResponse:
        """GET /pricing/promotions/variants/{variant_id}. Scopes => promotion."""
        response = self._request(
            "GET", GET_VARIANT_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.GetVariantResponse, response)

    def rejection_reason(
        self, promotion_variant_id: int, *, query: models.RejectionReasonQuery | None = None
    ) -> models.RejectionReasonResponse:
        """GET /pricing/promotions/variants/rejection-reason/{promotion_variant_id}. Scopes =>
        promotion."""
        response = self._request(
            "GET",
            REJECTION_REASON_PATH.format(promotion_variant_id=path_value(promotion_variant_id)),
            query=query,
        )
        return parse_response(models.RejectionReasonResponse, response)

    def get(self, promotion_id: int) -> models.GetResponse:
        """GET /pricing/promotions/{promotion_id}. Scopes => promotion."""
        response = self._request("GET", GET_PATH.format(promotion_id=path_value(promotion_id)))
        return parse_response(models.GetResponse, response)

    def list_variants(
        self, promotion_id: int, *, query: models.ListVariantsQuery | None = None
    ) -> models.ListVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = self._request(
            "GET", LIST_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.ListVariantsResponse, response)

    def add_variants(
        self, promotion_id: int, *, body: models.AddVariantsRequest
    ) -> models.AddVariantsResponse:
        """POST /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = self._request(
            "POST", ADD_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.AddVariantsResponse, response)

    def update_variants(
        self, promotion_id: int, *, body: models.UpdateVariantsRequest
    ) -> models.UpdateVariantsResponse:
        """PATCH /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = self._request(
            "PATCH", UPDATE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.UpdateVariantsResponse, response)

    def delete_variants(
        self, promotion_id: int, *, body: models.DeleteVariantsRequest
    ) -> models.DeleteVariantsResponse:
        """DELETE /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = self._request(
            "DELETE", DELETE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.DeleteVariantsResponse, response)

    def rejected_variants(
        self, promotion_id: int, *, query: models.RejectedVariantsQuery | None = None
    ) -> models.RejectedVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants/rejected. Scopes => promotion."""
        response = self._request(
            "GET", REJECTED_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.RejectedVariantsResponse, response)

    def add_variants_batch(
        self, promotion_id: int, *, body: models.AddVariantsBatchRequest
    ) -> models.AddVariantsBatchResponse:
        """POST /pricing/promotions/{promotion_id}/variants/batch. Scopes => promotion."""
        response = self._request(
            "POST", ADD_VARIANTS_BATCH_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.AddVariantsBatchResponse, response)

    def update_variants_batch(
        self, promotion_id: int, *, body: models.UpdateVariantsBatchRequest
    ) -> models.UpdateVariantsBatchResponse:
        """PATCH /pricing/promotions/{promotion_id}/variants/batch. Scopes => promotion."""
        response = self._request(
            "PATCH",
            UPDATE_VARIANTS_BATCH_PATH.format(promotion_id=path_value(promotion_id)),
            body=body,
        )
        return parse_response(models.UpdateVariantsBatchResponse, response)

    def eligible_variants(
        self, promotion_id: int, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants/eligible. Scopes => promotion."""
        response = self._request(
            "GET", ELIGIBLE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.EligibleVariantsResponse, response)

    def eligible_variants_v2(
        self, promotion_id: int, *, query: models.EligibleVariantsV2Query | None = None
    ) -> models.EligibleVariantsV2Response:
        """GET /pricing/promotions/{promotion_id}/variants/eligible_v2. Scopes => promotion."""
        response = self._request(
            "GET",
            ELIGIBLE_VARIANTS_V2_PATH.format(promotion_id=path_value(promotion_id)),
            query=query,
        )
        return parse_response(models.EligibleVariantsV2Response, response)

    def variants_to_join(
        self, promotion_id: int, *, query: models.VariantsToJoinQuery | None = None
    ) -> models.VariantsToJoinResponse:
        """GET /pricing/promotions/{promotion_id}/variants/to-join. Scopes => promotion."""
        response = self._request(
            "GET",
            VARIANTS_TO_JOIN_PATH.format(promotion_id=path_value(promotion_id)),
            query=query,
            separators={"search[variant_ids]": ","},
        )
        return parse_response(models.VariantsToJoinResponse, response)

    def commission_discount(
        self, promotion_id: int, variant_id: int
    ) -> models.CommissionDiscountResponse:
        """GET /pricing/promotions/{promotion_id}/variants/{variant_id}/commission-discount.
        Scopes => promotion."""
        response = self._request(
            "GET",
            COMMISSION_DISCOUNT_PATH.format(
                promotion_id=path_value(promotion_id), variant_id=path_value(variant_id)
            ),
        )
        return parse_response(models.CommissionDiscountResponse, response)

    def sample_excel(self, promotion_id: int) -> RawResponse:
        """GET /pricing/promotions/{promotion_id}/variants/excel/sample. Scopes => promotion.
        Response schema is undocumented; returns original bytes and headers."""
        response = self._request(
            "GET", SAMPLE_EXCEL_PATH.format(promotion_id=path_value(promotion_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def import_excel(
        self, promotion_id: int, *, body: models.ImportExcelRequest
    ) -> models.ImportExcelResponse:
        """POST /pricing/promotions/{promotion_id}/variants/excel. Scopes => promotion."""
        response = self._request(
            "POST", IMPORT_EXCEL_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.ImportExcelResponse, response)


class PromotionsAsync(AsyncResource):
    async def list(self, *, query: models.ListQuery | None = None) -> models.ListResponse:
        """GET /pricing/promotions. Scopes => promotion."""
        response = await self._request(
            "GET", LIST_PATH, query=query, separators={"search[nature]": ",", "search[status]": ","}
        )
        return parse_response(models.ListResponse, response)

    async def configs(self) -> models.ConfigsResponse:
        """GET /pricing/promotions/configs. Scopes => promotion."""
        response = await self._request("GET", CONFIGS_PATH)
        return parse_response(models.ConfigsResponse, response)

    async def recommended(
        self, *, query: models.RecommendedQuery | None = None
    ) -> models.RecommendedResponse:
        """GET /pricing/promotions/recommended. Scopes => promotion."""
        response = await self._request("GET", RECOMMENDED_PATH, query=query)
        return parse_response(models.RecommendedResponse, response)

    async def eligible(
        self, *, query: models.EligibleQuery | None = None
    ) -> models.EligibleResponse:
        """GET /pricing/promotions/eligible. Scopes => promotion."""
        response = await self._request(
            "GET",
            ELIGIBLE_PATH,
            query=query,
            separators={"search[nature]": ",", "search[label_ids]": ","},
        )
        return parse_response(models.EligibleResponse, response)

    async def minimum_discounts(
        self, *, body: models.MinimumDiscountsRequest
    ) -> models.MinimumDiscountsResponse:
        """POST /pricing/promotions/eligible/min-discounts. Scopes => promotion."""
        response = await self._request("POST", MINIMUM_DISCOUNTS_PATH, body=body)
        return parse_response(models.MinimumDiscountsResponse, response)

    async def unjoined(
        self, *, query: models.UnjoinedQuery | None = None
    ) -> models.UnjoinedResponse:
        """GET /pricing/promotions/unjoined. Scopes => promotion."""
        response = await self._request(
            "GET", UNJOINED_PATH, query=query, separators={"search[nature]": ","}
        )
        return parse_response(models.UnjoinedResponse, response)

    async def current_for_variant(
        self, product_variant_id: int, *, query: models.CurrentForVariantQuery | None = None
    ) -> models.CurrentForVariantResponse:
        """GET /pricing/promotions/variant-current-promotions/{product_variant_id}. Scopes =>
        promotion."""
        response = await self._request(
            "GET",
            CURRENT_FOR_VARIANT_PATH.format(product_variant_id=path_value(product_variant_id)),
            query=query,
        )
        return parse_response(models.CurrentForVariantResponse, response)

    async def variants(
        self, *, query: models.VariantsQuery | None = None
    ) -> models.VariantsResponse:
        """GET /pricing/promotions/variants. Scopes => promotion."""
        response = await self._request("GET", VARIANTS_PATH, query=query)
        return parse_response(models.VariantsResponse, response)

    async def get_variant(
        self, variant_id: int, *, query: models.GetVariantQuery | None = None
    ) -> models.GetVariantResponse:
        """GET /pricing/promotions/variants/{variant_id}. Scopes => promotion."""
        response = await self._request(
            "GET", GET_VARIANT_PATH.format(variant_id=path_value(variant_id)), query=query
        )
        return parse_response(models.GetVariantResponse, response)

    async def rejection_reason(
        self, promotion_variant_id: int, *, query: models.RejectionReasonQuery | None = None
    ) -> models.RejectionReasonResponse:
        """GET /pricing/promotions/variants/rejection-reason/{promotion_variant_id}. Scopes =>
        promotion."""
        response = await self._request(
            "GET",
            REJECTION_REASON_PATH.format(promotion_variant_id=path_value(promotion_variant_id)),
            query=query,
        )
        return parse_response(models.RejectionReasonResponse, response)

    async def get(self, promotion_id: int) -> models.GetResponse:
        """GET /pricing/promotions/{promotion_id}. Scopes => promotion."""
        response = await self._request(
            "GET", GET_PATH.format(promotion_id=path_value(promotion_id))
        )
        return parse_response(models.GetResponse, response)

    async def list_variants(
        self, promotion_id: int, *, query: models.ListVariantsQuery | None = None
    ) -> models.ListVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = await self._request(
            "GET", LIST_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.ListVariantsResponse, response)

    async def add_variants(
        self, promotion_id: int, *, body: models.AddVariantsRequest
    ) -> models.AddVariantsResponse:
        """POST /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = await self._request(
            "POST", ADD_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.AddVariantsResponse, response)

    async def update_variants(
        self, promotion_id: int, *, body: models.UpdateVariantsRequest
    ) -> models.UpdateVariantsResponse:
        """PATCH /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = await self._request(
            "PATCH", UPDATE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.UpdateVariantsResponse, response)

    async def delete_variants(
        self, promotion_id: int, *, body: models.DeleteVariantsRequest
    ) -> models.DeleteVariantsResponse:
        """DELETE /pricing/promotions/{promotion_id}/variants. Scopes => promotion."""
        response = await self._request(
            "DELETE", DELETE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.DeleteVariantsResponse, response)

    async def rejected_variants(
        self, promotion_id: int, *, query: models.RejectedVariantsQuery | None = None
    ) -> models.RejectedVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants/rejected. Scopes => promotion."""
        response = await self._request(
            "GET", REJECTED_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.RejectedVariantsResponse, response)

    async def add_variants_batch(
        self, promotion_id: int, *, body: models.AddVariantsBatchRequest
    ) -> models.AddVariantsBatchResponse:
        """POST /pricing/promotions/{promotion_id}/variants/batch. Scopes => promotion."""
        response = await self._request(
            "POST", ADD_VARIANTS_BATCH_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.AddVariantsBatchResponse, response)

    async def update_variants_batch(
        self, promotion_id: int, *, body: models.UpdateVariantsBatchRequest
    ) -> models.UpdateVariantsBatchResponse:
        """PATCH /pricing/promotions/{promotion_id}/variants/batch. Scopes => promotion."""
        response = await self._request(
            "PATCH",
            UPDATE_VARIANTS_BATCH_PATH.format(promotion_id=path_value(promotion_id)),
            body=body,
        )
        return parse_response(models.UpdateVariantsBatchResponse, response)

    async def eligible_variants(
        self, promotion_id: int, *, query: models.EligibleVariantsQuery | None = None
    ) -> models.EligibleVariantsResponse:
        """GET /pricing/promotions/{promotion_id}/variants/eligible. Scopes => promotion."""
        response = await self._request(
            "GET", ELIGIBLE_VARIANTS_PATH.format(promotion_id=path_value(promotion_id)), query=query
        )
        return parse_response(models.EligibleVariantsResponse, response)

    async def eligible_variants_v2(
        self, promotion_id: int, *, query: models.EligibleVariantsV2Query | None = None
    ) -> models.EligibleVariantsV2Response:
        """GET /pricing/promotions/{promotion_id}/variants/eligible_v2. Scopes => promotion."""
        response = await self._request(
            "GET",
            ELIGIBLE_VARIANTS_V2_PATH.format(promotion_id=path_value(promotion_id)),
            query=query,
        )
        return parse_response(models.EligibleVariantsV2Response, response)

    async def variants_to_join(
        self, promotion_id: int, *, query: models.VariantsToJoinQuery | None = None
    ) -> models.VariantsToJoinResponse:
        """GET /pricing/promotions/{promotion_id}/variants/to-join. Scopes => promotion."""
        response = await self._request(
            "GET",
            VARIANTS_TO_JOIN_PATH.format(promotion_id=path_value(promotion_id)),
            query=query,
            separators={"search[variant_ids]": ","},
        )
        return parse_response(models.VariantsToJoinResponse, response)

    async def commission_discount(
        self, promotion_id: int, variant_id: int
    ) -> models.CommissionDiscountResponse:
        """GET /pricing/promotions/{promotion_id}/variants/{variant_id}/commission-discount.
        Scopes => promotion."""
        response = await self._request(
            "GET",
            COMMISSION_DISCOUNT_PATH.format(
                promotion_id=path_value(promotion_id), variant_id=path_value(variant_id)
            ),
        )
        return parse_response(models.CommissionDiscountResponse, response)

    async def sample_excel(self, promotion_id: int) -> RawResponse:
        """GET /pricing/promotions/{promotion_id}/variants/excel/sample. Scopes => promotion.
        Response schema is undocumented; returns original bytes and headers."""
        response = await self._request(
            "GET", SAMPLE_EXCEL_PATH.format(promotion_id=path_value(promotion_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def import_excel(
        self, promotion_id: int, *, body: models.ImportExcelRequest
    ) -> models.ImportExcelResponse:
        """POST /pricing/promotions/{promotion_id}/variants/excel. Scopes => promotion."""
        response = await self._request(
            "POST", IMPORT_EXCEL_PATH.format(promotion_id=path_value(promotion_id)), body=body
        )
        return parse_response(models.ImportExcelResponse, response)
