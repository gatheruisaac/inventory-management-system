from flask import Flask
from routes.inventory import inventory_bp
from routes.openfoodfacts import openfoodfacts_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(inventory_bp)
app.register_blueprint(openfoodfacts_bp)

if __name__ == "__main__":
    app.run(debug=True)