"""Basalam — shared models reused across the data modules."""

from iranian_marketplaces_sdk.common.data import RequestSchema

__all__ = ["RangeInput"]


class RangeInput(RequestSchema):
    """A numeric ``start``/``end`` range filter. Both bounds are optional and open-ended."""

    start: int | None = None
    end: int | None = None
