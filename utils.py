from typing import Any, Iterable, Dict, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten nested dictionaries into a single-level dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: Iterable[Any], size: int) -> Iterable[Any]:
    """Split a sequence into smaller chunks of fixed size."""
    it = iter(data)
    return iter(lambda: list(islice(it, size)), [])

def clean_data(data: Dict[str, Any], keys_to_remove: Optional[list] = None) -> Dict[str, Any]:
    """Remove specified keys from a dictionary if present."""
    if not keys_to_remove:
        return data.copy()
    return {k: v for k, v in data.items() if k not in keys_to_remove}

from itertools import islice