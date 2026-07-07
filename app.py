from flask import Flask, jsonify, request
import requests

app = Flask(__name__)



# GET /inventory - return all items in the inventory list
@app.route("/inventory", methods=["GET"])
def get_all_items():
    return jsonify(inventory), 200


# GET /inventory/<id> - return one item by its ID
@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_one_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST /inventory - add a new item to the inventory list
@app.route("/inventory", methods=["POST"])
def add_item():
    global next_id

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    if "product_name" not in data:
        return jsonify({"error": "product_name is required"}), 400

    new_item = {
        "id": next_id,
        "barcode": data.get("barcode", ""),
        "product_name": data.get("product_name", ""),
        "brands": data.get("brands", ""),
        "ingredients_text": data.get("ingredients_text", ""),
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0),
        "category": data.get("category", ""),
        "nutriscore_grade": data.get("nutriscore_grade", "")
    }

    inventory.append(new_item)
    next_id = next_id + 1

    return jsonify(new_item), 201


# PATCH /inventory/<id> - update fields on an existing item
@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    for item in inventory:
        if item["id"] == item_id:

            # Only update the fields that were included in the request
            if "product_name" in data:
                item["product_name"] = data["product_name"]
            if "brands" in data:
                item["brands"] = data["brands"]
            if "ingredients_text" in data:
                item["ingredients_text"] = data["ingredients_text"]
            if "quantity" in data:
                item["quantity"] = data["quantity"]
            if "price" in data:
                item["price"] = data["price"]
            if "category" in data:
                item["category"] = data["category"]
            if "nutriscore_grade" in data:
                item["nutriscore_grade"] = data["nutriscore_grade"]

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE /inventory/<id> - remove an item from the inventory list
@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted", "id": item_id}), 200

    return jsonify({"error": "Item not found"}), 404


# GET /lookup/<barcode> - fetch product info from OpenFoodFacts by barcode
@app.route("/lookup/<barcode>", methods=["GET"])
def lookup_barcode(barcode):
    url = "https://world.openfoodfacts.org/api/v0/product/" + barcode + ".json"
    response = requests.get(url)
    data = response.json()

    if data["status"] != 1:
        return jsonify({"error": "Product not found on OpenFoodFacts"}), 404

    product = data["product"]

    result = {
        "barcode": barcode,
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "ingredients_text": product.get("ingredients_text", ""),
        "nutriscore_grade": product.get("nutriscore_grade", ""),
        "image_url": product.get("image_url", "")
    }

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)