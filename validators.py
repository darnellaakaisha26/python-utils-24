"""Validation utilities for general Python data structures and formats."""

import re
from typing import Any, Container, Dict, List, Optional, Union

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
URL_REGEX = re.compile(
    r"^(?:http|ftp)s?://"
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
    r"localhost|"
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


def is_valid_email(email: str) -> bool:
    """Validate if a string is a properly formatted email address.

    Args:
        email: The email string to validate.

    Returns:
        True if email format is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Check whether a given string is a valid HTTP/HTTPS or FTP URL.

    Args:
        url: The string URL to check.

    Returns:
        True if URL format is valid, False otherwise.
    """
    if not isinstance(url, str):
        return False
    return bool(URL_REGEX.match(url.strip()))


def validate_range(
    val: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Ensure a numerical value lies within specified bounds.

    Args:
        val: Numeric value to check.
        min_val: Optional lower bound (inclusive).
        max_val: Optional upper bound (inclusive).

    Returns:
        True if value falls within specified range, False otherwise.
    """
    if min_val is not None and val < min_val:
        return False
    if max_val is not None and val > max_val:
        return False
    return True


def validate_required_keys(
    data: Dict[str, Any], required_keys: Container[str]
) -> List[str]:
    """Find missing required keys in a dictionary.

    Args:
        data: Dictionary to check for keys.
        required_keys: Collection of keys that must be present.

    Returns:
        List of missing key names.
    """
    return [key for key in required_keys if key not in data]
