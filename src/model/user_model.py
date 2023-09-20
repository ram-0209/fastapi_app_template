from datetime import datetime
from typing import Union

from pydantic import BaseModel
from sqlmodel import VARCHAR, Column, Field, SQLModel


class User(SQLModel, table=True):
    """User Model"""

    __tablename__ = "user"
    __table_args__ = {"schema": "test"}
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
    """Token Model"""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token Data Model"""

    username: Union[str, None] = None
