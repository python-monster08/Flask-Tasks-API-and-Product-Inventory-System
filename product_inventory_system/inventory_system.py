import json
import os

INVENTORY_FILE = 'product_inventory.json'

class ProductInventory:
    def __init__(self, file_name=INVENTORY_FILE):
        self.file_name = file_name
        self.products = self.load_products()

    def load_products(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Error loading inventory. Starting with an empty list.")
                return []
        return []

    def save_products(self):
        try:
            with open(self.file_name, 'w') as file:
                json.dump(self.products, file, indent=4)
        except Exception as e:
            print(f"Error saving products: {e}")

    def add_product(self, product_id, product_name, quantity, price):
        product = {
            "Product ID": product_id,
            "Product Name": product_name,
            "Quantity": quantity,
            "Price": price
        }
        self.products.append(product)
        self.save_products()
        print(f"Product {product_name} added successfully!")

    def display_products(self):
        if not self.products:
            print("No products found in the inventory.")
            return
        for product in self.products:
            print(f"Product ID: {product['Product ID']}, "
                  f"Product Name: {product['Product Name']}, "
                  f"Quantity: {product['Quantity']}, "
                  f"Price: {product['Price']}")
        print()

    def update_product(self, product_id, new_quantity=None, new_price=None):
        for product in self.products:
            if product['Product ID'] == product_id:
                if new_quantity is not None:
                    product['Quantity'] = new_quantity
                if new_price is not None:
                    product['Price'] = new_price
                self.save_products()
                print(f"Product {product_id} updated successfully!")
                return
        print(f"Product with ID {product_id} not found.")

    def delete_product(self, product_id):
        for product in self.products:
            if product['Product ID'] == product_id:
                self.products.remove(product)
                self.save_products()
                print(f"Product {product_id} deleted successfully!")
                return
        print(f"Product with ID {product_id} not found.")

def main():
    inventory = ProductInventory()

    while True:
        print("\nProduct Inventory System")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            inventory.add_product(product_id, product_name, quantity, price)

        elif choice == '2':
            inventory.display_products()

        elif choice == '3':
            product_id = input("Enter Product ID to update: ")
            new_quantity = input("Enter new Quantity (leave blank to keep current): ")
            new_price = input("Enter new Price (leave blank to keep current): ")

            new_quantity = int(new_quantity) if new_quantity else None
            new_price = float(new_price) if new_price else None
            inventory.update_product(product_id, new_quantity, new_price)

        elif choice == '4':
            product_id = input("Enter Product ID to delete: ")
            inventory.delete_product(product_id)

        elif choice == '5':
            print("Exiting Product Inventory System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
