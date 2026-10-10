import re

def validate_input_data(data: dict) -> bool:
    """Validates expected keys and data formats."""
    required_keys = {'id', 'payload', 'timestamp'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        return False

    # Validate ID format (must be alphanumeric)
    if not re.match(r'^[a-zA-Z0-9]+$', str(data['id'])):
        return False

    # Validate payload is non-empty
    if not data['payload']:
        return False

    return True

def process_main_loop(data_stream: list):
    """Main loop with validation logic."""
    processed = []
    for item in data_stream:
        if not isinstance(item, dict):
            continue
            
        if validate_input_data(item):
            # Logic for data handling
            processed.append(item)
        else:
            # Log invalid input and skip
            print(f"Skipping invalid entry: {item}")
            
    return processed