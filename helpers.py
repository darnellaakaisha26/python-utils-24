import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data: Dict[str, Any], filepath: str) -> bool:
    """Serialize data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError):
        return False

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Fetch environment variable with default fallback."""
    return os.environ.get(key, default or '')

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def slugify(text: str) -> str:
    """Normalize string to filesystem-safe slug."""
    return "-".join(text.lower().split()).replace(" ", "-")
