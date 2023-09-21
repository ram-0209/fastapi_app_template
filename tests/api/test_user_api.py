from fastapi.testclient import TestClient

from tests.factories import user_factories
from tests.fixtures.setup_fixtures import client_fixture, session_fixture


def test_create_user(client: TestClient):
    """Test function for Create user

    Args:
        client (TestClient): _description_
    """
    response = client.post(
        "/api/create_user",
        json=user_factories.test_user,
    )
    assert response.status_code == 200


def test_get_user(client: TestClient):
    """Test Function for Get user by username

    Args:
        client (TestClient): _description_
    """
    response = client.get(f"/api/user?username={user_factories.username}")
    assert response.status_code == 200
