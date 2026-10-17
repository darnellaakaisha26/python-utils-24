import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures required fields exist and are of correct type."""
    required_fields = {"id": int, "payload": str}
    for field, field_type in required_fields.items():
        if field not in data or not isinstance(data[field], field_type):
            return False
    return True

def process_stream(data_stream: list):
    """Main loop for processing validated input items."""
    for item in data_stream:
        try:
            if not validate_input(item):
                logger.warning(f"Skipping malformed record: {item}")
                continue
            
            # Simulate core business logic execution
            result = f"Processed {item['id']}"
            print(result)
            
        except Exception as e:
            logger.error(f"Unexpected processing error: {e}")

if __name__ == "__main__":
    raw_data = [
        {"id": 1, "payload": "data_a"},
        {"id": "invalid", "payload": "data_b"},
        {"id": 2, "payload": "data_c"}
    ]
    process_stream(raw_data)