import json
from typing import Any, Dict, List, Optional
from pathlib import Path

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Load and parse a JSON file safely."""
    path = Path(file_path)
    if not path.exists():
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None

def chunk_list(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of fixed size."""
    if chunk_size <= 0:
        return [data]
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary using dot notation keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def format_byte_size(size_bytes: int) -> str:
    """Convert byte integer to human-readable string."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"