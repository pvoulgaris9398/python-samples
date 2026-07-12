from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.database import get_session

from . import schemas, service

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/all", response_model=list[schemas.UserResponse], status_code=201)
async def get_user_list():
    return list(service.get_user_list())


@router.post("/", response_model=schemas.UserCreateResponse, status_code=201)
async def create_user(user_data: schemas.UserCreateRequest, db: Session = Depends(get_session)):
    # Route only handles HTTP layer, calls service for
    # heavy lifting
    try:
        return service.create_user_login(db, user_data)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))
