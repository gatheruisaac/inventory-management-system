# Inventory Management System

## Overview

The Inventory Management System is a Python Flask REST API that allows users to manage inventory items through CRUD operations. It also integrates with the OpenFoodFacts API, enabling users to search for products by barcode and add them directly to the inventory through a Command Line Interface (CLI).

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/gatheruisaac/inventory-management-system.git
cd inventory-management-system
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Server

Start the Flask server:

```bash
python app.py
```

The API runs at:

```
http://127.0.0.1:5000
```

---

# Running the CLI

With the Flask server running, open another terminal and run:

```bash
python cli.py
```

The CLI provides an interactive menu for managing inventory and importing products from OpenFoodFacts.

---

# Running Tests

Run all tests with:

```bash
python -m pytest
```

---

# API Endpoints

## Inventory

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/inventory` | Fetch all inventory items |
| GET | `/inventory/<id>` | Fetch a single inventory item |
| POST | `/inventory` | Add a new inventory item |
| PATCH | `/inventory/<id>` | Update an inventory item |
| DELETE | `/inventory/<id>` | Delete an inventory item |

### Example GET `/inventory`

```json
[
  {
    "id": 1,
    "product_name": "Organic Almond Milk",
    "barcode": "1234567890123",
    "brands": "Silk",
    "quantity": 15,
    "price": 450,
    "category": "Dairy Alternatives",
    "nutriscore_grade": "A"
  }
]
```

### Example POST `/inventory`

**Request**

```json
{
  "product_name": "Orange Juice",
  "barcode": "1234567890123",
  "brands": "Minute Maid",
  "ingredients_text": "Orange juice",
  "quantity": 20,
  "price": 350,
  "category": "Beverages",
  "nutriscore_grade": "B"
}
```

**Response**

```json
{
  "id": 6,
  "product_name": "Orange Juice",
  "barcode": "1234567890123",
  "brands": "Minute Maid",
  "ingredients_text": "Orange juice",
  "quantity": 20,
  "price": 350,
  "category": "Beverages",
  "nutriscore_grade": "B"
}
```

### Example PATCH `/inventory/<id>`

**Request**

```json
{
  "quantity": 30,
  "price": 400
}
```

**Response**

```json
{
  "id": 6,
  "quantity": 30,
  "price": 400
}
```

### DELETE `/inventory/<id>`

- Returns **200 OK** when the item is deleted successfully.
- Returns **404 Not Found** if the item does not exist.

---

# External API Integration

This project integrates with the **OpenFoodFacts API** to retrieve product information using a barcode.

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/lookup/<barcode>` | Retrieve product information from OpenFoodFacts |

### Example

```
GET /lookup/5449000000996
```

**Response**

```json
{
  "barcode": "5449000000996",
  "product_name": "coca-cola",
  "brands": "Coca-Cola",
  "ingredients_text": "carbonated water, sugar...",
  "category": "Colas",
  "nutriscore_grade": "E",
  "image_url": "https://..."
}
```

The CLI allows users to import a product from OpenFoodFacts into the inventory by providing the quantity and price.

---

# CLI Options

Run the CLI with:

```bash
python cli.py
```

| Option | Action |
|---------|--------|
| 1 | View Inventory |
| 2 | View Product |
| 3 | Add Product |
| 4 | Update Product |
| 5 | Delete Product |
| 6 | Lookup Product (OpenFoodFacts) |
| 7 | Exit |

---

# Example CLI Session

```text
===================================
 INVENTORY MANAGEMENT SYSTEM
===================================
1. View Inventory
2. View Product
3. Add Product
4. Update Product
5. Delete Product
6. Lookup Product (OpenFoodFacts)
7. Exit

Enter Choice: 6

========== OPENFOODFACTS LOOKUP ==========
Enter Barcode: 5449000000996

========== PRODUCT FOUND ==========
barcode: 5449000000996
product_name: coca-cola
brands: Coca-Cola
category: Colas
nutriscore_grade: e

Add this product to inventory? (y/n): y

Quantity: 20
Price: 180

✅ Product added to inventory successfully!

Enter Choice: 1

========== INVENTORY ==========
ID: 1 | Name: Organic Almond Milk | Price: Ksh 450 | Quantity: 15
ID: 2 | Name: Whole Wheat Bread | Price: Ksh 180 | Quantity: 30
ID: 3 | Name: Corn Flakes | Price: Ksh 550 | Quantity: 20
ID: 4 | Name: Peanut Butter | Price: Ksh 720 | Quantity: 12
ID: 5 | Name: Orange Juice | Price: Ksh 350 | Quantity: 18
ID: 6 | Name: coca-cola | Price: Ksh 180.0 | Quantity: 20
```

---

# Project Structure

```text
inventory-management-system/
├── app.py
├── cli.py
├── data.py
├── requirements.txt
├── README.md
├── routes/
│   ├── inventory.py
│   └── openfoodfacts.py
├── services/
│   ├── api_service.py
│   └── __init__.py
└── tests/
    ├── test_inventory.py
    ├── test_api.py
    └── test_cli.py
```

---

# Technologies Used

- Python
- Flask
- Requests
- Pytest
- Git & GitHub