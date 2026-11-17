import json
from typing import Any, Dict, Optional

def safe_json_load(file_path: str) -> Dict[str, Any]:
    """Loads and parses a JSON file with basic error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single-level structure."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Any) -> Any:
    """Recursively cleans None values from a collection."""
    if isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items() if v is not None}
    elif isinstance(data, list):
        return [sanitize_data(x) for x in data if x is not None]
    return data