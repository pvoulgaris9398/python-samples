from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.database import get_session

from . import schemas, services

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/all", response_model=list[schemas.UserResponse], status_code=201)
async def get_user_list():
    return list(services.get_user_list())


@router.post("/", response_model=schemas.UserCreateResponse, status_code=200)
async def create_user(user_data: schemas.UserCreateRequest, db: Session = Depends(get_session)):
    try:
        return services.create_user_login(db, user_data)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
