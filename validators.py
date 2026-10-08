import re
from typing import Any, Dict, Optional

# regex patterns for core application fields
ID_PATTERN = re.compile(r'^[a-zA-Z0-9_-]+$')
MAX_INPUT_LENGTH = 1024

def validate_payload(data: Dict[str, Any]) -> bool:
    """verify payload structure and content constraints"""
    if not isinstance(data, dict):
        return False

    # check mandatory fields
    if 'id' not in data or 'value' not in data:
        return False

    # validate data types and bounds
    if not isinstance(data['id'], str) or not ID_PATTERN.match(data['id']):
        return False

    if len(str(data['value'])) > MAX_INPUT_LENGTH:
        return False

    return True

def sanitize_input(value: Any) -> Optional[str]:
    """clean string input for downstream processing"""
    if not isinstance(value, str):
        return None
    
    cleaned = value.strip()
    if not cleaned:
        return None
        
    return cleaned[:MAX_INPUT_LENGTH]