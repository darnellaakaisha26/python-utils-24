from typing import Any, Dict, List


def flatten_dict(
    data: Dict[str, Any],
    parent_key: str = "",
    sep: str = "."
) -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def unflatten_dict(
    data: Dict[str, Any],
    sep: str = "."
) -> Dict[str, Any]:
    """Reconstruct a nested dictionary from a flattened single-level dictionary."""
    result: Dict[str, Any] = {}
    for key, value in data.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current or not isinstance(current[part], dict):
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def chunk_iterable(items: List[Any], size: int) -> List[List[Any]]:
    """Split a sequence into uniform chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    return [items[i:i + size] for i in range(0, len(items), size)]
