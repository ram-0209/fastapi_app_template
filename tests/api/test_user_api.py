from fastapi.testclient import TestClient

from src.database import Session, engine, get_session
from src.main import app

client = TestClient(app)


def override_get_session():
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


def test_create_user():
    response = client.post(
        "/api/create_user",
        json={
            "last_name": "user22",
            "is_superuser": False,
            "is_staff": False,
            "date_joined": "",
            "first_name": "test",
            "password": "test@123",
            "email": "testuser@xyz.com",
            "last_login": False,
            "username": "test_user22",
            "is_active": False,
        },
    )
    assert response.status_code == 200


def test_get_user():
    username = "test_user10"
    response = client.get(f"/api/user?username={username}")
    assert response.status_code == 200
