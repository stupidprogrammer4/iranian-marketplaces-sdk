"""Shared TypedDicts reused across the Basalam type modules.

NOTE: this package must NOT use ``from __future__ import annotations`` —
stringized annotations break ``TypedDict`` ``NotRequired``/``Required``
resolution at runtime. Cross-module references use real imports.
"""

from typing import TypedDict

__all__ = ["RangeInput"]


class RangeInput(TypedDict, total=False):
    """A numeric ``start``/``end`` range filter (both bounds optional)."""

    start: int | None
    end: int | None
