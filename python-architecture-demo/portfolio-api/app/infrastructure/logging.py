import logging

import structlog

from app.config import settings


def configure_logging() -> None:
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )

    logging.basicConfig(level=settings.log_level.upper(), format="%(message)s")
