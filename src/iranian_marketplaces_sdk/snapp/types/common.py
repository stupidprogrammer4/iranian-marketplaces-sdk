"""Shared TypedDicts reused across the Snapp type modules.

NOTE: this package must NOT use ``from __future__ import annotations`` —
stringized annotations break ``TypedDict`` ``NotRequired``/``Required``
resolution at runtime. Cross-module references use real imports.
"""

from typing import TypedDict

__all__ = [
    "PaginationLinks",
    "Pagination",
    "Meta",
    "CursorLinks",
    "CursorPagination",
    "CursorMeta",
]


class PaginationLinks(TypedDict):
    """Next/previous page URLs of a paginated Snapp response."""

    next: str | None
    previous: str | None


class Pagination(TypedDict):
    """Pagination block of a Snapp list response."""

    total: int
    count: int
    per_page: int
    current_page: int
    total_pages: int
    links: PaginationLinks


class Meta(TypedDict):
    """The ``meta`` envelope of a Snapp list response."""

    pagination: Pagination


class CursorLinks(TypedDict):
    """Links block of a cursor-paginated Snapp response.

    Cursor pagination only exposes a forward ``next`` link, absent (or
    ``null``) once ``has_more`` is ``False``.
    """

    next: str | None


class CursorPagination(TypedDict):
    """Cursor-based pagination block of a Snapp list response."""

    path: str
    per_page: int
    count: int
    links: CursorLinks
    has_more: bool
    next_cursor: str | None


class CursorMeta(TypedDict):
    """The ``meta`` envelope of a cursor-paginated Snapp list response."""

    pagination: CursorPagination
