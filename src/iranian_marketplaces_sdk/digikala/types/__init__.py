"""Public TypedDict surface for the Digikala Seller Open API.

This package is split by scope for maintainability, but presents a single
flat namespace: ``from ...digikala.types import Variant`` works exactly as
before the split. Each submodule defines its own ``__all__``.
"""

from .auth import *  # noqa: F401,F403
from .auth import __all__ as _auth_all
from .common import *  # noqa: F401,F403
from .common import __all__ as _common_all
from .health import *  # noqa: F401,F403
from .health import __all__ as _health_all
from .inventories import *  # noqa: F401,F403
from .inventories import __all__ as _inventories_all
from .invoices import *  # noqa: F401,F403
from .invoices import __all__ as _invoices_all
from .orders import *  # noqa: F401,F403
from .orders import __all__ as _orders_all
from .packages import *  # noqa: F401,F403
from .packages import __all__ as _packages_all
from .pricing import *  # noqa: F401,F403
from .pricing import __all__ as _pricing_all
from .variants import *  # noqa: F401,F403
from .variants import __all__ as _variants_all

__all__ = [
    *_common_all,
    *_health_all,
    *_auth_all,
    *_variants_all,
    *_orders_all,
    *_inventories_all,
    *_invoices_all,
    *_packages_all,
    *_pricing_all,
]
