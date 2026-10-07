import os
import json
import logging
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[Any, Any]:
    """Reads and parses a JSON file from disk."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(file_path: str, data: Dict[Any, Any]) -> bool:
    """Serializes data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        logging.error(f"Failed to write json: {e}")
        return False

def ensure_dir(path: str) -> None:
    """Creates directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.getenv(key, default or "")

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