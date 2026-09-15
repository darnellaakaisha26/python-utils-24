import re
from typing import Any, Dict, Optional

def validate_payload(data: Dict[str, Any]) -> bool:
    """
    Validates core input structure and data types.
    Ensures required keys are present and data formats are valid.
    """
    required_keys = {'id', 'value', 'timestamp'}
    if not all(key in data for key in required_keys):
        return False

    if not isinstance(data['id'], str) or not re.match(r'^[a-z0-9-]+$', data['id']):
        return False

    if not isinstance(data['value'], (int, float)):
        return False

    if not isinstance(data['timestamp'], int) or data['timestamp'] <= 0:
        return False

    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Cleans input data by stripping whitespace and enforcing types.
    """
    return {
        'id': str(data['id']).strip().lower(),
        'value': float(data['value']),
        'timestamp': int(data['timestamp'])
    }

def process_with_validation(raw_data: Any) -> Optional[Dict[str, Any]]:
    """
    Wrapper for validation logic in the main processing loop.
    """
    if not isinstance(raw_data, dict):
        return None

    if validate_payload(raw_data):
        return sanitize_input(raw_data)

    return None