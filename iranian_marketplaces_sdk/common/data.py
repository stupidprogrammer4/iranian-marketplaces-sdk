"""The model bases every marketplace's ``data/`` package is built on.

Three bases, because a request and a response want opposite things from a validator:

* :class:`ResponseSchema` **keeps** unknown keys. These APIs add fields without warning, and a
  response model that rejected them would turn every upstream improvement into an outage. Extras
  survive on ``model_extra`` and round-trip through ``model_dump()``.
* :class:`RequestSchema` **rejects** unknown keys, and serialises only the fields you actually set.
  A typo in a payload key is a silent no-op at the marketplace's end — here it is a
  ``ValidationError`` before the request leaves. ``exclude_unset`` is what preserves partial-update
  semantics: ``PUT /variants/{id}`` with ``seller_stock`` alone must send exactly that one key, not
  every other field defaulted to null.
* :class:`QuerySchema` is a request whose fields become query-string parameters, so it also drops
  ``None`` — a query parameter with no value and an absent one mean the same thing to these APIs.

Wire names that are not snake_case (``resetTime``, ``specialPrice``, ``variantId``) are declared
with an alias, so Python code stays snake_case and the bytes on the wire stay exactly what the
marketplace documented. Those fields use ``validation_alias`` **and** ``serialization_alias``
rather than the shorter ``alias``: a plain ``alias`` also renames the parameter in the synthesised
``__init__`` as far as a type checker is concerned, so ``ProductUpdate(special_price=…)`` — which
pydantic accepts at runtime under ``populate_by_name`` — would be flagged as an error in every
editor. The pair keeps the constructor snake_case for the type checker and the wire camelCase for
the marketplace.

Timestamps are typed ``str``, not ``datetime``, throughout. These APIs report at least four
different formats — ``Y-m-d H:i:s``, ISO-8601, the Persian calendar, and Digikala's ``{date,
timezone_type, timezone}`` envelope — and several fields are documented as one and observed as
another. Parsing them here would mean a whole page of products failing to load because one
``market_price_last_update`` came back empty.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, TypeAdapter, ValidationError
from pydantic.alias_generators import to_camel

from iranian_marketplaces_sdk.common.exceptions import ResponseValidationError


class Schema(BaseModel):
    """Common base. Not used directly — pick a request or a response base below."""

    model_config = ConfigDict(
        populate_by_name=True,
        protected_namespaces=(),
    )


class ResponseSchema(Schema):
    """Base for everything the SDK parses *out of* a marketplace response."""

    model_config = ConfigDict(
        populate_by_name=True,
        protected_namespaces=(),
        extra="allow",
    )


class RequestSchema(Schema):
    """Base for everything the SDK sends as a JSON body."""

    model_config = ConfigDict(
        populate_by_name=True,
        protected_namespaces=(),
        extra="forbid",
    )

    def to_payload(self) -> dict[str, Any]:
        """The JSON body for this request: aliased, JSON-safe, and only what was set.

        ``exclude_unset`` is the whole point. A field you never touched is not sent, so a partial
        update stays partial and an optional field you deliberately set to ``None`` is still sent
        as ``null`` — which several endpoints require (Basalam's ``product_filter`` is documented
        as required *and* nullable).
        """
        return self.model_dump(mode="json", by_alias=True, exclude_unset=True)


class QuerySchema(RequestSchema):
    """Base for the filter/pagination models that become query-string parameters."""

    def to_params(self) -> dict[str, Any]:
        """The query parameters for this request: aliased, JSON-safe, no unset and no ``None``.

        List values are left as lists. Each marketplace joins or repeats them in its own
        ``helpers.py``, because they disagree: Digikala wants ``1,2,3`` (and ``1_2_3`` for one
        specific key), Basalam wants the parameter repeated.
        """
        return self.model_dump(mode="json", by_alias=True, exclude_unset=True, exclude_none=True)


class CamelCaseResponseSchema(ResponseSchema):
    """A response whose every wire key is camelCase — Tapsi's whole API, and parts of Digikala's.

    One generator beats an alias on every field: it is shorter, it cannot drift out of sync with a
    field it was meant to rename, and a type checker still sees a snake_case constructor.
    """

    model_config = ConfigDict(alias_generator=to_camel)


class CamelCaseRequestSchema(RequestSchema):
    """A request body whose every wire key is camelCase. See :class:`CamelCaseResponseSchema`."""

    model_config = ConfigDict(alias_generator=to_camel)


class CamelCaseQuerySchema(QuerySchema):
    """A query model whose every wire key is camelCase. See :class:`CamelCaseResponseSchema`."""

    model_config = ConfigDict(alias_generator=to_camel)


class MarketplaceConfig(Schema):
    """Base for the per-marketplace credential records.

    Frozen: an engine's credentials are fixed for its lifetime, and a shared client silently
    re-pointed at another seller mid-run is the kind of bug that is found in the invoice. The one
    exception is Digikala's token refresh, which replaces the whole config object rather than
    mutating it.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        protected_namespaces=(),
        extra="forbid",
        frozen=True,
    )


def parse[T: BaseModel](model: type[T], raw: Any) -> T:
    """Validate a decoded response body into ``model``, or raise :class:`ResponseValidationError`.

    Every engine method funnels its response through here, so schema drift arrives as one
    catchable exception carrying the raw body rather than as a ``pydantic.ValidationError`` from
    the middle of the SDK.
    """
    try:
        return model.model_validate(raw)
    except ValidationError as exc:
        raise ResponseValidationError(
            f"{model.__name__} could not be built from the response body",
            model=model.__name__,
            raw=raw,
            errors=exc.errors(),
        ) from exc


def parse_list[T: BaseModel](model: type[T], raw: Any) -> list[T]:
    """Same as :func:`parse`, for the endpoints that answer with a bare JSON array."""
    adapter: TypeAdapter[list[T]] = TypeAdapter(list[model])  # type: ignore[valid-type]
    try:
        return adapter.validate_python(raw)
    except ValidationError as exc:
        raise ResponseValidationError(
            f"list[{model.__name__}] could not be built from the response body",
            model=f"list[{model.__name__}]",
            raw=raw,
            errors=exc.errors(),
        ) from exc
