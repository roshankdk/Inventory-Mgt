# data_loader.py
import pandas as pd

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
