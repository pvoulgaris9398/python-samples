import time
from contextlib import asynccontextmanager
from uuid import uuid4

import structlog
from fastapi import FastAPI, Request

from app.features.health.routes import router as health_router
from app.features.portfolios.routes import router as portfolios_router
from app.features.users.routes import router as users_router
from app.infrastructure.database import engine
from app.infrastructure.logging import configure_logging
from app.infrastructure.tracing import configure_tracing

configure_logging()

logger = structlog.get_logger()  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Started")

    yield

    logger.info("Application Stopped")


app = FastAPI(title="Portfolio API", lifespan=lifespan)

configure_tracing(app, engine)


@app.middleware("http")
async def log_http_requests(request: Request, call_next):
    request_id = str(uuid4())
    request_logger = logger.bind(request_id=request_id)
    request_logger.info("http.request.start", method=request.method, path=request.url.path)

    start = time.monotonic()
    try:
        response = await call_next(request)
    except Exception as exc:
        elapsed_ms = round((time.monotonic() - start) * 1000, 2)
        request_logger.exception(
            "http.request.error",
            method=request.method,
            path=request.url.path,
            elapsed_ms=elapsed_ms,
            error=str(exc),
        )
        raise

    elapsed_ms = round((time.monotonic() - start) * 1000, 2)
    response.headers["X-Request-ID"] = request_id
    request_logger.info(
        "http.request.complete",
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        elapsed_ms=elapsed_ms,
    )
    return response


app.include_router(health_router)
app.include_router(users_router)
app.include_router(portfolios_router)
