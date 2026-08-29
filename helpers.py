import json
from typing import Any, Dict, List, Union

def get_nested_value(data: Dict[str, Any], path: str, default: Any = None, separator: str = '.') -> Any:
    """Retrieve value from nested dict using dot-separated path."""
    if not isinstance(data, dict):
        return default
    keys = path.split(separator)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def flatten_dict(nested: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested dictionary into single level with separator."""
    items: List[tuple] = []
    for k, v in nested.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def deep_merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, override takes precedence."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def safe_json_parse(data: Union[str, bytes, bytearray], default: Any = None) -> Any:
    """Parse JSON safely, return default on error."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError, ValueError):
        return default

def chunk_data(data: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of given size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def filter_none(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys with None values from dictionary."""
    return {k: v for k, v in data.items() if v is not None}