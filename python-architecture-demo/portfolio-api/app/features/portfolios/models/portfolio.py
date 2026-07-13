from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import Date, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base


class PortfolioModel(Base):
    __tablename__ = "portfolios"
    # Use Mapped[] type hints for strict type safety
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4,
    )
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
