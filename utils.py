import logging

# Configure logger for module tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_data_stream(items):
    """Processes a stream of inputs with strict validation."""
    valid_results = []
    
    for item in items:
        try:
            # Validation logic: Ensure data is a non-empty dictionary
            if not isinstance(item, dict) or not item:
                raise ValueError(f"Invalid input format: {type(item).__name__}")
            
            # Ensure required key exists
            if 'value' not in item:
                raise KeyError("Missing 'value' key in input")
            
            # Ensure value is a positive integer
            val = item.get('value')
            if not isinstance(val, int) or val < 0:
                raise TypeError(f"Non-positive integer encountered: {val}")
            
            valid_results.append(val * 2)
        except (ValueError, KeyError, TypeError) as e:
            logger.error(f"Skipping invalid item: {e}")
            continue
            
    return valid_results

if __name__ == "__main__":
    data = [{'value': 10}, 'bad_input', {'value': -5}, {'value': 20}, {}]
    results = process_data_stream(data)
    logger.info(f"Processed results: {results}")