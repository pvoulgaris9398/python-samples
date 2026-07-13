from sqlalchemy.orm import Session

from .models import UserModel
from .schemas import UserCreateRequest


def get_user_list():
    yield UserModel(username="joe", email="joe.momma@dude.com")
    yield UserModel(username="ralphi", email="ralphi.thompson@aol.com")
    yield UserModel(username="sookie", email="sookie.stackhouse@ms.com")


def create_user_login(db: Session, user_data: UserCreateRequest) -> UserModel:
    # Handle slice-specific business rules, hashes, validation, etc.
    user = UserModel(username=user_data.username, email=user_data.email)
    # db.add(user)
    # db.commit()
    # db.refresh(user)
    return user
