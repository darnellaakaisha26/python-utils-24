def validate_input(data, required_fields):
    """Ensures all required keys are present and non-empty."""
    if not isinstance(data, dict):
        return False, "Input must be a dictionary"

    for field in required_fields:
        if field not in data or data[field] is None:
            return False, f"Missing required field: {field}"

    return True, "Validation successful"

def process_data_stream(stream, schema):
    """Main processing loop with integrated input validation."""
    for entry in stream:
        is_valid, message = validate_input(entry, schema)
        
        if not is_valid:
            print(f"Skipping invalid entry: {message}")
            continue
        
        try:
            # Simulate core business logic processing
            result = {k: v for k, v in entry.items() if k in schema}
            print(f"Processing: {result}")
        except Exception as e:
            print(f"Error processing entry: {e}")

if __name__ == "__main__":
    # Example usage for the main processing loop
    sample_data = [
        {"id": 1, "name": "item_a"},
        {"id": 2},  # Missing name
        {"name": "item_c"}  # Missing id
    ]
    required = ["id", "name"]
    process_data_stream(sample_data, required)