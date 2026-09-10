from typing import Any, Dict, List, Optional
import json

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Useful for processing configuration files or API responses.
    """
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def safe_json_load(content: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Attempts to parse JSON string, returning a default dict on failure.
    """
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return default or {}

def sanitize_keys(data: Dict[str, Any], prefix: str = 'clean_') -> Dict[str, Any]:
    """
    Appends a prefix to keys in a dictionary for data safety.
    """
    return {f"{prefix}{k}": v for k, v in data.items()}
