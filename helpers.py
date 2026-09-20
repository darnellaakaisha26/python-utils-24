from typing import Any, Iterable, Dict, List, Optional

def chunk_data(data: Iterable[Any], chunk_size: int) -> List[List[Any]]:
    """Split an iterable into fixed-size chunks for batch processing."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")
    
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def deep_get(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """Access nested dictionary values using dot-notation keys."""
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data

def filter_none(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove keys with None values from a dictionary."""
    return {k: v for k, v in data.items() if v is not None}