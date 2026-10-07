import logging

logger = logging.getLogger(__name__)

def validate_input_data(data: dict) -> bool:
    """Validate schema and content of input dictionary."""
    required_fields = ['id', 'payload']
    
    if not isinstance(data, dict):
        logger.error("Invalid input type: expected dictionary")
        return False
        
    if not all(field in data for field in required_fields):
        logger.warning("Missing required fields in payload")
        return False
        
    if not isinstance(data['id'], int):
        logger.warning("Invalid type for id: expected integer")
        return False
        
    return True

def process_main_loop(items: list):
    """Execute processing with input validation safeguards."""
    for item in items:
        if not validate_input_data(item):
            continue
            
        try:
            # Simulate core business logic
            result = item['payload'] * 2
            logger.info(f"Processed item {item['id']}: {result}")
        except Exception as e:
            logger.error(f"Processing error on item {item['id']}: {e}")