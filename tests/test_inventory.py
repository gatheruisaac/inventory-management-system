import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):
    response = client.get("/inventory")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_product(client):
    response = client.get("/inventory/1")

    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_add_product(client):
    response = client.post(
        "/inventory",
        json={
            "product_name": "Test Product",
            "barcode": "111111111111",
            "quantity": 5,
            "price": 100
        }
    )

    assert response.status_code == 201
    assert response.get_json()["product_name"] == "Test Product"


def test_update_product(client):
    response = client.patch(
        "/inventory/1",
        json={
            "price": 999
        }
    )

    assert response.status_code == 200
    assert response.get_json()["price"] == 999


def test_delete_product(client):
    response = client.delete("/inventory/1")

    assert response.status_code == 200