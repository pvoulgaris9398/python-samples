from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class PortfolioResponse(BaseModel):
    name: str
    inception_dt: date | None = None
    nav: Decimal | None = None

    # Pydantic v2 (FastAPI standard since 2023)
    # REQUIRED: Tells Pydantic to read directly from SQLAlchemy models
    model_config = ConfigDict(from_attributes=True)


"""
    Pydantic v1 (Older FastAPI apps):
    class Config:
        orm_mode = True  # Use this if ConfigDict imports fail
"""
