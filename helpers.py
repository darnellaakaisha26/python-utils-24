"""General purpose helper utilities for common data manipulation tasks."""

from typing import Any, Dict, List, TypeVar, Optional, Generator

T = TypeVar("T")


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested dictionary with custom key separator."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def chunk_list(data: List[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Yield successive chunks of specified size from a list."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge dict2 into dict1 without mutating inputs."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def safe_cast(val: Any, to_type: type, default: Optional[Any] = None) -> Any:
    """Safely cast a value to a target type, returning default on failure."""
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
