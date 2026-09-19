import json
import os
from typing import Any, Dict, Optional

def load_json(filepath: str) -> Optional[Dict[str, Any]]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """Serialize data to a JSON file."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def ensure_dir(directory: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def get_env(key: str, default: Any = None) -> Any:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default)

def chunk_list(data: list, size: int):
    """Split list into smaller chunks of fixed size."""
    for i in range(0, len(data), size):
        yield data[i:i + size]