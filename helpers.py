"""General helper utilities for common Python data structures and operations."""

import re
from typing import Any, Dict, Generator, Iterable, List, Optional, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Iterable[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    
    chunk: List[T] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def deep_merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries without mutating the inputs."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result


def safe_cast(val: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def slugify(text: str) -> str:
    """Normalize string, remove non-alphanumeric chars, and convert spaces to hyphens."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)
