import json
import os
import time
from typing import Any, Dict, Optional

def read_json(filepath: str) -> Dict[str, Any]:
    """Load and parse a JSON file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(data: Dict[str, Any], filepath: str) -> None:
    """Write data to a JSON file with indentation."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def format_timestamp(timestamp: Optional[float] = None) -> str:
    """Convert epoch time to a readable string format."""
    t = timestamp or time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))

def chunk_list(data: list, size: int):
    """Split a list into smaller chunks."""
    for i in range(0, len(data), size):
        yield data[i:i + size]

def ensure_dir(directory: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)