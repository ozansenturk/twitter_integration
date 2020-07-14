import pytest
import http.client
from rest import create_app
from faker import Faker
fake = Faker()


@pytest.fixture
def app():
    application = create_app("testing")

    application.app_context().push()

    return application
