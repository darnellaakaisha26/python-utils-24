"""General utility functions for data manipulation and safe casting."""

import re
from typing import Any, Dict, List, Optional


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries without altering inputs."""
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged and isinstance(merged[key], dict) and isinstance(value, dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def sanitize_string(text: str, allow_punctuation: bool = False) -> str:
    """Normalize whitespace and optionally strip special characters."""
    text = text.strip()
    if not allow_punctuation:
        text = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", text)


def safe_cast(value: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Attempt casting a value to a target type with fallback default."""
    try:
        return to_type(value)
    except (ValueError, TypeError):
        return default


def chunk_sequence(sequence: List[Any], size: int) -> List[List[Any]]:
    """Split a list sequence into chunks of specified maximum size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [sequence[i : i + size] for i in range(0, len(sequence), size)]
