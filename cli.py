import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        inventory = response.json()

        print("\n========== INVENTORY ==========")
        for item in inventory:
            print(
                f"ID: {item['id']} | "
                f"Name: {item.get('product_name', item.get('name'))} | "
                f"Price: Ksh {item['price']} | "
                f"Quantity: {item['quantity']}"
            )
    else:
        print("Error:", response.json())


def view_product():
    item_id = input("\nEnter Product ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        item = response.json()

        print("\n========== PRODUCT DETAILS ==========")
        for key, value in item.items():
            print(f"{key}: {value}")

    else:
        print(response.json()["error"])


def add_product():
    print("\n========== ADD PRODUCT ==========")

    product = {
        "product_name": input("Product Name: "),
        "barcode": input("Barcode: "),
        "brands": input("Brand: "),
        "ingredients_text": input("Ingredients: "),
        "quantity": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "category": input("Category: "),
        "nutriscore_grade": input("Nutriscore Grade: ")
    }

    response = requests.post(f"{BASE_URL}/inventory", json=product)

    if response.status_code == 201:
        print("\n✅ Product Added Successfully!")
    else:
        print(response.json())


def update_product():
    print("\n========== UPDATE PRODUCT ==========")

    item_id = input("Enter Product ID: ")

    quantity = input("New Quantity (leave blank to skip): ")
    price = input("New Price (leave blank to skip): ")

    updates = {}

    if quantity:
        updates["quantity"] = int(quantity)

    if price:
        updates["price"] = float(price)

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=updates
    )

    if response.status_code == 200:
        print("\n✅ Product Updated Successfully!")
        print(response.json())
    else:
        print(response.json())


def delete_product():
    print("\n========== DELETE PRODUCT ==========")

    item_id = input("Enter Product ID: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print("\n✅ Product Deleted Successfully!")
    else:
        print(response.json())


def lookup_product():
    print("\n========== OPENFOODFACTS LOOKUP ==========")

    barcode = input("Enter Barcode: ")

    response = requests.get(f"{BASE_URL}/lookup/{barcode}")

    if response.status_code == 200:
        product = response.json()

        print("\n========== PRODUCT FOUND ==========")

        for key, value in product.items():
            print(f"{key}: {value}")

    else:
        print(response.json())


def menu():
    while True:

        print("\n===================================")
        print(" INVENTORY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. View Inventory")
        print("2. View Product")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Lookup Product (OpenFoodFacts)")
        print("7. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_product()

        elif choice == "3":
            add_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            lookup_product()

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()