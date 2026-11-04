import math
from typing import Any, Sequence


class ValidationError(ValueError):
    """Custom exception raised when validation parameters are invalid."""
    pass


def validate_numeric_range(
    value: Any,
    min_val: float | None = None,
    max_val: float | None = None,
) -> bool:
    """Validate if a value is a finite number within bounds with edge case checks."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False

    if math.isnan(value) or math.isinf(value):
        return False

    if min_val is not None and max_val is not None and min_val > max_val:
        raise ValidationError("min_val cannot be greater than max_val")

    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False

    return True


def validate_string_length(
    text: Any,
    min_len: int = 0,
    max_len: int | None = None,
    strip_whitespace: bool = True,
) -> bool:
    """Validate string length with edge case handling for non-strings and invalid bounds."""
    if not isinstance(text, str):
        return False

    if min_len < 0:
        raise ValidationError("min_len cannot be negative")
    if max_len is not None and max_len < min_len:
        raise ValidationError("max_len cannot be less than min_len")

    processed = text.strip() if strip_whitespace else text
    length = len(processed)

    if length < min_len:
        return False
    if max_len is not None and length > max_len:
        return False

    return True


def validate_required_keys(data: Any, required_keys: Sequence[Any]) -> bool:
    """Safely verify dictionary key presence, handling non-dict and unhashable inputs."""
    if not isinstance(data, dict):
        return False

    try:
        return all(key in data and data[key] is not None for key in required_keys)
    except TypeError:
        # Edge case: unhashable key provided in required_keys
        return False
