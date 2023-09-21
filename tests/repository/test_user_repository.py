from src.repository.user_repository import create_new_user_db, get_user_by_username_db
from tests.factories.user_factories import test_user_model, username
from tests.fixtures.data_fixtures import data_setup
from tests.fixtures.setup_fixtures import session_fixture


def test_create_new_user_db(session: session_fixture):
    # Create a mock user object
    mock_user = test_user_model

    # Call the function with the mock user and session
    result = create_new_user_db(mock_user, session)

    # Assertions
    assert result.username == username


def test_get_user_by_username_db(data_setup: data_setup, session: session_fixture):
    # Call the function with a mock username and session
    # mock_user = test_user_model
    # create_new_user_db(mock_user, session)
    result = get_user_by_username_db(username, session)
    assert result[0].username == username
