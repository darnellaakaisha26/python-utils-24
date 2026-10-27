class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data: dict, required_keys: list):
    """Ensures all required keys are present and values are non-empty."""
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")
    
    for key in required_keys:
        if key not in data:
            raise ValidationError(f"Missing required key: {key}")
        if data[key] is None:
            raise ValidationError(f"Value for {key} cannot be None")

def process_main_loop(items: list):
    """Main loop processing with input validation layer."""
    required = ['id', 'value']
    processed = []

    for item in items:
        try:
            validate_payload(item, required)
            # Business logic goes here
            processed.append(item['value'] * 2)
        except ValidationError as e:
            print(f"Skipping invalid item: {e}")
            continue
    
    return processed