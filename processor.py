import logging

def validate_input(data):
    """Ensures input data conforms to expected format."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    if "id" not in data or "value" not in data:
        raise KeyError("Missing required fields: 'id' or 'value'")
    if not isinstance(data["value"], (int, float)):
        raise TypeError("Field 'value' must be numeric")
    return True

def process_items(items):
    """Main processing loop with integrated validation."""
    processed = []
    for entry in items:
        try:
            if validate_input(entry):
                # Simulate business logic
                result = entry["value"] * 2
                processed.append({"id": entry["id"], "result": result})
        except (ValueError, KeyError, TypeError) as e:
            logging.error(f"Skipping invalid entry {entry}: {e}")
            continue
    return processed

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sample_data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "invalid"},
        {"id": 3, "value": 25.5},
        {}
    ]
    results = process_items(sample_data)
    print(f"Processed {len(results)} items successfully.")