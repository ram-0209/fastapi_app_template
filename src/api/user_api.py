from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.database import get_session
from src.dto.user_dto import UserModel
from src.service.user_service import create_new_user, fetch_user_by_username

router = APIRouter()


@router.post("/create_user")
async def create_user(user: UserModel, session: Session = Depends(get_session)):
    """_summary_

    Args:
        user (UserModel): _description_
        session (Session, optional): _description_. Defaults to Depends(get_session).

    Returns:
        _type_: _description_
    """
    return create_new_user(user, session)


@router.get("/user")
async def get_user(username: str, session: Session = Depends(get_session)):
    """_summary_

    Args:
        username (str): _description_
        session (Session, optional): _description_. Defaults to Depends(get_session).

    Returns:
        _type_: _description_
    """
    return fetch_user_by_username(username, session)
