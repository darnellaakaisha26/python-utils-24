"""Data validation utility functions for general python projects."""

import re
from typing import Any, Mapping, Sequence

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")


def is_valid_email(email: str) -> bool:
    """Check whether a given string is a valid email address format.

    Args:
        email: The string to validate as an email.

    Returns:
        True if the string matches email format, False otherwise.
    """
    if not isinstance(email, str) or not email:
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_in_range(val: float, min_val: float, max_val: float, inclusive: bool = True) -> bool:
    """Validate if a numeric value falls within a specified range.

    Args:
        val: The value to check.
        min_val: Minimum bound.
        max_val: Maximum bound.
        inclusive: If True, include bounds in comparison.

    Returns:
        True if within range, False otherwise.
    """
    if inclusive:
        return min_val <= val <= max_val
    return min_val < val < max_val


def validate_required_keys(data: Mapping[str, Any], required_keys: Sequence[str]) -> list[str]:
    """Find missing required keys in a dictionary-like structure.

    Args:
        data: The input mapping/dictionary to inspect.
        required_keys: A sequence of key names that must be present.

    Returns:
        A list of missing key names.
    """
    return [key for key in required_keys if key not in data]
