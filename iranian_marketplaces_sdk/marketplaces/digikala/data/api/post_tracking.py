"""Digikala post tracking: request and response models."""

from __future__ import annotations

from iranian_marketplaces_sdk.common.data import RequestSchema


class ImportTrackingCodesRequest(RequestSchema):
    file_id: int


__all__ = ["ImportTrackingCodesRequest"]
