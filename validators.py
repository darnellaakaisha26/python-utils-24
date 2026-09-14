import re
from typing import Any, Optional

def is_email(email: str) -> bool:
    """Validate standard email format."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_not_empty(value: Any) -> bool:
    """Check if string or collection is non-empty."""
    return bool(value and len(str(value).strip()) > 0)

def is_integer(value: Any) -> bool:
    """Determine if value is a valid integer representation."""
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def validate_length(value: str, min_len: int = 0, max_len: Optional[int] = None) -> bool:
    """Ensure string length within boundaries."""
    if not isinstance(value, str):
        return False
    length = len(value)
    if max_len is not None:
        return min_len <= length <= max_len
    return length >= min_len

def sanitize_input(value: str) -> str:
    """Remove whitespace and escape potential script tags."""
    if not isinstance(value, str):
        return ''
    clean = value.strip()
    clean = clean.replace('<', '&lt;').replace('>', '&gt;')
    return clean