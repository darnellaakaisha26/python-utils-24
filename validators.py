"""Validation utility functions for common data types and structures."""

import re
from typing import Any, Mapping, Optional, Sequence, Tuple


EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
URL_REGEX = re.compile(r"^https?://[^\s/$.?#].[^\s]*$", re.IGNORECASE)


def is_valid_email(email: str) -> bool:
    """Check if a given string is a valid email address format.

    Args:
        email: The string to validate as an email address.

    Returns:
        True if valid email format, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Validate whether a string is a properly formatted HTTP/HTTPS URL.

    Args:
        url: The string to validate as a URL.

    Returns:
        True if valid URL format, False otherwise.
    """
    if not isinstance(url, str):
        return False
    return bool(URL_REGEX.match(url.strip()))


def validate_range(
    val: float,
    min_val: Optional[float] = None,
    max_val: Optional[float] = None
) -> bool:
    """Determine if a numeric value falls within a specified range.

    Args:
        val: Numeric value to test.
        min_val: Lower limit (inclusive), if provided.
        max_val: Upper limit (inclusive), if provided.

    Returns:
        True if value meets range criteria, False otherwise.
    """
    if min_val is not None and val < min_val:
        return False
    if max_val is not None and val > max_val:
        return False
    return True


def validate_schema(data: Mapping[str, Any], required_keys: Sequence[str]) -> Tuple[bool, Optional[str]]:
    """Verify that a dictionary contains all required keys.

    Args:
        data: The dictionary mapping to inspect.
        required_keys: A sequence of required key names.

    Returns:
        Tuple of (is_valid, missing_key_name_or_none).
    """
    for key in required_keys:
        if key not in data:
            return False, key
    return True, None