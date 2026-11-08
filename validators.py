"""
Data validation utilities for general structure and type checking.
"""

from typing import Any, Dict, List, Optional, Type, Union


class ValidationError(Exception):
    """Raised when data structure validation fails."""
    pass


def validate_dict(
    data: Any,
    schema: Dict[str, Union[Type, tuple, Dict[str, Any]]],
    required_keys: Optional[List[str]] = None,
    allow_extra_keys: bool = True
) -> bool:
    """
    Validate a dictionary against a given schema of expected types or nested schemas.

    Args:
        data: The input dictionary to validate.
        schema: Mapping of key names to expected types or nested schema dicts.
        required_keys: Optional list of keys that must be present in data.
        allow_extra_keys: If False, raises error when unknown keys are present.

    Returns:
        bool: True if validation passes.

    Raises:
        ValidationError: If validation fails.
    """
    if not isinstance(data, dict):
        raise ValidationError(f"Expected dict, got {type(data).__name__}")

    if required_keys:
        missing = [key for key in required_keys if key not in data]
        if missing:
            raise ValidationError(f"Missing required keys: {', '.join(missing)}")

    if not allow_extra_keys:
        extra = [key for key in data if key not in schema]
        if extra:
            raise ValidationError(f"Unexpected extra keys: {', '.join(extra)}")

    for key, expected_type in schema.items():
        if key not in data:
            continue

        value = data[key]
        if isinstance(expected_type, dict):
            validate_dict(value, expected_type, allow_extra_keys=allow_extra_keys)
        elif not isinstance(value, expected_type):
            expected_name = (
                tuple(t.__name__ for t in expected_type)
                if isinstance(expected_type, tuple)
                else expected_type.__name__
            )
            raise ValidationError(
                f"Key '{key}' expected type {expected_name}, got {type(value).__name__}"
            )

    return True