import pytest
from fastapi.testclient import TestClient

from orderlab.api import create_app


@pytest.fixture
def client():
    with TestClient(create_app()) as test_client:
        yield test_client


def test_create_and_get(client):
    expected = {"id": 1, "subtotal": 20_000}
    created = client.post("/orders", json={"price": 10_000, "quantity": 2})
    assert created.status_code == 201
    assert created.json() == expected

    fetched = client.get("/orders/1")
    assert fetched.status_code == 200
    assert fetched.json() == expected


def test_not_found(client):
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not found"}


@pytest.mark.parametrize(
    "payload, field",
    [
        ({"price": 100, "quantity": 0}, "quantity"),
        ({"price": -1, "quantity": 2}, "price"),
    ],
)
def test_invalid_order(client, payload, field):
    response = client.post("/orders", json=payload)
    assert response.status_code == 422
    assert any(error["loc"] == ["body", field] for error in response.json()["detail"])


def test_app_instances_are_isolated(client):
    created = client.post("/orders", json={"price": 100, "quantity": 2})
    assert created.status_code == 201

    with TestClient(create_app()) as other_client:
        assert other_client.get("/orders/1").status_code == 404
