import json
from typing import Any, Dict, Optional

def safe_load_json(file_path: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Safely loads a JSON file from the filesystem.
    Returns a default dictionary if file is missing or corrupt.
    """
    if default is None:
        default = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return default

def chunk_list(data: list, size: int):
    """
    Yields successive chunks from a list.
    Used for batch processing large datasets.
    """
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_dict(data: Dict[str, Any], keys_to_remove: list) -> Dict[str, Any]:
    """
    Removes sensitive or unnecessary keys from a dictionary.
    Returns a new dictionary with specified keys excluded.
    """
    return {k: v for k, v in data.items() if k not in keys_to_remove}
