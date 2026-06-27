from typing import Protocol
from uuid import UUID

from .entity import Portfolio


class PortfolioRepository(Protocol):
    async def save(self, portfolio: Portfolio) -> None: ...

    async def get(self, id: UUID) -> Portfolio | None: ...
