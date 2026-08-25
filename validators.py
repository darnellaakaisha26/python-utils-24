"""Validators for common data types in python-utils-24.
Practical functions with type hints for input validation.
"""
import re
from typing import Any, List, Tuple

def validate_email(email: str) -> bool:
    """Check if provided string is a valid email address.
    Uses simple regex to match standard email format.
    Args:
        email: The candidate email address.
    Returns:
        True when matches pattern else False.
    """
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_url(url: str) -> bool:
    """Check if provided string is a valid http or https URL.
    Requires protocol and basic domain structure.
    Args:
        url: The candidate URL.
    Returns:
        True when matches pattern else False.
    """
    if not isinstance(url, str):
        return False
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/.*)?$'
    return bool(re.match(pattern, url.lower()))

def validate_phone(phone: str) -> bool:
    """Check if provided string resembles a phone number.
    Allows optional leading + and 7 to 15 digits after cleaning.
    Args:
        phone: The candidate phone number.
    Returns:
        True when matches pattern else False.
    """
    if not isinstance(phone, str):
        return False
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    pattern = r'^\+?\d{7,15}$'
    return bool(re.match(pattern, cleaned))

def validate_password(password: str, min_length: int = 8) -> Tuple[bool, str]:
    """Validate password meets minimum security criteria.
    Requires length, digit and alphabetic character.
    Args:
        password: The password to check.
        min_length: Minimum characters, default 8.
    Returns:
        Tuple with validity bool and explanatory string.
    """
    if not isinstance(password, str):
        return False, "Password must be a string"
    if len(password) < min_length:
        return False, f"Password must have at least {min_length} characters"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a digit"
    if not any(c.isalpha() for c in password):
        return False, "Password must contain a letter"
    return True, "Valid password"