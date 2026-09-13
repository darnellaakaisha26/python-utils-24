import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Reads and parses a JSON file into a dictionary."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """Serializes a dictionary to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks of specific size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with optional default fallback."""
    return os.environ.get(key, default or "")