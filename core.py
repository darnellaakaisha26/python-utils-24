import logging

# Configure logger for module tracking
logger = logging.getLogger(__name__)

def validate_input(data):
    """Ensures input is a non-empty dictionary."""
    if not isinstance(data, dict):
        return False
    if not data:
        return False
    return 'payload' in data and isinstance(data['payload'], (str, int))

def run_processing_loop(data_stream):
    """Main processing loop with input validation."""
    for entry in data_stream:
        try:
            if not validate_input(entry):
                logger.warning(f"Skipping invalid entry: {entry}")
                continue
            
            process_data(entry['payload'])
        except Exception as e:
            logger.error(f"Unexpected loop error: {e}")

def process_data(value):
    """Handles individual data payloads."""
    print(f"Processing value: {value}")

if __name__ == "__main__":
    sample_data = [
        {'payload': 'alpha'},
        {'payload': 42},
        {'invalid': 'data'},
        {},
        "not a dict"
    ]
    run_processing_loop(sample_data)