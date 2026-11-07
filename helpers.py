import os
import json
from typing import Any, Optional

def read_json(file_path: str) -> dict:
    """Load and parse a JSON file safely."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: dict, file_path: str) -> None:
    """Serialize dictionary to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_env_variable(key: str, default: Any = None) -> Optional[Any]:
    """Retrieve environment variable with fallback."""
    return os.environ.get(key, default)

def chunk_list(data: list, size: int) -> list:
    """Divide a list into smaller chunks."""
    return [data[i:i + size] for i in range(0, len(data), size)]

def sanitize_filename(name: str) -> str:
    """Remove invalid characters from filenames."""
    forbidden = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in forbidden:
        name = name.replace(char, '_')
    return name.strip()