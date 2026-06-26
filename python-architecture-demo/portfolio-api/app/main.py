from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from app.api.health import router as health_router
from app.infrastructure.logging import configure_logging

configure_logging()

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Started")

    yield

    logger.info("Application Stopped")


app = FastAPI(title="Portfolio API", lifespan=lifespan)

app.include_router(health_router)
