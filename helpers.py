import re


def validate_input_data(data: dict) -> bool:
    """
    Validates core structure and values for processing loop.
    Ensures fields are present and data types are valid.
    """
    required_keys = {'id', 'payload', 'timestamp'}
    
    # Check for missing keys
    if not all(key in data for key in required_keys):
        return False

    # Validate payload format using regex
    if not isinstance(data['payload'], str) or not re.match(r'^[a-zA-Z0-9_]+$', data['payload']):
        return False

    # Validate ID type
    if not isinstance(data['id'], int) or data['id'] < 0:
        return False

    return True


def process_main_loop(queue: list):
    """
    Main processing loop with integrated input validation.
    """
    results = []
    for item in queue:
        if not isinstance(item, dict):
            continue

        if validate_input_data(item):
            # Perform business logic here
            processed_val = item['payload'].upper()
            results.append(processed_val)
        else:
            # Log invalid input and skip
            print(f"Skipping invalid entry: {item}")
            
    return results