import json
import os
from typing import Any, Dict, List

def load_json(filepath: str) -> Dict[str, Any]:
    """Reads and parses a JSON file."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Any, filepath: str) -> None:
    """Serializes data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def slugify(text: str) -> str:
    """Converts strings to simple URL-safe slugs."""
    return "-".join(text.lower().split()).replace(" ", "-")

def get_env_var(key: str, default: str = "") -> str:
    """Fetches environment variable with fallback."""
    return os.getenv(key, default)

def safe_get(data: Dict, path: List[str], default: Any = None) -> Any:
    """Accesses deeply nested dictionary values."""
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current