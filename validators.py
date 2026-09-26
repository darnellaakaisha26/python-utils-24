import re
from typing import Any, Dict, List, Tuple

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validate_dict_schema(
    data: Dict[str, Any], schema: Dict[str, Tuple[type, bool]]
) -> Tuple[bool, List[str]]:
    """
    Validates a dictionary's keys and value types against a schema definition.

    The schema mapping should be: {key_name: (expected_type, is_required)}
    """
    errors = []

    if not isinstance(data, dict):
        return False, ["Input data is not a dictionary"]

    for key, (expected_type, required) in schema.items():
        if key not in data:
            if required:
                errors.append(f"Missing required key: '{key}'")
            continue

        value = data[key]
        if value is None and not required:
            continue

        if not isinstance(value, expected_type):
            actual_type = type(value).__name__
            expected_type_name = getattr(expected_type, "__name__", str(expected_type))
            errors.append(
                f"Invalid type for '{key}': expected {expected_type_name}, got {actual_type}"
            )

    return len(errors) == 0, errors


def is_valid_email(email: str) -> bool:
    """
    Checks if the provided string matches a general email format.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))
