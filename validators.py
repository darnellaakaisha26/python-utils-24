import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common string and data validations."""
    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Checks if the provided string is a valid email format."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_REGEX.match(email))

    @staticmethod
    def is_not_empty(value: Any) -> bool:
        """Verifies that the value is not None or empty."""
        if value is None:
            return False
        if isinstance(value, (str, list, dict, set)):
            return len(value) > 0
        return True

    @classmethod
    def validate_length(cls, value: str, min_len: int, max_len: Optional[int] = None) -> bool:
        """Checks if string length is within specified boundaries."""
        if not isinstance(value, str):
            return False
        length = len(value)
        if max_len is not None:
            return min_len <= length <= max_len
        return length >= min_len

    @staticmethod
    def sanitize_input(value: str) -> str:
        """Removes leading/trailing whitespace and control characters."""
        if not isinstance(value, str):
            return ""
        return value.strip().replace('\n', '').replace('\r', '')