from decimal import Decimal

from sqlalchemy import Date, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class PortfolioModel(Base):
    __tablename__ = "portfolios"
    # Use Mapped[] type hints for strict type safety
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    inception_dt: Mapped[Date] = mapped_column(Date, unique=False, index=True)
    nav: Mapped[Decimal] = mapped_column(Numeric(precision=15, scale=2))


"""
    positions: Mapped[list["PositionModel"]] = relationship(
        back_populates="portfolio",
        cascade="all, delete-orphan",
        lazy="selectin",
    )
"""
