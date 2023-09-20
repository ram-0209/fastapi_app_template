from sqlmodel import select

from src.dto.user_dto import UserModel
from src.model.user_model import User


def create_new_user_db(user: UserModel, session):
    create_user = User(**user.dict())
    session.add(create_user)
    session.commit()
    session.refresh(create_user)
    return create_user


def get_user_by_username_db(username, session):
    """gets the user name by its name"""
    statement = select(User).where(User.username == username)
    result = session.exec(statement)
    user = result.all()
    return user
