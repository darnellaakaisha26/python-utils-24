import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common string and data validations."""

    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def is_valid_email(email: Any) -> bool:
        """Verify email format using regex pattern."""
        if not isinstance(email, str):
            return False
        return bool(DataValidator.EMAIL_PATTERN.match(email))

    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int) -> bool:
        """Ensure integer is within specified boundaries."""
        return min_val <= value <= max_val

    @staticmethod
    def ensure_not_empty(data: Optional[str]) -> bool:
        """Check if string is not None and not whitespace only."""
        return data is not None and len(data.strip()) > 0

    @classmethod
    def validate_payload(cls, data: dict, required_keys: list) -> bool:
        """Verify presence of mandatory keys in dictionary."""
        return all(key in data for key in required_keys)