"""User SQL Models"""
from datetime import datetime
from typing import Union

from pydantic import BaseModel
from sqlmodel import VARCHAR, Column, Field, SQLModel

from src.config.app_config import SCHEMA


class User(SQLModel, table=True):
    """SQL Model for User table

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """

    __tablename__ = f"{SCHEMA}.user"
    id: int = Field(default=None, primary_key=True)
    password: str = Field(sa_column=Column(VARCHAR(54), nullable=False))
    last_login: datetime = Field(default=None)
    is_superuser: bool = Field(default=False)
    username: str = Field(default=None, unique=True)
    first_name: str = Field(sa_column=Column(VARCHAR(54), nullable=False))
    last_name: str = Field(sa_column=Column(VARCHAR(54), nullable=False))
    email: str = Field(sa_column=Column(VARCHAR(54), nullable=False))
    is_staff: bool = Field(default=False)
    is_active: bool = Field(default=True)
    date_joined: str = Field(default=datetime.now())


class Token(BaseModel):
    """Model for Token

    Args:
        BaseModel (_type_): _description_
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Model for Token Data

    Args:
        BaseModel (_type_): _description_
    """

    username: Union[str, None] = None
