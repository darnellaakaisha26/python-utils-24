"""Validation utility functions with resilient edge case handling."""

from typing import Any, Dict, Optional, Sequence, Union


class ValidationError(ValueError):
    """Custom exception raised when data validation fails."""
    pass


def validate_numeric_range(
    val: Any,
    min_val: Optional[Union[int, float]] = None,
    max_val: Optional[Union[int, float]] = None,
    allow_none: bool = False
) -> float:
    """Validate if a value is numeric and falls within specified bounds."""
    if val is None:
        if allow_none:
            return 0.0
        raise ValidationError("Value cannot be None")

    try:
        num = float(val)
    except (ValueError, TypeError) as err:
        raise ValidationError(f"Invalid numeric input '{val}': {err}") from err

    if min_val is not None and num < min_val:
        raise ValidationError(f"Value {num} is below minimum allowed ({min_val})")
    if max_val is not None and num > max_val:
        raise ValidationError(f"Value {num} exceeds maximum allowed ({max_val})")

    return num


def validate_dict_structure(
    data: Any,
    required_keys: Sequence[str],
    allowed_types: Optional[Dict[str, type]] = None
) -> Dict[str, Any]:
    """Validate structure and key data types of a dictionary."""
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, received {type(data).__name__}")

    missing = [key for key in required_keys if key not in data]
    if missing:
        raise ValidationError(f"Missing required keys: {', '.join(missing)}")

    if allowed_types:
        for key, expected_type in allowed_types.items():
            if key in data and data[key] is not None:
                if not isinstance(data[key], expected_type):
                    actual_type = type(data[key]).__name__
                    raise ValidationError(
                        f"Key '{key}' expected {expected_type.__name__}, got {actual_type}"
                    )

    return data
