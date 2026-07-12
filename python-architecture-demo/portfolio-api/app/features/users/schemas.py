from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    username: str
    email: EmailStr


class UserCreateRequest(BaseModel):
    username: str
    email: EmailStr


class UserCreateResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
