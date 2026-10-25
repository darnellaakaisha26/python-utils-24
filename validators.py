import re
from typing import Any, Optional

def is_valid_email(email: str) -> bool:
    """Validate email string format using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_non_empty_string(value: Any) -> bool:
    """Check if input is a non-empty string."""
    return isinstance(value, str) and len(value.strip()) > 0

def validate_range(value: int, min_val: int, max_val: int) -> bool:
    """Ensure integer is within inclusive boundaries."""
    return isinstance(value, int) and min_val <= value <= max_val

def get_safe_int(value: Any, default: int = 0) -> int:
    """Convert input to int or return default."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def validate_dict_keys(data: dict, required_keys: list[str]) -> bool:
    """Verify all required keys exist in dictionary."""
    return all(key in data for key in required_keys)