"""Data validation utility functions for python-utils-24."""

import re
from typing import Any, Dict, Iterable, Optional, Union

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
URL_REGEX = re.compile(
    r"^https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)$"
)


def is_valid_email(email: str) -> bool:
    """Validate whether the given string is a properly formatted email address.

    Args:
        email: The email string to check.

    Returns:
        True if the email string is valid, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))


def is_valid_url(url: str) -> bool:
    """Check if the provided string matches a standard HTTP/HTTPS URL pattern.

    Args:
        url: The web URL string to validate.

    Returns:
        True if the URL string is well-formed, False otherwise.
    """
    if not isinstance(url, str):
        return False
    return bool(URL_REGEX.match(url.strip()))


def validate_dict_keys(data: Dict[str, Any], required_keys: Iterable[str]) -> bool:
    """Verify that all required keys are present in the dictionary.

    Args:
        data: The target dictionary to inspect.
        required_keys: An iterable of key names that must exist.

    Returns:
        True if all required keys exist in data, False otherwise.
    """
    if not isinstance(data, dict):
        return False
    return all(key in data for key in required_keys)


def is_in_range(
    value: Union[int, float],
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
) -> bool:
    """Determine whether a numeric value lies within an optional min/max bound.

    Args:
        value: The number to test.
        min_val: Lower bound threshold (inclusive).
        max_val: Upper bound threshold (inclusive).

    Returns:
        True if value satisfies specified bounds, False otherwise.
    """
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True
