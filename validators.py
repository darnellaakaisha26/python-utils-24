from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Verify email address format using simple pattern matching."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return email.count("@") == 1 and "." in email.split("@")[1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numerical value falls within specified closed interval."""
    return min_val <= value <= max_val

def ensure_string(data: Any, default: str = "") -> str:
    """Convert input to string if possible, otherwise return default."""
    try:
        return str(data)
    except (ValueError, TypeError):
        return default

def validate_non_empty(value: Optional[str]) -> bool:
    """Determine if string is provided and contains visible characters."""
    return bool(value and value.strip())

def validate_integer(value: Any) -> bool:
    """Verify input can be strictly interpreted as an integer."""
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False