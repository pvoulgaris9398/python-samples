from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.features.health import schemas, services
from app.infrastructure.database import get_session
from app.infrastructure.runtime import get_uptime_seconds
from app.infrastructure.tracing import get_trace_ids

router = APIRouter()


def _build_status_response(value: bool) -> schemas.HealthResponse:
    trace_id, span_id = get_trace_ids()
    return schemas.HealthResponse(
        status="healthy",
        database=value,
        metrics=schemas.HealthMetrics(
            uptime_seconds=get_uptime_seconds(),
            database_query_success=value,
        ),
        trace=schemas.HealthTrace(
            trace_id=trace_id,
            span_id=span_id,
            otel_enabled=settings.otel_enabled,
        ),
        logs=schemas.HealthLogs(
            configured=True,
            log_level=settings.log_level,
        ),
    )


@router.get("/health", response_model=schemas.HealthResponse)
async def health(db: AsyncSession = Depends(get_session)) -> schemas.HealthResponse:
    value = await services.get_database_health(db=db)
    return _build_status_response(value == 1)


@router.get("/metrics", response_model=schemas.HealthResponse)
async def metrics(db: AsyncSession = Depends(get_session)) -> schemas.HealthResponse:
    value = await services.get_database_health(db=db)
    return _build_status_response(value == 1)
