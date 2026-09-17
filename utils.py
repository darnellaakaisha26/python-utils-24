from typing import Dict, Any, Generator, List

def deep_merge(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merges dict2 into dict1, returning a new dictionary."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def chunk_list(items: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yields successive chunks of a specified size from the input list."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flattens a nested dictionary, prefixing keys with parent keys separated by 'sep'."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def safe_get(d: Dict[str, Any], key_path: str, default: Any = None, sep: str = '.') -> Any:
    """Retrieves a nested key from a dictionary using a dot-separated string path."""
    keys = key_path.split(sep)
    current: Any = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current