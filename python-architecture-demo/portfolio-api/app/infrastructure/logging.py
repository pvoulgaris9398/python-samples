import logging

import structlog


def configure_logging() -> None:
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )

    logging.basicConfig(level=logging.INFO, format="%(message)s")
