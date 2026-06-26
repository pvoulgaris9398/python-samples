from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import text

from app.infrastructure.database import engine

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    database: bool


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    async with engine.connect() as conn:
        result = await conn.execute(text("select 1"))

        value = result.scalar()

    return HealthResponse(status="healthy", database=value == 1)
