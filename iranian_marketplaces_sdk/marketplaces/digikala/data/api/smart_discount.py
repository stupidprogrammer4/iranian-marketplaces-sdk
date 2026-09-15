"""Digikala smart discount: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class EligibleQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["latest", "price_low", "price_high", "earliest"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )
    search_only_buy_box_winner: bool | None = Field(
        default=None,
        validation_alias="search[onlyBuyBoxWinner]",
        serialization_alias="search[onlyBuyBoxWinner]",
    )


class EligibleResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class EligibleResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class EligibleResponseDataItemsItem(APIResponseSchema):
    promotion_variant_id: int | None = Field(default=None)
    parent_id: int | None = Field(default=None)
    status: str | None = Field(default=None)
    rejection_reason: str | None = Field(default=None)
    image_link: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    category_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    product_variant_id: int | None = Field(default=None)
    product_variant_title: str | None = Field(default=None)
    buy_box_winner_price: int | None = Field(default=None)
    min_price_in_promotion: int | None = Field(default=None)
    min_sku_selling_price: int | None = Field(default=None)
    discount_percent: int | None = Field(default=None)
    rrp_price: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    cash_selling_price: int | None = Field(default=None)
    cash_rrp_price: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    credit_rrp_price: int | None = Field(default=None)
    credit_increase_percentage: float | int | None = Field(default=None)
    min_incredible_discount: int | None = Field(default=None)
    digikala_stock: int | None = Field(default=None)
    seller_stock: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    commission: int | None = Field(default=None)
    selling_stock: int | None = Field(default=None)
    promotion_limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    min_category_discount: int | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    meta_data: list[JsonValue] | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_sales_count: int | None = Field(default=None)
    is_highly_demanded_product: bool | None = Field(default=None)
    already_exists_in_incredible_promotion: bool | None = Field(default=None)
    already_exist_in_same_promotion: bool | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)
    has_commission_discount: bool | None = Field(default=None)
    is_auto_joined: bool | None = Field(default=None)
    can_join_to_mega_promotion: bool | None = Field(default=None)
    product_type: str | None = Field(default=None)
    incentive: bool | None = Field(default=None)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )
    search_status: list[str] | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_started_at: str | None = Field(
        default=None, validation_alias="search[startedAt]", serialization_alias="search[startedAt]"
    )
    search_end_at: str | None = Field(
        default=None, validation_alias="search[endAt]", serialization_alias="search[endAt]"
    )


class ListResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class ListResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListResponseDataItemsItemAutoJoined(APIResponseSchema):
    normal: bool | None = Field(default=None)
    mega_promotion: bool | None = Field(default=None)


class CreateBatchRequest(RequestSchema):
    data: list[JsonValue]


class CreateBatchResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateBatchRequest(RequestSchema):
    promotion_variant_ids: list[int] = Field(
        validation_alias="promotionVariantIds", serialization_alias="promotionVariantIds"
    )
    discount: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    order_limit: int | None = Field(
        default=None, validation_alias="orderLimit", serialization_alias="orderLimit"
    )
    started_at: str | None = Field(
        default=None, validation_alias="startedAt", serialization_alias="startedAt"
    )
    end_at: str | None = Field(default=None, validation_alias="endAt", serialization_alias="endAt")


class UpdateBatchResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class CreateRequest(RequestSchema):
    data: list[JsonValue]


class CreateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class UpdateRequest(RequestSchema):
    promotion_variant_id: int = Field(
        validation_alias="promotionVariantId", serialization_alias="promotionVariantId"
    )
    promotion_price: int | None = Field(
        default=None, validation_alias="promotionPrice", serialization_alias="promotionPrice"
    )
    discount: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    order_limit: int | None = Field(
        default=None, validation_alias="orderLimit", serialization_alias="orderLimit"
    )
    started_at: str | None = Field(
        default=None, validation_alias="startedAt", serialization_alias="startedAt"
    )
    end_at: str | None = Field(default=None, validation_alias="endAt", serialization_alias="endAt")


class UpdateResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class DeleteRequest(RequestSchema):
    variant_ids: list[int]


class DeleteResponseData(APIResponseSchema):
    id: int | None = Field(default=None)
    success: bool | None = Field(default=None)
    message: str | None = Field(default=None)


class DeleteAllRequest(RequestSchema):
    variant_ids: list[int]


class DeleteAllResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class ExportResponseData(APIResponseSchema):
    success: bool | None = Field(default=None)


class ImportExcelRequest(RequestSchema):
    file_id: int | None = Field(default=None)
    file_ids: list[JsonValue] | None = Field(default=None)


class ImportExcelResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    import_request_ids: list[JsonValue] | None = Field(
        default=None, validation_alias="importRequestIds", serialization_alias="importRequestIds"
    )


class DeleteAllAsyncRequest(RequestSchema):
    file_id: int


class DeleteAllAsyncResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    import_request_id: int | None = Field(default=None)


class AutoJoinedQuery(QuerySchema):
    promotion_variant_id: int = Field(
        validation_alias="promotionVariantId", serialization_alias="promotionVariantId"
    )


class AutoJoinedResponseDataPromotionsItem(APIResponseSchema):
    promotion_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    promotion_status: str | None = Field(default=None)
    promotion_variant_status: str | None = Field(default=None)
    started_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    categories: list[str] | None = Field(default=None)
    discount_type_percent: int | None = Field(default=None)
    discount_type_amount: int | None = Field(default=None)
    min_price: int | None = Field(default=None)
    max_price: int | None = Field(default=None)
    max_discount: int | None = Field(default=None)
    min_variants: int | None = Field(default=None)
    promotion_link: str | None = Field(default=None)
    has_banner: bool | None = Field(default=None)
    condition: list[JsonValue] | None = Field(default=None)


class EligibleResponseData(APIResponseSchema):
    sort_data: EligibleResponseDataSortData | None = Field(default=None)
    pager: EligibleResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    promotion_variant_id: int | None = Field(default=None)
    variant_id: int | None = Field(default=None)
    variant_price_id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    rrp_price: int | None = Field(default=None)
    cash_selling_price: int | None = Field(default=None)
    cash_rrp_price: int | None = Field(default=None)
    cash_discount: int | None = Field(default=None)
    credit_selling_price: int | None = Field(default=None)
    credit_rrp_price: int | None = Field(default=None)
    credit_discount: int | None = Field(default=None)
    credit_increase_percentage: float | int | None = Field(default=None)
    selling_stock: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    limit: int | None = Field(default=None)
    order_limit: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    min_discount: int | None = Field(default=None)
    max_allowable_price: int | None = Field(default=None)
    title: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    promotion_status: str | None = Field(default=None)
    started_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    image_link: str | None = Field(default=None)
    auto_joined: ListResponseDataItemsItemAutoJoined | None = Field(default=None)
    can_join_to_mega_promotion: bool | None = Field(default=None)
    incentive: bool | None = Field(default=None)


class CreateBatchResponse(APIResponseSchema):
    status: str
    data: CreateBatchResponseData


class UpdateBatchResponse(APIResponseSchema):
    status: str
    data: UpdateBatchResponseData


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class DeleteResponse(APIResponseSchema):
    status: str
    data: DeleteResponseData


class DeleteAllResponse(APIResponseSchema):
    status: str
    data: DeleteAllResponseData


class ExportResponse(APIResponseSchema):
    status: int | str
    data: ExportResponseData


class ImportExcelResponse(APIResponseSchema):
    status: str
    data: ImportExcelResponseData


class DeleteAllAsyncResponse(APIResponseSchema):
    status: str
    data: DeleteAllAsyncResponseData


class AutoJoinedResponseData(APIResponseSchema):
    promotion_variant_id: int | None = Field(default=None)
    selling_price: int | None = Field(default=None)
    promotion_price: int | None = Field(default=None)
    promotions: list[AutoJoinedResponseDataPromotionsItem] | None = Field(default=None)


class EligibleResponse(APIResponseSchema):
    status: str
    data: EligibleResponseData


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class AutoJoinedResponse(APIResponseSchema):
    status: int | str
    data: AutoJoinedResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


__all__ = [
    "AutoJoinedQuery",
    "AutoJoinedResponse",
    "AutoJoinedResponseData",
    "AutoJoinedResponseDataPromotionsItem",
    "CreateBatchRequest",
    "CreateBatchResponse",
    "CreateBatchResponseData",
    "CreateRequest",
    "CreateResponse",
    "CreateResponseData",
    "DeleteAllAsyncRequest",
    "DeleteAllAsyncResponse",
    "DeleteAllAsyncResponseData",
    "DeleteAllRequest",
    "DeleteAllResponse",
    "DeleteAllResponseData",
    "DeleteRequest",
    "DeleteResponse",
    "DeleteResponseData",
    "EligibleQuery",
    "EligibleResponse",
    "EligibleResponseData",
    "EligibleResponseDataItemsItem",
    "EligibleResponseDataPager",
    "EligibleResponseDataSortData",
    "ExportResponse",
    "ExportResponseData",
    "ImportExcelRequest",
    "ImportExcelResponse",
    "ImportExcelResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataItemsItemAutoJoined",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "UpdateBatchRequest",
    "UpdateBatchResponse",
    "UpdateBatchResponseData",
    "UpdateRequest",
    "UpdateResponse",
    "UpdateResponseData",
]
