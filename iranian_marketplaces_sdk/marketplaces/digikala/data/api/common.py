"""Bases for the Swagger models; unspecified schemas use pydantic.JsonValue.

Digikala's PHP backend serializes some empty objects as []. Normalize that exact empty
case for documented objects, while continuing to reject non-empty arrays as objects.
"""

from typing import Annotated

from pydantic import BeforeValidator, model_validator

from iranian_marketplaces_sdk.common.data import ResponseSchema


def empty_object(value: object) -> object:
    if value == []:
        return {}
    return value


type ObjectMap[T] = Annotated[dict[str, T], BeforeValidator(empty_object)]


class APIResponseSchema(ResponseSchema):
    """Response models accept upstream additions and normalize PHP's empty object encoding."""

    @model_validator(mode="before")
    @classmethod
    def _empty_object(cls, value: object) -> object:
        return empty_object(value)
