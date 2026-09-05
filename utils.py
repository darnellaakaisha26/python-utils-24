from typing import Any, Dict, List, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten nested dictionary into single level."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split list into smaller chunks of fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i:i + size] for i in range(0, len(data), size)]

def clean_data(data: Any, default: Any = None) -> Any:
    """Return data if not None, otherwise return default."""
    return data if data is not None else default

def parse_bool(value: Any) -> bool:
    """Coerce input value to boolean."""
    if isinstance(value, str):
        return value.lower() in ("yes", "true", "t", "1")
    return bool(value)