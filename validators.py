import re
from typing import Any, Optional

def validate_input(data: Any) -> bool:
    """Checks if input data meets the required structure."""
    if not isinstance(data, dict):
        return False
    
    # Ensure required keys exist and types are correct
    if 'id' not in data or not isinstance(data['id'], int):
        return False
        
    # Regex validation for alphanumeric labels
    label = data.get('label', '')
    if not isinstance(label, str) or not re.match(r'^[a-zA-Z0-9_]{3,20}$', label):
        return False
        
    return True

def sanitize_input(value: Any) -> str:
    """Strips whitespace and enforces string format."""
    return str(value).strip()

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass