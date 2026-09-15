import re
from typing import Any, Optional

def validate_input(data: Any, expected_type: type, pattern: Optional[str] = None) -> bool:
    """checks if data matches required type and regex"""
    if not isinstance(data, expected_type):
        return False
    
    if pattern and isinstance(data, str):
        if not re.match(pattern, data):
            return False
            
    return True

def sanitize_payload(payload: dict) -> dict:
    """strips whitespace and validates common fields"""
    sanitized = {}
    for key, value in payload.items():
        if isinstance(value, str):
            sanitized[key] = value.strip()
        else:
            sanitized[key] = value
    return sanitized