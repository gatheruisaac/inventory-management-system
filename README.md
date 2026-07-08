# Inventory Management System

## Overview

This project is a Python Flask REST API that allows users to manage inventory items through CRUD operations. It also integrates with the OpenFoodFacts API, allowing users to search products by barcode and add them directly to the inventory through a Command Line Interface (CLI).

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

```text
inventory-management-system/
├── app.py
├── cli.py
├── data.py
├── routes/
├── services/
├── tests/
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/gatheruisaac/inventory-management-system.git
cd inventory-management-system
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Open another terminal, activate the virtual environment again, and run the CLI:

```bash
python cli.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/inventory` | Get all inventory items |
| GET | `/inventory/<id>` | Get one inventory item |
| POST | `/inventory` | Add a new inventory item |
| PATCH | `/inventory/<id>` | Update an inventory item |
| DELETE | `/inventory/<id>` | Delete an inventory item |
| GET | `/lookup/<barcode>` | Lookup a product using OpenFoodFacts |

## Running Tests

Run all tests with:

```bash
python -m pytest
```

## Author

**Isaac Gatheru**

GitHub: https://github.com/gatheruisaac

## License

This project is licensed under the MIT License.