"""Digikala plp: request and response models."""

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
    search_id_or_title: str | None = Field(
        default=None, validation_alias="search[idOrTitle]", serialization_alias="search[idOrTitle]"
    )
    search_statuses: list[str] | None = Field(
        default=None, validation_alias="search[statuses]", serialization_alias="search[statuses]"
    )
    search_start_at: str | None = Field(
        default=None, validation_alias="search[startAt]", serialization_alias="search[startAt]"
    )
    search_end_at: str | None = Field(
        default=None, validation_alias="search[endAt]", serialization_alias="search[endAt]"
    )
    search_is_ad_plp: bool | None = Field(
        default=None, validation_alias="search[isAdPLP]", serialization_alias="search[isAdPLP]"
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
    title: str | None = Field(default=None)
    platform: str | None = Field(default=None)
    link: str | None = Field(default=None)
    status: str | None = Field(default=None)
    start_at: str | None = Field(default=None)
    end_at: str | None = Field(default=None)
    isadplp: bool | None = Field(default=None)
    variants_count: int | None = Field(default=None)
    total_discount: int | None = Field(default=None)


class DeleteRequest(RequestSchema):
    promotion_id: int


class DeleteResponseData(APIResponseSchema):
    message: str | None = Field(default=None)


class CreateRequest(RequestSchema):
    title: str
    platform: str
    start_at: int = Field(validation_alias="startAt", serialization_alias="startAt")
    end_at: int = Field(validation_alias="endAt", serialization_alias="endAt")
    is_ad_plp: bool = Field(validation_alias="isAdPLP", serialization_alias="isAdPLP")


class CreateResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    id: int | None = Field(default=None)


class UpdateRequest(RequestSchema):
    promotion_id: int
    title: str
    platform: str
    start_at: int = Field(validation_alias="startAt", serialization_alias="startAt")
    end_at: int = Field(validation_alias="endAt", serialization_alias="endAt")
    is_ad_plp: bool = Field(validation_alias="isAdPLP", serialization_alias="isAdPLP")


class UpdateResponse(APIResponseSchema):
    status: str
    data: DeleteResponseData


class GetQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["id"] | None = Field(default=None)
    order: str | None = Field(default=None)
    product_or_variant_id: str | None = Field(
        default=None,
        validation_alias="productOrVariantId",
        serialization_alias="productOrVariantId",
    )


class GetResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: str | None = Field(default=None)


class GetResponseDataPager(APIResponseSchema):
    page: int | None = Field(default=None)
    item_per_page: int | None = Field(default=None)
    total_pages: int | None = Field(default=None)
    total_rows: int | None = Field(default=None)


class GetResponseDataItemsItemColor(APIResponseSchema):
    title: str | None = Field(default=None)
    hex_code: str | None = Field(
        default=None, validation_alias="hexCode", serialization_alias="hexCode"
    )


class DeleteVariantsRequest(RequestSchema):
    promotion_id: int
    variant_ids: list[int]


class DeleteVariantsResponse(APIResponseSchema):
    status: str
    data: DeleteResponseData


class EligibleVariantsQuery(QuerySchema):
    page: int | None = Field(default=None)
    size: int | None = Field(default=None)
    sort: Literal["latest", "price_low", "price_high", "earliest"] | None = Field(default=None)
    order: str | None = Field(default=None)
    search_only_buy_box_winner: bool | None = Field(
        default=None,
        validation_alias="search[onlyBuyBoxWinner]",
        serialization_alias="search[onlyBuyBoxWinner]",
    )
    search_id_or_title: str | None = Field(
        default=None, validation_alias="search[idOrTitle]", serialization_alias="search[idOrTitle]"
    )


class EligibleVariantsResponseDataSortData(APIResponseSchema):
    sort_column: str | None = Field(default=None)
    sort_order: str | None = Field(default=None)
    sort_columns: list[str] | None = Field(default=None)


class EligibleVariantsResponseDataItemsItemColor(APIResponseSchema):
    title: str | None = Field(default=None)
    hex_code: str | None = Field(
        default=None, validation_alias="hexCode", serialization_alias="hexCode"
    )


class SampleExcelResponseDataExcelFile(APIResponseSchema):
    name: str | None = Field(default=None)
    content: str | None = Field(default=None)
    mime_type: str | None = Field(
        default=None, validation_alias="mimeType", serialization_alias="mimeType"
    )


class ExportResponseDataExcelFile(APIResponseSchema):
    name: str | None = Field(default=None)
    content: str | None = Field(default=None)
    mime_type: str | None = Field(
        default=None, validation_alias="mimeType", serialization_alias="mimeType"
    )


class ImportExcelRequest(RequestSchema):
    title: str
    platform: JsonValue
    start_at: str = Field(validation_alias="startAt", serialization_alias="startAt")
    end_at: str = Field(validation_alias="endAt", serialization_alias="endAt")
    is_ad_plp: bool = Field(validation_alias="isAdPLP", serialization_alias="isAdPLP")
    promotion_id: int | None = Field(
        default=None, validation_alias="promotionId", serialization_alias="promotionId"
    )
    file_id: int = Field(validation_alias="fileId", serialization_alias="fileId")


class ImportExcelResponseData(APIResponseSchema):
    message: str | None = Field(default=None)
    import_request_id: int | None = Field(default=None)
    promotion_id: int | None = Field(
        default=None, validation_alias="promotionId", serialization_alias="promotionId"
    )


class ListResponseData(APIResponseSchema):
    sort_data: ListResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[ListResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class DeleteResponse(APIResponseSchema):
    status: str
    data: DeleteResponseData


class CreateResponse(APIResponseSchema):
    status: str
    data: CreateResponseData


class GetResponseDataItemsItem(APIResponseSchema):
    imagelink: str | None = Field(default=None)
    productid: int | None = Field(default=None)
    productlink: str | None = Field(default=None)
    productvariantid: int | None = Field(default=None)
    productvarianttitle: str | None = Field(default=None)
    producttitle: str | None = Field(default=None)
    categorytitle: str | None = Field(default=None)
    supplycategorytitle: str | None = Field(default=None)
    sellingprice: int | None = Field(default=None)
    rrpprice: int | None = Field(default=None)
    lastweekproductviewcount: int | None = Field(default=None)
    lastweeksalescount: int | None = Field(default=None)
    size: str | None = Field(default=None)
    color: GetResponseDataItemsItemColor | None = Field(default=None)


class EligibleVariantsResponseDataItemsItem(APIResponseSchema):
    categorytitle: str | None = Field(default=None)
    color: EligibleVariantsResponseDataItemsItemColor | None = Field(default=None)
    imagelink: str | None = Field(default=None)
    lastweekproductviewcount: int | None = Field(default=None)
    lastweeksalescount: int | None = Field(default=None)
    productid: int | None = Field(default=None)
    productlink: str | None = Field(default=None)
    producttitle: str | None = Field(default=None)
    productvariantid: int | None = Field(default=None)
    productvarianttitle: str | None = Field(default=None)
    rrpprice: int | None = Field(default=None)
    sellingprice: int | None = Field(default=None)
    size: str | None = Field(default=None)
    supplycategorytitle: str | None = Field(default=None)


class SampleExcelResponseData(APIResponseSchema):
    excel_file: SampleExcelResponseDataExcelFile | None = Field(
        default=None, validation_alias="excelFile", serialization_alias="excelFile"
    )


class ExportResponseData(APIResponseSchema):
    excel_file: ExportResponseDataExcelFile | None = Field(
        default=None, validation_alias="excelFile", serialization_alias="excelFile"
    )


class ImportExcelResponse(APIResponseSchema):
    status: str
    data: ImportExcelResponseData


class ListResponse(APIResponseSchema):
    status: str
    data: ListResponseData


class GetResponseData(APIResponseSchema):
    sort_data: GetResponseDataSortData | None = Field(default=None)
    pager: GetResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[GetResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class EligibleVariantsResponseData(APIResponseSchema):
    sort_data: EligibleVariantsResponseDataSortData | None = Field(default=None)
    pager: ListResponseDataPager | None = Field(default=None)
    form_data: list[JsonValue] | None = Field(default=None)
    items: list[EligibleVariantsResponseDataItemsItem] | None = Field(default=None)
    meta_data: ObjectMap[JsonValue] | None = Field(default=None)


class SampleExcelResponse(APIResponseSchema):
    status: int | str
    data: SampleExcelResponseData


class ExportResponse(APIResponseSchema):
    status: int | str
    data: ExportResponseData


class GetResponse(APIResponseSchema):
    status: str
    data: GetResponseData


class EligibleVariantsResponse(APIResponseSchema):
    status: str
    data: EligibleVariantsResponseData


__all__ = [
    "CreateRequest",
    "CreateResponse",
    "CreateResponseData",
    "DeleteRequest",
    "DeleteResponse",
    "DeleteResponseData",
    "DeleteVariantsRequest",
    "DeleteVariantsResponse",
    "EligibleVariantsQuery",
    "EligibleVariantsResponse",
    "EligibleVariantsResponseData",
    "EligibleVariantsResponseDataItemsItem",
    "EligibleVariantsResponseDataItemsItemColor",
    "EligibleVariantsResponseDataSortData",
    "ExportResponse",
    "ExportResponseData",
    "ExportResponseDataExcelFile",
    "GetQuery",
    "GetResponse",
    "GetResponseData",
    "GetResponseDataItemsItem",
    "GetResponseDataItemsItemColor",
    "GetResponseDataPager",
    "GetResponseDataSortData",
    "ImportExcelRequest",
    "ImportExcelResponse",
    "ImportExcelResponseData",
    "ListQuery",
    "ListResponse",
    "ListResponseData",
    "ListResponseDataItemsItem",
    "ListResponseDataPager",
    "ListResponseDataSortData",
    "SampleExcelResponse",
    "SampleExcelResponseData",
    "SampleExcelResponseDataExcelFile",
    "UpdateRequest",
    "UpdateResponse",
]
