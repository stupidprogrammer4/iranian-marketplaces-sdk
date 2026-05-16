"""Shared TypedDicts reused across the Digikala type modules.

NOTE: the ``types`` package intentionally does *not* use ``from __future__
import annotations``. Stringized annotations prevent ``TypedDict`` from
resolving ``NotRequired``/``Required`` qualifiers at runtime, which would
corrupt ``__required_keys__``/``__optional_keys__``. Cross-module references
go through real imports, so no forward references are needed.
"""

from typing import TypedDict

__all__ = [
    "RateLimitResetTime",
    "RateLimit",
    "SortData",
    "Pager",
    "DigikalaDateTime",
    "KeyTitle",
]


class RateLimitResetTime(TypedDict):
    """The ``resetTime`` block inside the health-check rate limit."""

    date: str
    timezone_type: int
    timezone: str


class RateLimit(TypedDict):
    """Current rate-limit window reported by the health-check endpoint."""

    max: int
    current: int
    resetTime: RateLimitResetTime


class SortData(TypedDict):
    """Sorting metadata returned by paginated list endpoints."""

    sort_column: str
    sort_order: str
    sort_columns: list[str]


class Pager(TypedDict):
    """Pagination metadata returned by paginated list endpoints."""

    page: int
    item_per_page: int
    total_pages: int
    total_rows: int


class DigikalaDateTime(TypedDict):
    """Digikala's standard datetime envelope (date + timezone metadata)."""

    date: str
    timezone_type: int
    timezone: str


class KeyTitle(TypedDict):
    """A generic ``{key, title}`` pair used across many endpoints."""

    key: str
    title: str
