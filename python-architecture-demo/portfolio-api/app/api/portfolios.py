from uuid import UUID

import structlog
from fastapi import APIRouter, Depends, HTTPException, status

from app.application.portfolios.create.command import (
    CreatePortfolioCommand,
)
from app.application.portfolios.create.handler import (
    CreatePortfolioHandler,
)
from app.application.portfolios.get.handler import (
    GetPortfolioHandler,
)
from app.application.portfolios.get.query import (
    GetPortfolioQuery,
)
from app.domain.portfolio.exceptions import (
    PortfolioAlreadyExistsError,
)

logger = structlog.get_logger()  # type: ignore

router = APIRouter(
    prefix="/portfolios",
    tags=["Portfolios"],
)


# ----------------------------------------------------------------------
# Dependency Injection
# ----------------------------------------------------------------------


def get_create_handler() -> CreatePortfolioHandler:
    """
    Temporary implementation.

    Later we'll inject a repository and UnitOfWork here.
    """
    raise NotImplementedError()


def get_get_handler() -> GetPortfolioHandler:  # type: ignore
    """
    Temporary implementation.

    Later we'll inject a repository and UnitOfWork here.
    """
    logger.info("Application Started")
    raise NotImplementedError()


# ----------------------------------------------------------------------
# POST /portfolios
# ----------------------------------------------------------------------


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def create_portfolio(
    command: CreatePortfolioCommand,
    handler: CreatePortfolioHandler = Depends(get_create_handler),
):
    try:
        portfolio = await handler.handle(command)

        return portfolio

    except PortfolioAlreadyExistsError as ex:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(ex),
        )


# ----------------------------------------------------------------------
# GET /portfolios/{id}
# ----------------------------------------------------------------------


@router.get("/{portfolio_id}")
async def get_portfolio(  # type: ignore
    portfolio_id: UUID,
    handler: GetPortfolioHandler = Depends(get_get_handler),  # type: ignore
):
    query = GetPortfolioQuery(  # type: ignore
        id=portfolio_id,
    )

    portfolio = await handler.handle(query)  # type: ignore

    if portfolio is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found.",
        )

    return portfolio  # type: ignore
