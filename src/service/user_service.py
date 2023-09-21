"""Service Layer for User APIs"""
from fastapi import Depends
from sqlmodel import Session

from src.database import get_session
from src.dto.user_dto import UserModel
from src.repository.user_repository import create_new_user_db, get_user_by_username_db


def create_new_user(user: UserModel, session: Session = Depends(get_session)):
    """Create a new user

    Args:
        user (UserModel): user details
        session (Session): Database session connection

    Returns: create_new_user_db
        _type_: function
    """
    return create_new_user_db(user, session)


def fetch_user_by_username(username: str, session: Session = Depends(get_session)):
    """_summary_

    Args:
        username (str): Name of the user
        session (Session): Database session connection

    Returns: get_user_by_username_db
        _type_: function
    """
    return get_user_by_username_db(username, session)
