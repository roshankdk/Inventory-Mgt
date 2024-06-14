import random
from packaging_details import save_packaging_details


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
