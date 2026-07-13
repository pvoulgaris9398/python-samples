from uuid import uuid4

from ..entities.portfolio import Portfolio
from ..portfolio_repository import PortfolioRepository
from .commands import CreatePortfolioRequest, CreatePortfolioResponse


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
        command: CreatePortfolioRequest,
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
