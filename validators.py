import json
import re
from typing import Any, Dict, List, Tuple


def is_valid_email(email: str) -> bool:
    """Check if a string is a valid email address."""
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))


def is_valid_json(json_str: str) -> bool:
    """Verify whether a string contains valid JSON data."""
    if not isinstance(json_str, str):
        return False
    try:
        json.loads(json_str)
        return True
    except (ValueError, TypeError):
        return False


def validate_dict_schema(data: Dict[str, Any], schema: Dict[str, type]) -> Tuple[bool, List[str]]:
    """Validate a dictionary against an expected key-type schema.

    Args:
        data: The input dictionary to validate.
        schema: Mapping of required keys to their expected data types.

    Returns:
        A tuple of (is_valid, error_messages).
    """
    errors: List[str] = []
    if not isinstance(data, dict):
        return False, ["Input data must be a dictionary"]

    for field, expected_type in schema.items():
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
        elif not isinstance(data[field], expected_type):
            actual_type = type(data[field]).__name__
            errors.append(
                f"Field '{field}' expected {expected_type.__name__}, got {actual_type}"
            )

    return len(errors) == 0, errors


def sanitize_string(val: Any) -> str:
    """Convert input to a clean string, stripping surrounding white space."""
    if val is None:
        return ""
    return str(val).strip()
