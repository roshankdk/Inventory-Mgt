# result_display.py
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