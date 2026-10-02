import ipaddress
import re
from urllib.parse import urlparse

# Regular expression for a standard email format
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_email(email: str) -> bool:
    """Check if the provided string is a valid email address."""
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_url(url: str) -> bool:
    """Verify if a string is a well-formed HTTP/HTTPS URL."""
    if not url or not isinstance(url, str):
        return False
    try:
        result = urlparse(url)
        return all([result.scheme in ("http", "https"), result.netloc])
    except ValueError:
        return False


def is_valid_ip(ip_str: str) -> bool:
    """Validate if the string is a valid IPv4 or IPv6 address."""
    if not ip_str or not isinstance(ip_str, str):
        return False
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False


def is_strong_password(password: str, min_length: int = 8) -> bool:
    """Check if password meets basic strength requirements.

    Requires at least one uppercase letter, one lowercase letter,
    one digit, and one special character.
    """
    if not password or len(password) < min_length:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return all([has_upper, has_lower, has_digit, has_special])
