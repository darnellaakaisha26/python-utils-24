import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary with required keys."""
    if not isinstance(data, dict):
        return False, "Data must be a dictionary"
    if "task_id" not in data or "payload" not in data:
        return False, "Missing mandatory keys: task_id, payload"
    return True, None

def run_processing_loop(data_stream):
    """Main processing loop with integrated input validation."""
    for entry in data_stream:
        is_valid, error = validate_input(entry)
        
        if not is_valid:
            logger.error(f"validation failed: {error}")
            continue

        try:
            process_task(entry['task_id'], entry['payload'])
        except Exception as e:
            logger.error(f"task {entry['task_id']} execution error: {e}")

def process_task(task_id, payload):
    """Actual business logic execution."""
    print(f"Processing task {task_id} with payload {payload}")

if __name__ == '__main__':
    mock_data = [
        {"task_id": 1, "payload": "data_a"},
        {"invalid": "payload"},
        {"task_id": 2, "payload": "data_b"}
    ]
    run_processing_loop(mock_data)