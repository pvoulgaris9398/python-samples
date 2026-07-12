from fastapi import APIRouter

from . import schemas, service

router = APIRouter(prefix="/portfolios", tags=["Portfolios"])


@router.get("/all", response_model=list[schemas.PortfolioResponse], status_code=201)
async def get_portfolio_list():
    return list(service.get_portfolio_list())
