from unittest.mock import patch
from app import app


@patch("services.api_service.requests.get")
def test_lookup_product(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Sprite",
            "brands": "Coca-Cola",
            "ingredients_text": "Water, Sugar",
            "categories": "Soft Drinks",
            "nutriscore_grade": "B",
            "image_url": "https://example.com/image.jpg"
        }
    }

    client = app.test_client()

    response = client.get("/lookup/5449000000996")

    assert response.status_code == 200

    data = response.get_json()

    assert data["product_name"] == "Sprite"
    assert data["brands"] == "Coca-Cola"