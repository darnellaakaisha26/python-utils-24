"""General utility helper functions for object and string manipulation."""

from typing import Any, Dict, List, Optional


def flatten_dict(
    nested_dict: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into single-level key-value pairs."""
    items: List[tuple] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def safe_cast(
    value: Any, target_type: type, default: Optional[Any] = None
) -> Any:
    """Safely convert a value to a target type without raising exceptions."""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default


def truncate_string(text: str, max_length: int = 50, suffix: str = "...") -> str:
    """Truncate string to maximum length and append suffix if shortened."""
    if not text or len(text) <= max_length:
        return text
    adjusted_length = max(0, max_length - len(suffix))
    return text[:adjusted_length] + suffix


def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller fixed-size chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    return [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]
