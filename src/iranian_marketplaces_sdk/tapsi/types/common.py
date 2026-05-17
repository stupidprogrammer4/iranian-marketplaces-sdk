"""Shared TypedDicts reused across the Tapsi type modules.

NOTE: this package must NOT use ``from __future__ import annotations`` —
stringized annotations break ``TypedDict`` ``NotRequired``/``Required``
resolution at runtime. Cross-module references use real imports.
"""

from typing import TypedDict

__all__ = ["ApiMessage"]


class ApiMessage(TypedDict):
    """A single message in the ``messages`` array of a Tapsi response.

    ``type`` is an integer severity/category code (schema not published).
    """

    message: str
    code: str
    type: int
