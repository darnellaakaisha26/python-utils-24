import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


def safe_convert_to_int(
    val: Any, default: Optional[int] = None
) -> Optional[int]:
    """Safely convert a value to an integer, handling edge cases."""
    if val is None:
        return default
    try:
        if isinstance(val, str) and "." in val:
            return int(float(val))
        return int(val)
    except (ValueError, TypeError) as e:
        logger.warning(
            f"Failed to convert {val} of type {type(val)} to int: {e}"
        )
        return default


def get_nested_value(
    data: Dict[str, Any], path: str, default: Any = None
) -> Any:
    """Retrieve a nested value from a dictionary using dot notation."""
    if not isinstance(data, dict):
        return default
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current
