from data_loader import load_inventory_from_excel
from Order import place_order
from packaging_details import save_packaging_details
from result_display import display_inventory

# main driver function
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
