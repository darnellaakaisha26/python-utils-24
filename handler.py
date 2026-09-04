import json
from typing import Any, Dict, Optional

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """Loads and parses a JSON file with error handling."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Data loading error in {file_path}: {e}")
        return {}

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Dict[str, Any], keys_to_remove: list) -> Dict[str, Any]:
    """Removes sensitive or unwanted keys from a dictionary."""
    return {k: v for k, v in data.items() if k not in keys_to_remove}

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieves value from nested dict using dot notation path."""
    keys = path.split('.')
    val = data
    try:
        for key in keys:
            val = val[key]
        return val
    except (KeyError, TypeError):
        return default