from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_session

from . import schemas, service

router = APIRouter()


@router.get("/health", response_model=schemas.HealthResponse)
async def health(db: AsyncSession = Depends(get_session)) -> schemas.HealthResponse:
    value = await service.get_database_health(db=db)
    return schemas.HealthResponse(status="healthy", database=value == 1)
