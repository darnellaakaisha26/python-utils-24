from typing import Any, Union, Optional
import re

def is_email(value: str) -> bool:
    """Validate if the provided string is a standard email address."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, value))

def is_not_empty(value: Any) -> bool:
    """Check if the input object contains data."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict, set)):
        return len(value) > 0
    return True

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Verify numeric value falls within inclusive boundaries."""
    return min_val <= value <= max_val

def sanitize_string(value: Optional[str]) -> str:
    """Strip whitespace and return empty string if input is None."""
    if value is None:
        return ""
    return value.strip()