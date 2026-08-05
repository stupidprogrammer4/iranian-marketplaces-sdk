"""The two engine interfaces.

Unlike a payment gateway, two marketplaces share almost no endpoints — Digikala has invoices and
smart discounts, Tapsi has neither, and none of them agree on what a "product" is. So what these
protocols capture is the part that *is* uniform: how a client is named, addressed, and disposed of.
Everything past that is the marketplace's own surface, discovered through its typed engine class.

These are :class:`typing.Protocol`, so the engines satisfy them structurally. No engine inherits
from anything here, and neither does yours.
"""

from types import TracebackType
from typing import Protocol, Self, runtime_checkable


@runtime_checkable
class ISyncMarketplaceClient(Protocol):
    """The sync engine: for scripts, Django, and Celery workers."""

    name: str

    @property
    def base_url(self) -> str: ...

    def close(self) -> None: ...

    def __enter__(self) -> Self: ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...


@runtime_checkable
class IAsyncMarketplaceClient(Protocol):
    """The async engine: for FastAPI, aiohttp, and anything else on asyncio."""

    name: str

    @property
    def base_url(self) -> str: ...

    async def aclose(self) -> None: ...

    async def __aenter__(self) -> Self: ...

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
