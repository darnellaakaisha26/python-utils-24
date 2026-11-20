import os
import json
from typing import Any, Dict

def read_json(filepath: str) -> Dict[str, Any]:
    """Loads and parses a JSON file from disk."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: Dict[str, Any], filepath: str) -> None:
    """Saves a dictionary as a formatted JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def ensure_dir(path: str) -> None:
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Any = None) -> Any:
    """Retrieves environment variable with fallback default."""
    return os.environ.get(key, default)