"""User Database functions"""
from sqlmodel import select

from src.dto.user_dto import UserModel
from src.model.user_model import User


def create_new_user_db(user: UserModel, session):
    """Add user to the database

    Args:
        user (UserModel): _description_
        session (_type_): _description_

    Returns:
        _type_: _description_
    """
    create_user = User(**user.dict())
    session.add(create_user)
    session.commit()
    session.refresh(create_user)
    return create_user


def get_user_by_username_db(username, session):
    """Get User by name from database

    Args:
        username (_type_): _description_
        session (_type_): _description_

    Returns:
        _type_: _description_
    """
    statement = select(User).where(User.username == username)
    result = session.exec(statement)
    user = result.all()
    return user
