"""Public TypedDict surface for the Tapsi API.

Split by scope for maintainability while presenting a single flat namespace
(``from ...tapsi.types import X``). As endpoints are implemented, add a
submodule per scope (e.g. ``common.py`` for shared bases, then one module
per resource group), give each its own ``__all__``, and re-export it here.

NOTE: submodules must NOT use ``from __future__ import annotations``.
Stringized annotations stop ``TypedDict`` from resolving
``NotRequired``/``Required`` at runtime. Use real cross-module imports
instead of forward references.
"""

__all__: list[str] = []
