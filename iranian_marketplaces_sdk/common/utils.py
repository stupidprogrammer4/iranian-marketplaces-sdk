"""The checks and coercions every marketplace needs, written once so they cannot drift apart."""

from collections.abc import Mapping, Sequence
from typing import Any, cast

from iranian_marketplaces_sdk.common.exceptions import ConfigurationError


def require_text(value: str | None, *, field: str, marketplace: str) -> str:
    """A credential that must be present and non-blank, or a :class:`ConfigurationError`.

    Fails at construction rather than at the first call, so a missing token shows up while you are
    wiring the client up instead of halfway through a batch of price updates.
    """
    text = str(value or "").strip()
    if not text:
        raise ConfigurationError(f"the {marketplace} client requires {field}")
    return text


def join_values(value: Any, separator: str = ",") -> Any:
    """Concatenate a list/tuple filter value; leave a scalar alone.

    Several of these APIs document a multi-value filter as one query parameter holding a separated
    list rather than a repeated parameter. Callers always pass a Python list; this is where it
    becomes the string the API asked for.
    """
    if isinstance(value, (list, tuple)):
        # `value` is Any, so its elements have no type a checker can see. They are stringified
        # either way; the cast just says so.
        items = cast("Sequence[object]", value)
        return separator.join(str(item) for item in items)
    return value


def drop_none(mapping: Mapping[str, Any] | None) -> dict[str, Any]:
    """Copy a mapping without its ``None`` values.

    For a query string, an absent parameter and one with an empty value mean the same thing to
    these APIs, and sending ``None`` would serialise as the literal string ``"None"``.
    """
    if not mapping:
        return {}
    return {key: value for key, value in mapping.items() if value is not None}


def bracket_params(prefix: str, params: Mapping[str, Any] | None) -> dict[str, Any]:
    """Rewrite ``{"active": True}`` as ``{"search[active]": True}``.

    Digikala's list endpoints take their filters in PHP's bracket form. The models keep plain
    field names; the bracket only exists on the wire.
    """
    if not params:
        return {}
    return {f"{prefix}[{key}]": value for key, value in params.items()}


def rename_keys(params: Mapping[str, Any] | None, key_map: Mapping[str, str]) -> dict[str, Any]:
    """Map pythonic parameter names onto the marketplace's own.

    For the query keys that are not valid Python identifiers at all — Basalam's ``stock[gte]`` and
    ``items.order_ids`` — an alias on the model is not enough, because the name has to survive as
    a dict key rather than as an attribute.
    """
    if not params:
        return {}
    return {key_map.get(key, key): value for key, value in params.items()}
