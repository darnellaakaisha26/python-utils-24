"""General utility helper functions for common data manipulation tasks."""

from typing import Any, Dict, Generator, List, Optional


def chunk_iterable(iterable: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i : i + chunk_size]


def safe_get(data: Dict[str, Any], path: str, default: Optional[Any] = None, delimiter: str = ".") -> Any:
    """Safely retrieve nested values from a dictionary using dot notation."""
    keys = path.split(delimiter)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a deeply nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def format_bytes(bytes_num: int) -> str:
    """Convert standard byte count into human-readable string format."""
    if bytes_num < 0:
        raise ValueError("bytes_num must be non-negative")
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(bytes_num)
    unit_index = 0
    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"
