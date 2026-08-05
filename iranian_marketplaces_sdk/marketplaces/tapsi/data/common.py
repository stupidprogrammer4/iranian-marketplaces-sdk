"""Tapsi Shop — shared models reused across the data modules."""

from iranian_marketplaces_sdk.common.data import ResponseSchema

__all__ = ["ApiMessage"]


class ApiMessage(ResponseSchema):
    """A single entry of the ``messages`` array every Tapsi response carries.

    Present on successes as well as failures — ``success`` is what says whether the call worked,
    and ``messages`` says what the API wants you to know either way. ``type`` is an integer
    severity/category code whose schema is not published.
    """

    message: str
    code: str
    type: int
