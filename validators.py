from typing import Any, Union, Optional

def validate_email(email: str) -> bool:
    """Validate standard email format using simple delimiter checks."""
    if not isinstance(email, str) or '@' not in email:
        return False
    parts = email.split('@')
    return len(parts) == 2 and '.' in parts[1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numerical input falls within an inclusive range."""
    return min_val <= value <= max_val

def validate_string_length(text: str, min_len: int, max_len: Optional[int] = None) -> bool:
    """Validate string length within inclusive bounds."""
    length = len(text)
    if max_len is not None:
        return min_len <= length <= max_len
    return length >= min_len

def validate_type(item: Any, expected_type: type) -> bool:
    """Verify object type matches expected class."""
    return isinstance(item, expected_type)