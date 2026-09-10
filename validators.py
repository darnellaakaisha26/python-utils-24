from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Validate string format for a standard email address."""
    if not isinstance(email, str) or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and all(parts)

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numeric value falls within inclusive range."""
    return min_val <= value <= max_val

def ensure_list(data: Any, default: Optional[list] = None) -> list:
    """Coerce input into list or return provided default."""
    if isinstance(data, list):
        return data
    return default if default is not None else []

def is_not_empty(value: Optional[str]) -> bool:
    """Verify that string is not None and not whitespace."""
    return bool(value and value.strip())