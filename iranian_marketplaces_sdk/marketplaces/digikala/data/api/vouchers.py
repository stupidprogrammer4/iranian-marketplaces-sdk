"""Digikala vouchers: request and response models."""

from __future__ import annotations

from typing import Literal

from pydantic import Field, JsonValue

from iranian_marketplaces_sdk.common.data import QuerySchema, RequestSchema
from iranian_marketplaces_sdk.marketplaces.digikala.data.api.common import (
    APIResponseSchema,
    ObjectMap,
)


class ListQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_title: str | None = Field(
        default=None, validation_alias="search[title]", serialization_alias="search[title]"
    )
    search_status: str | None = Field(
        default=None, validation_alias="search[status]", serialization_alias="search[status]"
    )
    search_start_at: str | None = Field(
        default=None, validation_alias="search[startAt]", serialization_alias="search[startAt]"
    )
    search_end_at: str | None = Field(
        default=None, validation_alias="search[endAt]", serialization_alias="search[endAt]"
    )
    search_is_private: bool | None = Field(
        default=None, validation_alias="search[isPrivate]", serialization_alias="search[isPrivate]"
    )


class ListResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class ListResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class ListResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    product_id: int | None = Field(default=None)
    product_link: str | None = Field(default=None)
    image_link: str | None = Field(default=None)
    category_title: str | None = Field(default=None)
    stock: int | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_product_sales_count: int | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)


class CreateRequest(RequestSchema):
    product_ids: list[int] = Field(validation_alias="productIds", serialization_alias="productIds")
    title: str
    limit: int
    voucher_type_id: int | None = Field(
        default=None, validation_alias="voucherTypeId", serialization_alias="voucherTypeId"
    )
    type: str | None = Field(default=None)
    percentage: int | None = Field(default=None)
    max_discount: int | None = Field(default=None)
    discount: int | None = Field(default=None)
    min_price_discount_activation: int | None = Field(default=None)
    start_at: str = Field(validation_alias="startAt", serialization_alias="startAt")
    end_at: str = Field(validation_alias="endAt", serialization_alias="endAt")
    is_private: bool = Field(validation_alias="isPrivate", serialization_alias="isPrivate")


class CreateResponseData(APIResponseSchema):
    code: str | None = Field(default=None)


class UpdateRequest(RequestSchema):
    new_product_ids: list[int] = Field(
        validation_alias="newProductIds", serialization_alias="newProductIds"
    )
    deleted_product_ids: list[int] = Field(
        validation_alias="deletedProductIds", serialization_alias="deletedProductIds"
    )
    title: str
    limit: int
    voucher_type_id: int = Field(
        validation_alias="voucherTypeId", serialization_alias="voucherTypeId"
    )
    voucher_id: int = Field(validation_alias="voucherId", serialization_alias="voucherId")
    start_at: str = Field(validation_alias="startAt", serialization_alias="startAt")
    end_at: str = Field(validation_alias="endAt", serialization_alias="endAt")
    is_visible: bool = Field(validation_alias="isVisible", serialization_alias="isVisible")
    is_private: bool = Field(validation_alias="isPrivate", serialization_alias="isPrivate")


class UpdateResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class TypesQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_type: str | None = Field(
        default=None, validation_alias="search[type]", serialization_alias="search[type]"
    )


class TypesResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    type: str | None = Field(default=None)
    percentage: int | None = Field(default=None)
    max_discount: int | None = Field(default=None)
    min_price_to_active_discount: int | None = Field(default=None)
    discount: int | None = Field(default=None)


class GetResponseDataProductsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_id: int | None = Field(
        default=None, validation_alias="productId", serialization_alias="productId"
    )
    title: str | None = Field(default=None)
    product_link: str | None = Field(
        default=None, validation_alias="productLink", serialization_alias="productLink"
    )
    image_link: str | None = Field(
        default=None, validation_alias="imageLink", serialization_alias="imageLink"
    )
    category_title: str | None = Field(
        default=None, validation_alias="categoryTitle", serialization_alias="categoryTitle"
    )
    is_buy_box_winner: bool | None = Field(
        default=None, validation_alias="isBuyBoxWinner", serialization_alias="isBuyBoxWinner"
    )
    stock: int | None = Field(default=None)
    last_week_product_view_count: int | None = Field(
        default=None,
        validation_alias="lastWeekProductViewCount",
        serialization_alias="lastWeekProductViewCount",
    )
    last_week_product_sales_count: int | None = Field(
        default=None,
        validation_alias="lastWeekProductSalesCount",
        serialization_alias="lastWeekProductSalesCount",
    )


class GetResponseDataVoucherVoucherType(APIResponseSchema):
    id: int | None = Field(default=None)
    type: str | None = Field(default=None)
    percentage: int | None = Field(default=None)
    max_discount: int | None = Field(
        default=None, validation_alias="maxDiscount", serialization_alias="maxDiscount"
    )
    min_price_to_active_discount: int | None = Field(
        default=None,
        validation_alias="minPriceToActiveDiscount",
        serialization_alias="minPriceToActiveDiscount",
    )
    discount: int | None = Field(default=None)


class EligibleVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["latest", "price_low", "price_high", "earliest"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_query: str | None = Field(
        default=None, validation_alias="search[query]", serialization_alias="search[query]"
    )
    search_categories: str | None = Field(
        default=None,
        validation_alias="search[categories]",
        serialization_alias="search[categories]",
    )
    search_only_buy_box_winner: bool | None = Field(
        default=None,
        validation_alias="search[onlyBuyBoxWinner]",
        serialization_alias="search[onlyBuyBoxWinner]",
    )
    search_type: str | None = Field(
        default=None, validation_alias="search[type]", serialization_alias="search[type]"
    )


class EligibleVariantsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class EligibleVariantsResponseDataItemsItem(APIResponseSchema):
    id: int | None = Field(default=None)
    product_id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    product_link: str | None = Field(default=None)
    image_link: str | None = Field(default=None)
    category_title: str | None = Field(default=None)
    stock: int | None = Field(default=None)
    last_week_product_view_count: int | None = Field(default=None)
    last_week_product_sales_count: int | None = Field(default=None)
    avg_selling_price: int | None = Field(default=None)
    is_buy_box_winner: bool | None = Field(default=None)


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class UpdateResponse(APIResponseSchema):
    status: str
    data: UpdateResponseData


class TypesResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[TypesResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class GetResponseDataVoucher(APIResponseSchema):
    id: int | None = Field(default=None)
    title: str | None = Field(default=None)
    code: str | None = Field(default=None)
    start_at: str | None = Field(
        default=None, validation_alias="startAt", serialization_alias="startAt"
    )
    edn_at: str | None = Field(default=None, validation_alias="ednAt", serialization_alias="ednAt")
    limit: int | None = Field(default=None)
    used: int | None = Field(default=None)
    voucher_type: GetResponseDataVoucherVoucherType | None = Field(
        default=None, validation_alias="voucherType", serialization_alias="voucherType"
    )
    status: str | None = Field(default=None)
    is_advertise_active: bool | None = Field(
        default=None, validation_alias="isAdvertiseActive", serialization_alias="isAdvertiseActive"
    )
    is_edit_active: bool | None = Field(
        default=None, validation_alias="isEditActive", serialization_alias="isEditActive"
    )
    is_visible: bool | None = Field(
        default=None, validation_alias="isVisible", serialization_alias="isVisible"
    )
    plp_link: str | None = Field(
        default=None, validation_alias="plpLink", serialization_alias="plpLink"
    )


class EligibleVariantsResponseData(APIResponseSchema):
    sort_data: EligibleVariantsResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class TypesResponse(APIResponseSchema):
    status: str
    data: TypesResponseData


class GetResponseData(APIResponseSchema):
    products: list[GetResponseDataProductsItem] | None = Field(default=None)
    voucher: GetResponseDataVoucher | None = Field(default=None)
    total_stock: int | None = Field(
        default=None, validation_alias="totalStock", serialization_alias="totalStock"
    )


class EligibleVariantsResponse(APIResponseSchema):
    status: str
    data: EligibleVariantsResponseData


class GetResponse(APIResponseSchema):
    status: int | str
    data: GetResponseData


__all__ = [
    "CreateRequest",
    "CreateResponse",
    "CreateResponseData",
    "EligibleVariantsQuery",
    "EligibleVariantsResponse",
    "EligibleVariantsResponseData",
    "EligibleVariantsResponseDataItemsItem",
    "EligibleVariantsResponseDataSortData",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataProductsItem",
    "GetResponseDataVoucher",
    "GetResponseDataVoucherVoucherType",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "TypesQuery",
    "TypesResponse",
    "TypesResponseData",
    "TypesResponseDataItemsItem",
    "UpdateRequest",
    "UpdateResponse",
    "UpdateResponseData",
]
