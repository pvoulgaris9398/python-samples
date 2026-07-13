from datetime import date
from decimal import Decimal

from .models.portfolio import PortfolioModel


def get_portfolio_list():
    yield PortfolioModel(name="AAA", inception_dt=date(2026, 2, 13), nav=Decimal("102300"))
    yield PortfolioModel(name="BBB ex-US", inception_dt=date(2024, 4, 7), nav=Decimal("20200000"))
    yield PortfolioModel(name="CCC ex-EMEA", inception_dt=date(2023, 8, 27), nav=Decimal("330000"))
    yield PortfolioModel(
        name="DDD Large-Cap", inception_dt=date(2026, 11, 4), nav=Decimal("4400000")
    )
    yield PortfolioModel(
        name="EEE Small-Cap", inception_dt=date(2025, 6, 19), nav=Decimal("450300776")
    )
