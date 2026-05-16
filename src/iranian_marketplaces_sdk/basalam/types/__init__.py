"""Public TypedDict surface for the Basalam API.

Split by scope for maintainability while presenting a single flat namespace
(``from ...basalam.types import X``). As endpoints are implemented, add a
submodule per scope (e.g. ``common.py`` for shared bases, then one module
per resource group), give each its own ``__all__``, and re-export it here.

NOTE: submodules must NOT use ``from __future__ import annotations``.
Stringized annotations stop ``TypedDict`` from resolving
``NotRequired``/``Required`` at runtime. Use real cross-module imports
instead of forward references.
"""

from .common import *  # noqa: F401,F403
from .common import __all__ as _common_all
from .discounts import *  # noqa: F401,F403
from .discounts import __all__ as _discounts_all
from .parcels import *  # noqa: F401,F403
from .parcels import __all__ as _parcels_all
from .products import *  # noqa: F401,F403
from .products import __all__ as _products_all

__all__ = [
    *_common_all,
    *_products_all,
    *_discounts_all,
    *_parcels_all,
]
