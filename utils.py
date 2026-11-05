import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures input data contains required fields."""
    required = ['id', 'payload']
    return all(key in data for key in required)

def process_items(items: list):
    """
    Main processing loop with integrated validation.
    Skips malformed items and continues processing.
    """
    for index, item in enumerate(items):
        try:
            if not isinstance(item, dict) or not validate_input(item):
                logger.warning(f"skipping invalid item at index {index}")
                continue
            
            # Simulate core logic execution
            result = f"processed-{item['id']}"
            logger.info(f"item {index} success: {result}")
            
        except Exception as e:
            logger.error(f"unexpected error on index {index}: {e}")

if __name__ == "__main__":
    # Sample data stream
    raw_data = [
        {'id': 1, 'payload': 'data_a'},
        {'invalid': 'entry'},
        {'id': 2, 'payload': 'data_b'}
    ]
    process_items(raw_data)