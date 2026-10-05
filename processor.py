import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_payload(data):
    """Ensure input data matches expected schema."""
    if not isinstance(data, dict):
        raise ValueError("Payload must be a dictionary")
    if "id" not in data or not isinstance(data["id"], int):
        raise ValueError("Valid integer 'id' field required")
    return True

def process_items(items):
    """Main processing loop with input validation."""
    for index, item in enumerate(items):
        try:
            validate_payload(item)
            # Simulate core processing logic
            result = item.get("id") * 2
            logger.info(f"Processed item {index}: result={result}")
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid item at index {index}: {e}")
            continue

if __name__ == "__main__":
    dataset = [
        {"id": 10, "name": "alpha"},
        {"id": "invalid", "name": "beta"},
        {"id": 20, "name": "gamma"},
        "corrupted_data"
    ]
    process_items(dataset)