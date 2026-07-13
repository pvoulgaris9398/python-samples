import structlog
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

logger = structlog.get_logger()

engine = create_async_engine(settings.database_url, echo=False)
logger.info("db.engine.created", database_url=settings.database_url, echo=False)
SessionFactory = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""

    pass


async def get_session():
    async with SessionFactory() as session:
        logger.info("db.session.opened")
        try:
            yield session
        except Exception as exc:
            logger.exception("db.session.error", error=str(exc))
            raise
        finally:
            logger.info("db.session.closed")
