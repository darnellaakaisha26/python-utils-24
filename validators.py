import logging

# Configure logger for module activities
logger = logging.getLogger(__name__)

def validate_input_data(data):
    """Ensures input data conforms to expected schema."""
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    
    required_fields = ['id', 'payload', 'timestamp']
    for field in required_fields:
        if field not in data:
            logger.error(f"Missing required field: {field}")
            return False
    
    if not isinstance(data.get('id'), int):
        logger.warning("Invalid ID format provided")
        return False
        
    return True

def process_main_loop(items):
    """Main processing loop with integrated validation logic."""
    results = []
    for item in items:
        try:
            if validate_input_data(item):
                # Simulate processing logic
                processed = item.get('payload').upper()
                results.append(processed)
            else:
                logger.info(f"Skipping invalid item: {item.get('id')}")
        except Exception as e:
            logger.exception(f"Unexpected error during processing: {e}")
            continue
            
    return results