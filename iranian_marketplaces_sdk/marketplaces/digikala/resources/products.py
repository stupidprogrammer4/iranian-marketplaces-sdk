"""Digikala products: sync and async resource clients."""

from __future__ import annotations

from iranian_marketplaces_sdk.marketplaces.digikala.data.api import products as models
from iranian_marketplaces_sdk.marketplaces.digikala.resources.base import (
    AsyncResource,
    RawResponse,
    SyncResource,
    Upload,
    parse_response,
    path_value,
)

SEARCH_PATH = "/product-creation/search/v2"
SUGGESTIONS_PATH = "/product-creation/search/suggestion/v2"
SELLER_PERMISSION_PATH = "/product-creation/be-seller/{product_id}"
SEARCH_CATEGORIES_PATH = "/product-creation/search/category/v2/{keyword}"
VALIDATE_CATEGORY_PATH = "/product-creation/category/{category_id}/validation"
VALIDATE_DETAILS_PATH = "/product-creation/product/detail/validation"
COUNT_DRAFTS_PATH = "/product-creation/draft-product/count"
GET_DRAFT_PATH = "/product-creation/draft-product/{draft_product_id}"
GET_AUTO_TITLE_PATH = "/product-creation/{draft_product_id}/auto-title"
SAVE_AUTO_TITLE_PATH = "/product-creation/auto-title/save"
GET_ATTRIBUTES_PATH = "/product-creation/attributes/{category_id}"
SAVE_ATTRIBUTES_PATH = "/product-creation/attributes"
UPLOAD_BRAND_LOGO_PATH = "/product-creation/images/requests/brand-logo/upload"
UPLOAD_REQUEST_IMAGE_PATH = "/product-creation/images/requests/upload"
UPLOAD_IMAGE_PATH = "/product-creation/images/upload"
GENERATE_IMAGE_PATH = "/product-creation/images/ai"
SAVE_PATH = "/product-creation/save"
ASSIGN_PATH = "/product-creation/assign"
REQUEST_BRAND_PATH = "/product-creation/brand/request"
LIST_BRANDS_PATH = "/product-creation/brand"
LIST_DRAFTS_PATH = "/draft-products/seller"
DELETE_DRAFT_PATH = "/draft-products/{draft_product_id}"
LIST_SELLER_PATH = "/products/seller"
SCORE_PATH = "/products/{product_id}/score"
PUBLISH_PATH = "/product-edit/{product_id}/publish"
GET_EDIT_PATH = "/product-edit/{product_id}"
UPDATE_PATH = "/product-edit/{product_id}"
GENERATE_TITLE_PATH = "/product-edit/{category_id}/auto-title"


class ProductsSync(SyncResource):
    def search(self, *, query: models.SearchQuery) -> models.SearchResponse:
        """GET /product-creation/search/v2. Scopes => product."""
        response = self._request("GET", SEARCH_PATH, query=query)
        return parse_response(models.SearchResponse, response)

    def suggestions(
        self, *, query: models.SuggestionsQuery | None = None
    ) -> models.SuggestionsResponse:
        """GET /product-creation/search/suggestion/v2. Scopes => product."""
        response = self._request("GET", SUGGESTIONS_PATH, query=query)
        return parse_response(models.SuggestionsResponse, response)

    def seller_permission(self, product_id: int) -> models.SellerPermissionResponse:
        """GET /product-creation/be-seller/{product_id}. Scopes => product."""
        response = self._request(
            "GET", SELLER_PERMISSION_PATH.format(product_id=path_value(product_id))
        )
        return parse_response(models.SellerPermissionResponse, response)

    def search_categories(self, keyword: str | int) -> models.SearchCategoriesResponse:
        """GET /product-creation/search/category/v2/{keyword}. Scopes => product."""
        response = self._request("GET", SEARCH_CATEGORIES_PATH.format(keyword=path_value(keyword)))
        return parse_response(models.SearchCategoriesResponse, response)

    def validate_category(self, category_id: int) -> models.ValidateCategoryResponse:
        """GET /product-creation/category/{category_id}/validation. Scopes => product."""
        response = self._request(
            "GET", VALIDATE_CATEGORY_PATH.format(category_id=path_value(category_id))
        )
        return parse_response(models.ValidateCategoryResponse, response)

    def validate_details(
        self, *, body: models.ValidateDetailsRequest
    ) -> models.ValidateDetailsResponse:
        """POST /product-creation/product/detail/validation. Scopes => product."""
        response = self._request("POST", VALIDATE_DETAILS_PATH, body=body)
        return parse_response(models.ValidateDetailsResponse, response)

    def count_drafts(self) -> models.CountDraftsResponse:
        """GET /product-creation/draft-product/count. Scopes => product."""
        response = self._request("GET", COUNT_DRAFTS_PATH)
        return parse_response(models.CountDraftsResponse, response)

    def get_draft(self, draft_product_id: int) -> models.GetDraftResponse:
        """GET /product-creation/draft-product/{draft_product_id}. Scopes => product."""
        response = self._request(
            "GET", GET_DRAFT_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return parse_response(models.GetDraftResponse, response)

    def get_auto_title(self, draft_product_id: int) -> models.GetAutoTitleResponse:
        """GET /product-creation/{draft_product_id}/auto-title. Scopes => product."""
        response = self._request(
            "GET", GET_AUTO_TITLE_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return parse_response(models.GetAutoTitleResponse, response)

    def save_auto_title(self, *, body: models.SaveAutoTitleRequest) -> models.SaveAutoTitleResponse:
        """POST /product-creation/auto-title/save. Scopes => product."""
        response = self._request("POST", SAVE_AUTO_TITLE_PATH, body=body)
        return parse_response(models.SaveAutoTitleResponse, response)

    def get_attributes(self, category_id: int) -> models.GetAttributesResponse:
        """GET /product-creation/attributes/{category_id}. Scopes => product."""
        response = self._request(
            "GET", GET_ATTRIBUTES_PATH.format(category_id=path_value(category_id))
        )
        return parse_response(models.GetAttributesResponse, response)

    def save_attributes(self, *, body: models.SaveAttributesRequest) -> RawResponse:
        """POST /product-creation/attributes. Scopes => product. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request("POST", SAVE_ATTRIBUTES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    def upload_brand_logo(self, *, file: Upload) -> models.UploadBrandLogoResponse:
        """POST /product-creation/images/requests/brand-logo/upload. Scopes => product."""
        response = self._request("POST", UPLOAD_BRAND_LOGO_PATH, file=file)
        return parse_response(models.UploadBrandLogoResponse, response)

    def upload_request_image(self, *, file: Upload) -> models.UploadRequestImageResponse:
        """POST /product-creation/images/requests/upload. Scopes => product."""
        response = self._request("POST", UPLOAD_REQUEST_IMAGE_PATH, file=file)
        return parse_response(models.UploadRequestImageResponse, response)

    def upload_image(self, *, file: Upload) -> models.UploadImageResponse:
        """POST /product-creation/images/upload. Scopes => product."""
        response = self._request("POST", UPLOAD_IMAGE_PATH, file=file)
        return parse_response(models.UploadImageResponse, response)

    def generate_image(self, *, body: models.GenerateImageRequest) -> models.GenerateImageResponse:
        """POST /product-creation/images/ai. Scopes => product."""
        response = self._request("POST", GENERATE_IMAGE_PATH, body=body)
        return parse_response(models.GenerateImageResponse, response)

    def save(self, *, body: models.SaveRequest | None = None) -> models.SaveResponse:
        """POST /product-creation/save. Scopes => product."""
        response = self._request("POST", SAVE_PATH, body=body)
        return parse_response(models.SaveResponse, response)

    def assign(self, *, body: models.AssignRequest) -> models.AssignResponse:
        """POST /product-creation/assign. Scopes => product."""
        response = self._request("POST", ASSIGN_PATH, body=body)
        return parse_response(models.AssignResponse, response)

    def request_brand(self, *, body: models.RequestBrandRequest) -> models.RequestBrandResponse:
        """POST /product-creation/brand/request. Scopes => product."""
        response = self._request("POST", REQUEST_BRAND_PATH, body=body)
        return parse_response(models.RequestBrandResponse, response)

    def list_brands(
        self, *, query: models.ListBrandsQuery | None = None
    ) -> models.ListBrandsResponse:
        """GET /product-creation/brand. Scopes => product."""
        response = self._request("GET", LIST_BRANDS_PATH, query=query)
        return parse_response(models.ListBrandsResponse, response)

    def list_drafts(
        self, *, query: models.ListDraftsQuery | None = None
    ) -> models.ListDraftsResponse:
        """GET /draft-products/seller. Scopes => product."""
        response = self._request(
            "GET",
            LIST_DRAFTS_PATH,
            query=query,
            separators={"search[brand_ids]": ",", "search[category_ids]": ","},
        )
        return parse_response(models.ListDraftsResponse, response)

    def delete_draft(self, draft_product_id: int) -> RawResponse:
        """DELETE /draft-products/{draft_product_id}. Scopes => product. Response schema is
        undocumented; returns original bytes and headers."""
        response = self._request(
            "DELETE", DELETE_DRAFT_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def list_seller(
        self, *, query: models.ListSellerQuery | None = None
    ) -> models.ListSellerResponse:
        """GET /products/seller. Scopes => product."""
        response = self._request("GET", LIST_SELLER_PATH, query=query)
        return parse_response(models.ListSellerResponse, response)

    def score(self, product_id: int) -> models.ScoreResponse:
        """GET /products/{product_id}/score. Scopes => product."""
        response = self._request("GET", SCORE_PATH.format(product_id=path_value(product_id)))
        return parse_response(models.ScoreResponse, response)

    def publish(
        self, product_id: int, *, body: models.PublishRequest | None = None
    ) -> models.PublishResponse:
        """POST /product-edit/{product_id}/publish. Scopes => product."""
        response = self._request(
            "POST", PUBLISH_PATH.format(product_id=path_value(product_id)), body=body
        )
        return parse_response(models.PublishResponse, response)

    def get_edit(self, product_id: int) -> models.GetEditResponse:
        """GET /product-edit/{product_id}. Scopes => product."""
        response = self._request("GET", GET_EDIT_PATH.format(product_id=path_value(product_id)))
        return parse_response(models.GetEditResponse, response)

    def update(self, product_id: int, *, body: models.UpdateRequest) -> RawResponse:
        """PUT /product-edit/{product_id}. Scopes => product. Response schema is undocumented;
        returns original bytes and headers."""
        response = self._request(
            "PUT", UPDATE_PATH.format(product_id=path_value(product_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)

    def generate_title(
        self, category_id: int, *, body: models.GenerateTitleRequest
    ) -> models.GenerateTitleResponse:
        """POST /product-edit/{category_id}/auto-title. Scopes => product."""
        response = self._request(
            "POST", GENERATE_TITLE_PATH.format(category_id=path_value(category_id)), body=body
        )
        return parse_response(models.GenerateTitleResponse, response)


class ProductsAsync(AsyncResource):
    async def search(self, *, query: models.SearchQuery) -> models.SearchResponse:
        """GET /product-creation/search/v2. Scopes => product."""
        response = await self._request("GET", SEARCH_PATH, query=query)
        return parse_response(models.SearchResponse, response)

    async def suggestions(
        self, *, query: models.SuggestionsQuery | None = None
    ) -> models.SuggestionsResponse:
        """GET /product-creation/search/suggestion/v2. Scopes => product."""
        response = await self._request("GET", SUGGESTIONS_PATH, query=query)
        return parse_response(models.SuggestionsResponse, response)

    async def seller_permission(self, product_id: int) -> models.SellerPermissionResponse:
        """GET /product-creation/be-seller/{product_id}. Scopes => product."""
        response = await self._request(
            "GET", SELLER_PERMISSION_PATH.format(product_id=path_value(product_id))
        )
        return parse_response(models.SellerPermissionResponse, response)

    async def search_categories(self, keyword: str | int) -> models.SearchCategoriesResponse:
        """GET /product-creation/search/category/v2/{keyword}. Scopes => product."""
        response = await self._request(
            "GET", SEARCH_CATEGORIES_PATH.format(keyword=path_value(keyword))
        )
        return parse_response(models.SearchCategoriesResponse, response)

    async def validate_category(self, category_id: int) -> models.ValidateCategoryResponse:
        """GET /product-creation/category/{category_id}/validation. Scopes => product."""
        response = await self._request(
            "GET", VALIDATE_CATEGORY_PATH.format(category_id=path_value(category_id))
        )
        return parse_response(models.ValidateCategoryResponse, response)

    async def validate_details(
        self, *, body: models.ValidateDetailsRequest
    ) -> models.ValidateDetailsResponse:
        """POST /product-creation/product/detail/validation. Scopes => product."""
        response = await self._request("POST", VALIDATE_DETAILS_PATH, body=body)
        return parse_response(models.ValidateDetailsResponse, response)

    async def count_drafts(self) -> models.CountDraftsResponse:
        """GET /product-creation/draft-product/count. Scopes => product."""
        response = await self._request("GET", COUNT_DRAFTS_PATH)
        return parse_response(models.CountDraftsResponse, response)

    async def get_draft(self, draft_product_id: int) -> models.GetDraftResponse:
        """GET /product-creation/draft-product/{draft_product_id}. Scopes => product."""
        response = await self._request(
            "GET", GET_DRAFT_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return parse_response(models.GetDraftResponse, response)

    async def get_auto_title(self, draft_product_id: int) -> models.GetAutoTitleResponse:
        """GET /product-creation/{draft_product_id}/auto-title. Scopes => product."""
        response = await self._request(
            "GET", GET_AUTO_TITLE_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return parse_response(models.GetAutoTitleResponse, response)

    async def save_auto_title(
        self, *, body: models.SaveAutoTitleRequest
    ) -> models.SaveAutoTitleResponse:
        """POST /product-creation/auto-title/save. Scopes => product."""
        response = await self._request("POST", SAVE_AUTO_TITLE_PATH, body=body)
        return parse_response(models.SaveAutoTitleResponse, response)

    async def get_attributes(self, category_id: int) -> models.GetAttributesResponse:
        """GET /product-creation/attributes/{category_id}. Scopes => product."""
        response = await self._request(
            "GET", GET_ATTRIBUTES_PATH.format(category_id=path_value(category_id))
        )
        return parse_response(models.GetAttributesResponse, response)

    async def save_attributes(self, *, body: models.SaveAttributesRequest) -> RawResponse:
        """POST /product-creation/attributes. Scopes => product. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request("POST", SAVE_ATTRIBUTES_PATH, body=body)
        return RawResponse(response.status_code, response.headers, response.content)

    async def upload_brand_logo(self, *, file: Upload) -> models.UploadBrandLogoResponse:
        """POST /product-creation/images/requests/brand-logo/upload. Scopes => product."""
        response = await self._request("POST", UPLOAD_BRAND_LOGO_PATH, file=file)
        return parse_response(models.UploadBrandLogoResponse, response)

    async def upload_request_image(self, *, file: Upload) -> models.UploadRequestImageResponse:
        """POST /product-creation/images/requests/upload. Scopes => product."""
        response = await self._request("POST", UPLOAD_REQUEST_IMAGE_PATH, file=file)
        return parse_response(models.UploadRequestImageResponse, response)

    async def upload_image(self, *, file: Upload) -> models.UploadImageResponse:
        """POST /product-creation/images/upload. Scopes => product."""
        response = await self._request("POST", UPLOAD_IMAGE_PATH, file=file)
        return parse_response(models.UploadImageResponse, response)

    async def generate_image(
        self, *, body: models.GenerateImageRequest
    ) -> models.GenerateImageResponse:
        """POST /product-creation/images/ai. Scopes => product."""
        response = await self._request("POST", GENERATE_IMAGE_PATH, body=body)
        return parse_response(models.GenerateImageResponse, response)

    async def save(self, *, body: models.SaveRequest | None = None) -> models.SaveResponse:
        """POST /product-creation/save. Scopes => product."""
        response = await self._request("POST", SAVE_PATH, body=body)
        return parse_response(models.SaveResponse, response)

    async def assign(self, *, body: models.AssignRequest) -> models.AssignResponse:
        """POST /product-creation/assign. Scopes => product."""
        response = await self._request("POST", ASSIGN_PATH, body=body)
        return parse_response(models.AssignResponse, response)

    async def request_brand(
        self, *, body: models.RequestBrandRequest
    ) -> models.RequestBrandResponse:
        """POST /product-creation/brand/request. Scopes => product."""
        response = await self._request("POST", REQUEST_BRAND_PATH, body=body)
        return parse_response(models.RequestBrandResponse, response)

    async def list_brands(
        self, *, query: models.ListBrandsQuery | None = None
    ) -> models.ListBrandsResponse:
        """GET /product-creation/brand. Scopes => product."""
        response = await self._request("GET", LIST_BRANDS_PATH, query=query)
        return parse_response(models.ListBrandsResponse, response)

    async def list_drafts(
        self, *, query: models.ListDraftsQuery | None = None
    ) -> models.ListDraftsResponse:
        """GET /draft-products/seller. Scopes => product."""
        response = await self._request(
            "GET",
            LIST_DRAFTS_PATH,
            query=query,
            separators={"search[brand_ids]": ",", "search[category_ids]": ","},
        )
        return parse_response(models.ListDraftsResponse, response)

    async def delete_draft(self, draft_product_id: int) -> RawResponse:
        """DELETE /draft-products/{draft_product_id}. Scopes => product. Response schema is
        undocumented; returns original bytes and headers."""
        response = await self._request(
            "DELETE", DELETE_DRAFT_PATH.format(draft_product_id=path_value(draft_product_id))
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def list_seller(
        self, *, query: models.ListSellerQuery | None = None
    ) -> models.ListSellerResponse:
        """GET /products/seller. Scopes => product."""
        response = await self._request("GET", LIST_SELLER_PATH, query=query)
        return parse_response(models.ListSellerResponse, response)

    async def score(self, product_id: int) -> models.ScoreResponse:
        """GET /products/{product_id}/score. Scopes => product."""
        response = await self._request("GET", SCORE_PATH.format(product_id=path_value(product_id)))
        return parse_response(models.ScoreResponse, response)

    async def publish(
        self, product_id: int, *, body: models.PublishRequest | None = None
    ) -> models.PublishResponse:
        """POST /product-edit/{product_id}/publish. Scopes => product."""
        response = await self._request(
            "POST", PUBLISH_PATH.format(product_id=path_value(product_id)), body=body
        )
        return parse_response(models.PublishResponse, response)

    async def get_edit(self, product_id: int) -> models.GetEditResponse:
        """GET /product-edit/{product_id}. Scopes => product."""
        response = await self._request(
            "GET", GET_EDIT_PATH.format(product_id=path_value(product_id))
        )
        return parse_response(models.GetEditResponse, response)

    async def update(self, product_id: int, *, body: models.UpdateRequest) -> RawResponse:
        """PUT /product-edit/{product_id}. Scopes => product. Response schema is undocumented;
        returns original bytes and headers."""
        response = await self._request(
            "PUT", UPDATE_PATH.format(product_id=path_value(product_id)), body=body
        )
        return RawResponse(response.status_code, response.headers, response.content)

    async def generate_title(
        self, category_id: int, *, body: models.GenerateTitleRequest
    ) -> models.GenerateTitleResponse:
        """POST /product-edit/{category_id}/auto-title. Scopes => product."""
        response = await self._request(
            "POST", GENERATE_TITLE_PATH.format(category_id=path_value(category_id)), body=body
        )
        return parse_response(models.GenerateTitleResponse, response)
