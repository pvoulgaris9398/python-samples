from uuid import uuid4

from entities.portfolio import Portfolio
from fastapi import Depends
from models.portfolio import PortfolioModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_session


class PortfolioRepository:
    def __init__(self, db: AsyncSession = Depends(get_session)):
        self.db = db

    async def save(self, portfolio: Portfolio):
        model = PortfolioModel(id=portfolio.id, name=portfolio.name)

        self.db.add(model)

        await self.db.commit()

    async def get(self, id: int):
        model = await self.db.get(PortfolioModel, id)

        if model is None:
            return None

        """
        TODO: Update the "id" parameter in the model and database
        to be a UUID or similar
        """
        return Portfolio(id=uuid4(), name=model.name)
