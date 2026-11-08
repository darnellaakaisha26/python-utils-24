from typing import Any, Dict, List


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with delimited keys."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def get_nested(d: Dict[str, Any], path: str, default: Any = None, sep: str = ".") -> Any:
    """Safely retrieve a value from a nested dictionary using a dot-separated path."""
    keys = path.split(sep)
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def set_nested(d: Dict[str, Any], path: str, value: Any, sep: str = ".") -> None:
    """Set a value in a nested dictionary using a path, building parent structures if missing."""
    keys = path.split(sep)
    current = d
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value
