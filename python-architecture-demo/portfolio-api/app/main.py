import time
from contextlib import asynccontextmanager
from typing import Awaitable, Callable
from uuid import uuid4

import structlog
from fastapi import FastAPI, Request, Response

from app.features.health.routes import router as health_router
from app.features.portfolios.routes import router as portfolios_router
from app.features.users.routes import router as users_router
from app.infrastructure.database import engine
from app.infrastructure.logging import configure_logging

# TODO: Fix invalid or bad imports in the tracing module
from app.infrastructure.tracing import configure_tracing, get_trace_ids

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
async def log_http_requests(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    request_id = str(uuid4())
    trace_id, span_id = get_trace_ids()
    request_logger = logger.bind(
        request_id=request_id,
        trace_id=trace_id,
        span_id=span_id,
    )
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
    if trace_id is not None:
        response.headers["X-Trace-ID"] = trace_id
    if span_id is not None:
        response.headers["X-Span-ID"] = span_id

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
