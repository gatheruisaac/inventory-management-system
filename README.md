# Inventory Management System

## Overview

This is a Python Flask REST API that allows users to manage inventory items through CRUD operations. It also integrates with the OpenFoodFacts API, enabling users to search products by barcode and add them directly to the inventory using a Command Line Interface (CLI).

## Features

- View all inventory items
- View a single inventory item
- Add, update, and delete products
- Lookup products using the OpenFoodFacts API
- Add products from OpenFoodFacts to the inventory
- Command Line Interface (CLI)
- Unit testing with pytest

## Technologies Used

- Python
- Flask
- Requests
- Pytest
- Git & GitHub

## Project Structure

inventory-management-system/
├── app.py
├── cli.py
├── data.py
├── routes/
├── services/
├── tests/
├── requirements.txt
└── README.md


## Installation

Clone the repository:

git clone https://github.com/gatheruisaac/inventory-management-system.git

cd inventory-management-system


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
```

Install dependencies:


pip install -r requirements.txt


## Running the Application

Start the Flask server:

python app.py

Run the CLI in another terminal:

python cli.py


## API Endpoints

| Method | Endpoint |
|--------|----------|
| GET | /inventory |
| GET | /inventory/<id> |
| POST | /inventory |
| PATCH | /inventory/<id> |
| DELETE | /inventory/<id> |
| GET | /lookup/<barcode> |

## Running Tests

Run all tests with:


python -m pytest


## Author

**Isaac Gatheru**

GitHub: https://github.com/gatheruisaac

## License

This project is licensed under the MIT License.