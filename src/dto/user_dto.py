"""
    Common Schema for mapping user
"""
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class UserModel(SQLModel):
    """
    Class for constructing Response schema
    """

    username: str
    password: str
    last_login: Optional[datetime]
    is_superuser: Optional[bool]
    first_name: str
    last_name: str
    email: str
    is_staff: Optional[bool]
    is_active: Optional[bool]
    date_joined: Optional[str]
