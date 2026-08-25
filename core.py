from typing import Any, Dict, List, Callable

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary to a single-level dict."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for i, item in enumerate(value):
                list_key = f"{new_key}[{i}]"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, value))
    return dict(items)

def unflatten_dict(flat_data: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    """Unflatten a flat dict to nested structure."""
    result: Dict[str, Any] = {}
    for key, value in flat_data.items():
        keys = key.split(sep)
        current = result
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        current[keys[-1]] = value
    return result

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any], deep: bool = True) -> Dict[str, Any]:
    """Recursively merge two dictionaries."""
    result = dict1.copy()
    for key, value in dict2.items():
        if deep and key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value, deep=True)
        else:
            result[key] = value
    return result

def safe_get(data: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """Get value from nested dict using path string."""
    keys = path.split(sep)
    current: Any = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def filter_by_keys(data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
    """Create dict filtered to include only given keys."""
    return {k: data.get(k) for k in keys if k in data}

def apply_to_values(data: Dict[str, Any], func: Callable[[Any], Any]) -> Dict[str, Any]:
    """Transform all non-dict values using provided function."""
    result: Dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result[key] = apply_to_values(value, func)
        else:
            result[key] = func(value)
    return result