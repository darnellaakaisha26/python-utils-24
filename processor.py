import json
import logging
from typing import Any, Dict, Optional

def sanitize_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Removes keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}

def safe_load_json(data: str) -> Optional[Dict[str, Any]]:
    """Parses JSON string safely returning None on failure."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return None

def chunk_list(items: list, size: int):
    """Yields successive chunks from a list."""
    for i in range(0, len(items), size):
        yield items[i:i + size]

def get_nested(data: Dict, path: str, default: Any = None) -> Any:
    """Accesses dictionary values using dot notation."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default

def format_byte_size(num: int) -> str:
    """Converts integer bytes to human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if num < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} TB"