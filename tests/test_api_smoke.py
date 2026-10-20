
import pytest
from fastapi.testclient import TestClient

import main


@pytest.fixture(scope="module")
def client():
    with TestClient(main.app) as test_client:
        yield test_client


def test_app_page_loads(client):
    response = client.get("/app")

    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")


def test_settings_endpoint_returns_expected_fields(client):
    response = client.get("/settings")

    assert response.status_code == 200

    data = response.json()
    assert "model" in data
    assert "temperature" in data
    assert "max_tokens" in data


def test_conversations_endpoint_responds(client):
    response = client.get("/conversations")

    assert response.status_code == 200
    # The endpoint may return a list or an object, depending on
    # your existing response format. Either is acceptable here.
    assert isinstance(response.json(), (list, dict))


def test_openapi_schema_is_available(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200

    schema = response.json()
    assert "paths" in schema
    assert "/settings" in schema["paths"]
    assert "/conversations" in schema["paths"]
