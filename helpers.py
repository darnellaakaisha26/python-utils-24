"""General utility helper functions for data manipulation and formatting."""

from typing import Any, Dict, Iterable, List, TypeVar, Optional
import re

T = TypeVar('T')


def safe_cast(value: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Safely cast a value to a target type with a fallback default."""
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries into a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> List[List[T]]:
    """Split an iterable into uniform chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    items = list(iterable)
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def sanitize_string(text: str, allow_alphanumeric_only: bool = False) -> str:
    """Clean whitespace and optionally remove non-alphanumeric characters."""
    cleaned = " ".join(text.strip().split())
    if allow_alphanumeric_only:
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned)
    return cleaned
