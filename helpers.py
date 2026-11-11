"""General helper utilities for data structures and text formatting."""

from typing import Any, Dict, List, TypeVar

T = TypeVar("T")


def safe_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Safely extract nested values from a dictionary using dot-notation.

    Example: safe_get({'a': {'b': 1}}, 'a.b') -> 1
    """
    keys = path.split(".")
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to a maximum length, appending suffix if truncated."""
    if max_length <= 0:
        raise ValueError("max_length must be greater than 0")
    if len(text) <= max_length:
        return text

    adjusted_len = max(1, max_length - len(suffix))
    return text[:adjusted_len] + suffix


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, giving priority to dict2 values."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
