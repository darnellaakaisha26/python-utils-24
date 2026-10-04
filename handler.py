from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    """
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Any, allowed_types: Optional[tuple] = None) -> Any:
    """
    Recursively removes non-serializable objects from input data.
    """
    if allowed_types is None:
        allowed_types = (str, int, float, bool, type(None), list, dict)

    if isinstance(data, dict):
        return {str(k): sanitize_data(v, allowed_types) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i, allowed_types) for i in data]
    
    return data if isinstance(data, allowed_types) else str(data)

def batch_process(data: List[Any], chunk_size: int = 10):
    """
    Generator yielding chunks of a list.
    """
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]