from fastapi import APIRouter

from . import schemas, services

router = APIRouter(prefix="/portfolios", tags=["Portfolios"])


@router.get("/all", response_model=list[schemas.PortfolioResponse], status_code=200)
async def get_portfolio_list():
    return list(services.get_portfolio_list())


"""
from uuid import UUID

import structlog
from fastapi import APIRouter, Depends, HTTPException, status

import app.features.portfolios.create.command
import app.features.portfolios.get.handler
import app.features.portfolios.get.query
from app.features.portfolio.exceptions import (
    PortfolioAlreadyExistsError,
)
from app.features.portfolios.create.handler import (
    CreatePortfolioHandler,
)

logger = structlog.get_logger()

router = APIRouter(
    prefix="/portfolios",
    tags=["Portfolios"],
)


# ----------------------------------------------------------------------
# Dependency Injection
# ----------------------------------------------------------------------


def get_create_handler() -> CreatePortfolioHandler:
    raise NotImplementedError()


def get_get_handler() -> app.application.portfolios.get.handler.GetPortfolioHandler:  # type: ignore
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
    command: app.application.portfolios.create.command.CreatePortfolioCommand,
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
    handler: app.application.portfolios.get.handler.GetPortfolioHandler = Depends(get_get_handler),  # type: ignore
):
    query = app.application.portfolios.get.query.GetPortfolioQuery(  # type: ignore
        id=portfolio_id,
    )

    portfolio = await handler.handle(query)  # type: ignore

    if portfolio is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found.",
        )

    return portfolio  # type: ignore
"""
