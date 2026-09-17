import logging

logger = logging.getLogger(__name__)

def validate_input(data: dict, required_keys: list) -> bool:
    """
    Validates that all required keys exist and have non-empty values.
    """
    try:
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary")
            
        for key in required_keys:
            if key not in data or data[key] is None:
                logger.error(f"Validation failed: missing key '{key}'")
                return False
        return True
    except Exception as e:
        logger.exception(f"Unexpected validation error: {e}")
        return False

def process_main_loop(items: list, schema: list):
    """
    Processes items in a loop with mandatory validation.
    """
    results = []
    for index, item in enumerate(items):
        if not validate_input(item, schema):
            logger.warning(f"Skipping invalid item at index {index}")
            continue
        
        # Process logic
        processed_data = {k: item[k] for k in schema}
        results.append(processed_data)
        
    return results