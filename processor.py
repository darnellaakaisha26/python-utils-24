import collections.abc
from typing import Any, Dict, List, Union

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Uses dot notation for keys to maintain structural context.
    """
    items: List[tuple] = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_by_keys(data: Dict[str, Any], keys: List[str], exclude: bool = False) -> Dict[str, Any]:
    """
    Filters dictionary entries based on a list of keys.
    Supports both inclusive and exclusive filtering modes.
    """
    if exclude:
        return {k: v for k, v in data.items() if k not in keys}
    return {k: v for k, v in data.items() if k in keys}

def normalize_data(data: Union[List, Dict]) -> Union[List, Dict]:
    """
    Deep copies and ensures standard data structures.
    Converts common non-serializable iterables to lists.
    """
    if isinstance(data, dict):
        return {k: normalize_data(v) for k, v in data.items()}
    elif isinstance(data, (list, tuple, set)):
        return [normalize_data(item) for item in data]
    return data