from flask import Blueprint, jsonify
from services.api_service import lookup_product

openfoodfacts_bp = Blueprint("openfoodfacts", __name__)


@openfoodfacts_bp.route("/lookup/<barcode>", methods=["GET"])
def lookup_barcode(barcode):

    result, status = lookup_product(barcode)

    return jsonify(result), status