import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_input(data: dict) -> bool:
    """Ensures dictionary contains mandatory keys with non-empty values."""
    required_keys = ['id', 'payload']
    for key in required_keys:
        if key not in data or not data[key]:
            logger.error(f"missing or invalid key: {key}")
            return False
    return True

def process_stream(data_stream: list):
    """Main processing loop with integrated input validation."""
    for entry in data_stream:
        if not isinstance(entry, dict):
            logger.warning("skipping non-dictionary input")
            continue

        if not validate_input(entry):
            continue

        try:
            logger.info(f"processing entry: {entry['id']}")
            # simulate downstream business logic
            result = f"processed-{entry['payload']}"
            print(result)
        except Exception as e:
            logger.exception(f"unexpected error processing entry {entry.get('id')}: {e}")

if __name__ == '__main__':
    mock_data = [
        {'id': 1, 'payload': 'task_alpha'},
        {'id': 2, 'payload': ''},
        {'invalid': 'entry'},
        {'id': 3, 'payload': 'task_beta'}
    ]
    process_stream(mock_data)