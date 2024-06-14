# data_processor.py
def process_data(data):
    if data is None:
        print("No data to process.")
        return None
    try:
        # Process the data (e.g., calculating the mean of numerical columns)
        processed_data = data.mean()
        return processed_data
    except AttributeError as e:
        print(f"Error processing data: {e}")
        return None
