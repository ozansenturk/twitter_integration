from unittest.mock import ANY
import http.client
from freezegun import freeze_time
from faker import Faker
from backend import services
import os
import logging

fake = Faker()

logger = logging.getLogger(__name__)

def test_get_bearer_token(client):


    response = services.get_bearer_token(os.environ.get("API_KEY"), os.environ.get("API_SECRET_KEY"))
    logger.debug("response: {}".format(response))

    assert http.client.OK == response.status_code

    expected = {
        'token_type': ANY,
        'access_token': ANY
    }

    assert response.json() == expected


def test_search_tweets(client):

    params = {"q":"python", "result_type":"recent","count":5}

    response = services.search_tweets(params)
    logger.debug("response: {}".format(response))

    assert http.client.OK == response.status_code

    expected = {
        "created_at": ANY,
        "id_str": ANY,
        "text": ANY}


    for key, value in expected.items():
        assert key in response.json()["statuses"][0].keys()
