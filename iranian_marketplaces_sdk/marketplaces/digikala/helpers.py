"""Digikala — headers and query building.

Everything here is a pure function over the models in ``data/``, which is what lets the sync and
async engines share every decision and differ only in how the HTTP call is made. If the two engines
ever disagree about what Digikala was asked, the bug is in this file, not in one of them.
"""

from typing import Any

from iranian_marketplaces_sdk.common.constants import JSON_CONTENT_TYPE
from iranian_marketplaces_sdk.common.utils import bracket_params, join_values
from iranian_marketplaces_sdk.marketplaces.digikala.constants import (
    SEARCH_PARAM_PREFIX,
    UNDERSCORE_JOINED_KEYS,
)
from iranian_marketplaces_sdk.marketplaces.digikala.data import DigikalaConfig

JSON_HEADERS = {"Content-Type": JSON_CONTENT_TYPE}
"""Digikala's gateway wants this on GET requests too, not only on the ones carrying a body."""


def auth_headers(config: DigikalaConfig) -> dict[str, str]:
    """The session headers for an authenticated client."""
    return {"Authorization": f"Bearer {config.access_token}"}


def format_filter_value(key: str, value: Any) -> Any:
    """Concatenate a multi-value filter the way Digikala expects it.

    Almost every list filter is comma-joined. ``search[ids]`` is the documented exception and is
    underscore-joined; getting it wrong returns an empty page rather than an error, which is why
    the exception is named in :data:`~...constants.UNDERSCORE_JOINED_KEYS` rather than guessed at
    the call site.
    """
    separator = "_" if key in UNDERSCORE_JOINED_KEYS else ","
    return join_values(value, separator)


def _paging(
    page: int | None, size: int | None, sort: str | None, order: str | None
) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if size is not None:
        params["size"] = size
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return params


def list_params(
    *,
    page: int | None = None,
    size: int | None = None,
    sort: str | None = None,
    order: str | None = None,
    search: Any = None,
) -> dict[str, Any]:
    """Flatten paging plus a ``search`` model into Digikala's query parameters.

    ``search`` is any :class:`~iranian_marketplaces_sdk.common.data.QuerySchema`; its fields become
    ``search[field]`` and its lists are joined by :func:`format_filter_value`. Fields the caller
    never set are not sent at all.
    """
    params = _paging(page, size, sort, order)
    if search is not None:
        raw = {key: format_filter_value(key, value) for key, value in search.to_params().items()}
        params.update(bracket_params(SEARCH_PARAM_PREFIX, raw))
    return params


def flat_list_params(
    *,
    page: int | None = None,
    size: int | None = None,
    sort: str | None = None,
    order: str | None = None,
    filters: Any = None,
) -> dict[str, Any]:
    """Like :func:`list_params`, but the filters are top-level query keys.

    ``GET /orders/history`` is the one list endpoint that does not use the ``search[...]`` form.
    """
    params = _paging(page, size, sort, order)
    if filters is not None:
        for key, value in filters.to_params().items():
            params[key] = format_filter_value(key, value)
    return params
