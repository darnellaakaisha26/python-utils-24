class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_payload(data):
    """
    Validates that the input is a non-empty dictionary
    containing required keys.
    """
    if not isinstance(data, dict):
        raise ValidationError("Payload must be a dictionary")
    
    required_keys = {"id", "payload"}
    if not required_keys.issubset(data.keys()):
        missing = required_keys - data.keys()
        raise ValidationError(f"Missing required keys: {missing}")
    
    if not isinstance(data.get("id"), int):
        raise ValidationError("Field 'id' must be an integer")

def process_main_loop(data_stream):
    """
    Main processing loop with integrated input validation.
    """
    for entry in data_stream:
        try:
            validate_payload(entry)
            # Logic for valid data processing goes here
            print(f"Processing record: {entry['id']}")
        except ValidationError as e:
            print(f"Skipping invalid entry: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")