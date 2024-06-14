import pandas as pd
import random


def load_inventory_from_excel(file_path):
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        inventory = df.set_index("Product").to_dict("index")
        for item in inventory.values():
            item["price"] = float(item.pop("Price$"))
            item["quantity"] = int(item.pop("Inventory"))
        return inventory
    except FileNotFoundError:
        print(f"Error: The file at path '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def display_inventory(inventory):
    print("\nAvailable Products:")
    print(
        "{:<15} {:<10} {:<10} {:<15}".format(
            "Product", "Inventory", "Price", "Location"
        )
    )
    print("-" * 50)
    for product, details in inventory.items():
        print(
            "{:<15} {:<10} {:<10} {:<15}".format(
                product,
                details["quantity"],
                f"${details['price']:.2f}",
                details.get("Location", ""),
            )
        )


def save_packaging_details(packaging_details, file_path):
    try:
        with open(file_path, 'a') as file:
            file.write("Customer Name: " + packaging_details['name'] + "\n")
            file.write("Customer ID: " + packaging_details['id'] + "\n")
            file.write("Ordered Items:\n")
            for item in packaging_details['items']:
                file.write(f"- {item['quantity']} {item['product']}(s)\n")
            file.write("Total Cost: $" + str(packaging_details['total_cost']) + "\n")
            file.write("Packing Number: " + str(packaging_details['packing_number']) + "\n")
            file.write("-" * 50 + "\n")  # Separator line
        print("Packaging details saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving packaging details: {e}")



def place_order(customer_details, inventory, packing_numbers, packaging_file_path):
    name = customer_details.get('name', 'Unknown')
    customer_id = customer_details.get('id', '00000')

    order = []
    total_cost = 0
    
    while True:
        product = input("Enter the product name you want to order (or type 'done' to finish): ").capitalize()
        if product == 'Done':
            break
        
        if product not in inventory:
            print("Sorry, the product is not available.")
            continue

        try:
            quantity = int(input(f"Enter the quantity of {product} you want to order: "))
            if quantity <= 0:
                print("Quantity should be greater than zero.")
                continue
        except ValueError:
            print("Invalid quantity entered. Please enter a valid number.")
            continue
        
        if quantity > inventory[product]["quantity"]:
            print("Sorry, the quantity you requested is not available.")
            continue
        
        order.append({'product': product, 'quantity': quantity})
        total_cost += inventory[product]["price"] * quantity
        
        # Update inventory
        inventory[product]["quantity"] -= quantity
        
        print(f"{product} added to the order.")
    
    if not order:
        print("No items selected for the order.")
        return
    
    print("\nOrder Summary:")
    print(f"Customer Name: {name}")
    print(f"Customer ID: {customer_id}")
    print("Ordered Items:")
    for item in order:
        print(f"- {item['quantity']} {item['product']}(s)")
    print(f"Total Cost: ${total_cost:.2f}")

    packing_number = random.choice(packing_numbers)
    packing_numbers.remove(packing_number)
    print(f"Packing Number: {packing_number}")

    # Save packaging details to file
    packaging_details = {
        'name': name,
        'id': customer_id,
        'items': order,
        'total_cost': total_cost,
        'packing_number': packing_number
    }
    save_packaging_details(packaging_details, packaging_file_path)

def main():
    file_path = r"inventory.csv.xlsx"  # Replace with the actual path to your Excel file
    inventory = load_inventory_from_excel(file_path)
    if inventory is None:
        return

    # Initialize packing numbers
    packing_numbers = [i for i in range(1, 101)]

    # Collect customer details
    name = input("Enter your name: ")
    while True:
        customer_id = input("Enter your 5-digit ID: ")
        if len(customer_id) == 5 and customer_id.isdigit():
            break
        print("Invalid ID. Please enter a 5-digit number.")

    customer_details = {"name": name, "id": customer_id}

    # File path to save packaging details
    packaging_file_path = "packaging_details.txt"

    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Place Order")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            place_order(
                customer_details, inventory, packing_numbers, packaging_file_path
            )
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
