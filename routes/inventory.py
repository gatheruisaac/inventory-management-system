from flask import Blueprint, jsonify, request
from data import inventory

inventory_bp = Blueprint("inventory", __name__)

next_id = len(inventory) + 1


# GET /inventory
@inventory_bp.route("/inventory", methods=["GET"])
def get_all_items():
    return jsonify(inventory), 200


# GET /inventory/<id>
@inventory_bp.route("/inventory/<int:item_id>", methods=["GET"])
def get_one_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# POST /inventory
@inventory_bp.route("/inventory", methods=["POST"])
def add_item():
    global next_id

    data = request.get_json()

    if not data:
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
    next_id += 1

    return jsonify(new_item), 201


# PATCH /inventory/<id>
@inventory_bp.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_item(item_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    for item in inventory:

        if item["id"] == item_id:

            fields = [
                "product_name",
                "barcode",
                "brands",
                "ingredients_text",
                "quantity",
                "price",
                "category",
                "nutriscore_grade"
            ]

            for field in fields:
                if field in data:
                    item[field] = data[field]

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404


# DELETE /inventory/<id>
@inventory_bp.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):

    for item in inventory:

        if item["id"] == item_id:
            inventory.remove(item)

            return jsonify({
                "message": "Item deleted successfully",
                "id": item_id
            }), 200

    return jsonify({"error": "Item not found"}), 404