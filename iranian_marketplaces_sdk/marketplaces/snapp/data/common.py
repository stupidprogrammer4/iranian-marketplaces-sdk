"""Snapp Shop — shared models reused across the data modules.

Snapp paginates two different ways and it matters which: products come back offset-paginated with
a total and a page count, orders cursor-paginated with neither. An order list cannot tell you how
many orders there are — you follow ``next_cursor`` until ``has_more`` is false.
"""

from iranian_marketplaces_sdk.common.data import ResponseSchema

__all__ = [
    "CursorLinks",
    "CursorMeta",
    "CursorPagination",
    "Meta",
    "Pagination",
    "PaginationLinks",
]


class PaginationLinks(ResponseSchema):
    """Next/previous page URLs of an offset-paginated Snapp response."""

    next: str | None = None
    previous: str | None = None


class Pagination(ResponseSchema):
    """Offset-based pagination block of a Snapp list response."""

    total: int
    count: int
    per_page: int
    current_page: int
    total_pages: int
    links: PaginationLinks


class Meta(ResponseSchema):
    """The ``meta`` envelope of an offset-paginated Snapp list response."""

    pagination: Pagination


class CursorLinks(ResponseSchema):
    """Links block of a cursor-paginated Snapp response.

    Forward only: there is no ``previous``, and ``next`` is ``null`` once ``has_more`` is false.
    """

    next: str | None = None


class CursorPagination(ResponseSchema):
    """Cursor-based pagination block of a Snapp list response.

    Pass ``next_cursor`` back as the ``cursor`` filter to get the following page.
    """

    path: str
    per_page: int
    count: int
    links: CursorLinks
    has_more: bool
    next_cursor: str | None = None


class CursorMeta(ResponseSchema):
    """The ``meta`` envelope of a cursor-paginated Snapp list response."""

    pagination: CursorPagination
