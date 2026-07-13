from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.portfolios.entities.portfolio import Portfolio
from app.features.portfolios.models.portfolio import PortfolioModel
from app.infrastructure.database import get_session


class PortfolioRepository:
    def __init__(self, db: AsyncSession = Depends(get_session)):
        self.db = db

    async def save(self, portfolio: Portfolio) -> None:
        portfolio_model = PortfolioModel(id=portfolio.id, name=portfolio.name)
        self.db.add(portfolio_model)
        await self.db.commit()

    async def get(self, portfolio_id: UUID) -> Portfolio | None:
        model = await self.db.get(PortfolioModel, portfolio_id)
        if model is None:
            return None

        return Portfolio(id=model.id, name=model.name)
