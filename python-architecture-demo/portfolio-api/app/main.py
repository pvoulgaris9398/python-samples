from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from app.features.health.routes import router as health_router
from app.features.portfolios.routes import router as portfolios_router
from app.features.users.routes import router as users_router
from app.infrastructure.logging import configure_logging

configure_logging()

logger = structlog.get_logger()  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Started")

    yield

    logger.info("Application Stopped")


app = FastAPI(title="Portfolio API", lifespan=lifespan)

app.include_router(health_router)
app.include_router(users_router)
app.include_router(portfolios_router)
