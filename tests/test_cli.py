from unittest.mock import patch
import cli


@patch("builtins.print")
@patch("requests.get")
def test_view_inventory(mock_get, mock_print):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "product_name": "Sprite",
            "price": 180,
            "quantity": 20
        }
    ]

    cli.view_inventory()

    mock_get.assert_called_once()


@patch("builtins.input", return_value="737628064502")
@patch("builtins.print")
@patch("requests.get")
def test_lookup_product(mock_get, mock_print, mock_input):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "product_name": "Sprite",
        "brands": "Coca-Cola"
    }

    cli.lookup_product()

    mock_get.assert_called_once()