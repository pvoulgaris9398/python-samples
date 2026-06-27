class SqlPortfolioRepository:
    def __init__(self, session):
        self.session = session

    async def save(self, portfolio):
        model = PortfolioModel(id=portfolio.id, name=portfolio.name)

        self.session.add(model)

        await self.session.commit()

    async def get(self, id):
        model = await self.session.get(PortfolioModel, id)

        if model is None:
            return None

        return Portfolio(id=model.id, name=model.name)
