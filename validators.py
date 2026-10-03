import re
from typing import Union, Any
from urllib.parse import urlparse

# Regular expression for a standard email format validation
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\$")


def is_valid_email(email: Any) -> bool:
    """Validate if the provided value is a syntactically correct email address.

    Args:
        email: The input to validate. Usually a string.

    Returns:
        True if the input is a valid email string, False otherwise.
    """
    if not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email))


def is_valid_url(url: Any) -> bool:
    """Verify if a given string is a properly formatted URL.

    Args:
        url: The input string to check.

    Returns:
        True if the input is a valid HTTP/HTTPS URL, False otherwise.
    """
    if not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url)
        return all([parsed.scheme in ("http", "https"), parsed.netloc])
    except Exception:
        return False


def validate_numeric_range(
    value: Union[int, float],
    min_value: Union[int, float],
    max_value: Union[int, float],
) -> bool:
    """Check if a numeric value falls within a specified inclusive range.

    Args:
        value: The number to validate.
        min_value: The lower bound of the range.
        max_value: The upper bound of the range.

    Returns:
        True if value is between min_value and max_value inclusive, False otherwise.

    Raises:
        ValueError: If min_value is greater than max_value.
    """
    if min_value > max_value:
        raise ValueError("Minimum value cannot be greater than maximum value.")
    return min_value <= value <= max_value
