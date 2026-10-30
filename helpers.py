"""General helper functions for data manipulation, formatting, and safety checks."""

import re
from typing import Any, Dict, List, Optional


def flatten_dict(
    data: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary with custom delimiter."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def truncate_text(
    text: str, max_length: int = 100, suffix: str = "..."
) -> str:
    """Safely truncate text to specified length with suffix."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)].rstrip() + suffix


def sanitize_slug(text: str) -> str:
    """Convert text into a clean URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller fixed-size chunks."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]


def safe_get(
    dictionary: Dict[str, Any], keys: List[str], default: Optional[Any] = None
) -> Any:
    """Safely retrieve a deeply nested dictionary value using a list of keys."""
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current