from uuid import uuid4

from app.application.portfolios.create.command import (
    CreatePortfolioCommand,
)
from app.application.portfolios.create.response import (
    CreatePortfolioResponse,
)
from app.domain.portfolio.entity import Portfolio
from app.domain.portfolio.repository import PortfolioRepository


class CreatePortfolioHandler:
    """
    Application use case for creating a portfolio.
    """

    def __init__(
        self,
        repository: PortfolioRepository,
    ):
        self._repository = repository

    async def handle(
        self,
        command: CreatePortfolioCommand,
    ) -> CreatePortfolioResponse:
        portfolio = Portfolio(
            id=uuid4(),
            name=command.name,
        )

        await self._repository.save(portfolio)

        return CreatePortfolioResponse(
            id=portfolio.id,
            name=portfolio.name,
        )
