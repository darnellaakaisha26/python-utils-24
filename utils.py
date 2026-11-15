"""General utility functions with robust edge-case handling."""

from typing import Any, Optional, Type, TypeVar

T = TypeVar("T")


def safe_get(data: Any, path: str, default: Any = None, delimiter: str = ".") -> Any:
    """Retrieve nested object or dict values safely using a delimited path string.

    Handles non-dict structures, index bounds, and invalid path inputs cleanly.
    """
    if not isinstance(path, str) or not path:
        return default

    keys = path.split(delimiter)
    current = data

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(key)
                if 0 <= idx < len(current):
                    current = current[idx]
                else:
                    return default
            except (ValueError, TypeError):
                return default
        else:
            return default

        if current is default:
            break

    return current


def safe_cast(val: Any, target_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    """Safely cast a value to a target type with default fallback on failure."""
    if val is None:
        return default
    try:
        return target_type(val)
    except (ValueError, TypeError, OverflowError):
        return default


def clamp(val: Any, min_val: Optional[float] = None, max_val: Optional[float] = None) -> float:
    """Clamp a numeric value between bounds, resolving type conflicts safely."""
    num = safe_cast(val, float, default=0.0)
    if num is None:
        num = 0.0

    if min_val is not None:
        min_num = safe_cast(min_val, float)
        if min_num is not None and num < min_num:
            num = min_num

    if max_val is not None:
        max_num = safe_cast(max_val, float)
        if max_num is not None and num > max_num:
            num = max_num

    return num
