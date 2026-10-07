import re
from typing import Any, Optional

class DataValidator:
    """Utility class for common data structure validation."""

    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    @staticmethod
    def is_email(value: Any) -> bool:
        """Check if input is a valid email string."""
        if not isinstance(value, str):
            return False
        return bool(DataValidator.EMAIL_PATTERN.match(value))

    @staticmethod
    def is_non_empty_string(value: Any) -> bool:
        """Verify string existence and content."""
        return isinstance(value, str) and len(value.strip()) > 0

    @staticmethod
    def is_valid_port(value: Any) -> bool:
        """Ensure integer is a valid network port."""
        try:
            port = int(value)
            return 1 <= port <= 65535
        except (ValueError, TypeError):
            return False

def validate_schema(data: dict, schema: dict) -> bool:
    """Deep schema check for dictionary inputs."""
    for key, validator_func in schema.items():
        if key not in data:
            return False
        if not validator_func(data[key]):
            return False
    return True