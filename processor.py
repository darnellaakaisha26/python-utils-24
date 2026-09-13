import json
import os
from typing import Any, Dict, Optional

def read_json_file(filepath: str) -> Dict[str, Any]:
    """Loads data from a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def write_json_file(filepath: str, data: Dict[str, Any]) -> bool:
    """Saves dictionary to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def slugify(text: str) -> str:
    """Converts string to a URL-friendly format."""
    return "-".join(text.lower().split()).replace(" ", "-")

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Retrieves environment variable with fallback."""
    return os.environ.get(key, default or "")

def chunk_list(data: list, size: int):
    """Splits a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]