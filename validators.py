import re
from typing import Any, Optional

def is_email(value: str) -> bool:
    """Validate standard email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, value))

def is_not_empty(value: Any) -> bool:
    """Check if input has non-zero length."""
    if value is None:
        return False
    return len(str(value).strip()) > 0

def is_numeric_range(value: Any, min_val: float, max_val: float) -> bool:
    """Check if number falls within bounds."""
    try:
        num = float(value)
        return min_val <= num <= max_val
    except (ValueError, TypeError):
        return False

def sanitize_string(value: str, max_length: Optional[int] = None) -> str:
    """Remove whitespace and truncate string."""
    clean = str(value).strip()
    if max_length:
        return clean[:max_length]
    return clean