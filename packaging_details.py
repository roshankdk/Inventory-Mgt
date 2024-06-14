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