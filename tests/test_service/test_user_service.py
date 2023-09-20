from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.database import Session, engine
from src.dto.user_dto import UserModel
from src.main import app
from src.service.user_service import create_new_user, fetch_user_by_username

client = TestClient(app)


@pytest.fixture
def mock_db_session():
    # Create a mock database session
    mock_session = Mock(spec=Session)
    return mock_session


def test_fetch_user_by_username(mock_db_session):
    # Connect to database to get values
    mock_db_session.return_value = Session(engine)

    # Creating a mock_username
    mock_username = "test_user10"

    # Call the function with a mock username and session
    result = fetch_user_by_username(mock_username, mock_db_session.return_value)
    assert result[0].username == "test_user10"


def test_create_new_user(mock_db_session):
    # Create a mock user object
    mock_user = UserModel(
        last_name="user",
        is_superuser=False,
        is_staff=False,
        date_joined="",
        email="testuser@xyz.com",
        first_name="pytest",
        password="test@123",
        last_login="1970-01-01T00:00:00",
        username="pytest_user",
        is_active=False,
    )

    # Call the function with the mock user and session
    result = create_new_user(mock_user, mock_db_session)

    # Assertions
    assert result.username == "pytest_user"
