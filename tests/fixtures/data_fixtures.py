"""Creation of a data for test database"""

import pytest

from src.model.user_model import User
from tests.factories.user_factories import test_user_model
from tests.fixtures.setup_fixtures import client_fixture, session_fixture


@pytest.fixture
def data_setup(session: session_fixture):
    session.add(User(**test_user_model.dict()))
