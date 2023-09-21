"""This file include model factory data for all user tests api """
from src.dto.user_dto import UserModel

username = "pytestuser1"
test_user = {
    "last_name": "user1",
    "is_superuser": False,
    "is_staff": False,
    "date_joined": "",
    "first_name": "pytest1",
    "password": "pytest@123",
    "email": "pytestuser1@xyz.com",
    "last_login": False,
    "username": username,
    "is_active": False,
}

test_user_model = UserModel(
    last_name="user1",
    is_superuser=False,
    is_staff=False,
    date_joined="",
    first_name="pytest1",
    password="pytest@123",
    email="pytestuser1@xyz.com",
    last_login=False,
    username=username,
    is_active=False,
)
