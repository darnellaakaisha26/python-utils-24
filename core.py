import json
import os
from typing import Any, Dict, List, Optional

def read_json(filepath: str) -> Dict[str, Any]:
    """Load and parse JSON file contents."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(filepath: str, data: Dict[str, Any]) -> None:
    """Serialize data to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """Convert nested lists into a single flat list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_iterable(items: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of specific size."""
    return [items[i:i + size] for i in range(0, len(items), size)]

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with default fallback."""
    return os.environ.get(key, default) or ''