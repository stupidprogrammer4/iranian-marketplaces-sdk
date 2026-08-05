"""Shared models reused across the Digikala data modules.

Every list endpoint in the Seller Open API answers with the same envelope — ``{status, data}``
where ``data`` carries ``sort_data``, ``pager``, ``form_data``, ``items`` and ``meta_data`` — so
the paging half of it is defined once here and the resource modules only declare their ``items``.
"""

from iranian_marketplaces_sdk.common.data import CamelCaseResponseSchema, ResponseSchema

__all__ = [
    "DigikalaDateTime",
    "KeyTitle",
    "Pager",
    "RateLimit",
    "RateLimitResetTime",
    "SortData",
]


class RateLimitResetTime(ResponseSchema):
    """The ``resetTime`` block inside the health-check rate limit."""

    date: str
    timezone_type: int
    timezone: str


class RateLimit(CamelCaseResponseSchema):
    """Current rate-limit window, as reported by the health check and some list endpoints."""

    max: int
    current: int
    reset_time: RateLimitResetTime


class SortData(ResponseSchema):
    """Sorting metadata returned by paginated list endpoints.

    ``sort_columns`` is the authoritative list of what may be passed as ``sort`` to that endpoint.
    """

    sort_column: str
    sort_order: str
    sort_columns: list[str]


class Pager(ResponseSchema):
    """Pagination metadata returned by paginated list endpoints."""

    page: int
    item_per_page: int
    total_pages: int
    total_rows: int


class DigikalaDateTime(ResponseSchema):
    """Digikala's standard datetime envelope (date plus timezone metadata).

    ``date`` is left as the string Digikala sent — see the note in
    :mod:`iranian_marketplaces_sdk.common.data` on why timestamps are not parsed here.
    """

    date: str
    timezone_type: int
    timezone: str


class KeyTitle(ResponseSchema):
    """A generic ``{key, title}`` pair: statuses, types, payment methods, and the rest.

    ``key`` is the stable machine value to branch on; ``title`` is Persian display text that
    changes without notice.
    """

    key: str
    title: str
