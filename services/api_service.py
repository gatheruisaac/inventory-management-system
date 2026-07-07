import requests


def lookup_product(barcode):
    """
    Fetch product information from OpenFoodFacts using a barcode.
    """

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (isaac@example.com)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as e:
        print("OpenFoodFacts Error:", e)
        return {
            "error": "Could not connect to OpenFoodFacts"
        }, 503

    if data.get("status") != 1:
        return {
            "error": "Product not found on OpenFoodFacts"
        }, 404

    product = data.get("product", {})

    result = {
        "barcode": barcode,
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "ingredients_text": product.get("ingredients_text", ""),
        "category": product.get("categories", ""),
        "nutriscore_grade": product.get("nutriscore_grade", ""),
        "image_url": product.get("image_url", "")
    }

    return result, 200