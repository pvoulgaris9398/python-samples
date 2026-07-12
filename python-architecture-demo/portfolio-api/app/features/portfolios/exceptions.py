"""
Domain exceptions for the Portfolio bounded context.

These exceptions represent business rule violations.
They should never depend on FastAPI, SQLAlchemy, or PostgreSQL.
"""


class PortfolioError(Exception):
    """Base class for all portfolio domain exceptions."""


class DuplicatePositionError(PortfolioError):
    """Raised when attempting to add the same security twice."""


class PositionNotFoundError(PortfolioError):
    """Raised when a requested position does not exist."""


class InvalidPortfolioNameError(PortfolioError):
    """Raised when the portfolio name violates business rules."""


class EmptyPortfolioError(PortfolioError):
    """Raised when an operation requires at least one position."""


class PortfolioAlreadyExistsError(PortfolioError):
    """Raised when attempting to create a portfolio with a duplicate identity."""
