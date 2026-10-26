import json
from typing import Any, Dict, List, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Splits a list into smaller chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def safe_load_json(file_path: str) -> Optional[Dict[str, Any]]:
    """Safely loads and parses a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def retry_operation(func, retries: int = 3, *args, **kwargs) -> Any:
    """Executes a function with basic retry capability."""
    last_err = None
    for _ in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_err = e
    raise last_err