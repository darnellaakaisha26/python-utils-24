from typing import Dict, Any, Mapping

def flatten_dict(target: Mapping[str, Any], sep: str = '_', parent_key: str = '') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary structure.

    Args:
        target: The dictionary to flatten.
        sep: The separator to use between keys.
        parent_key: The accumulated parent key string.
    """
    flat_dict = {}
    for key, val in target.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(val, dict):
            flat_dict.update(flatten_dict(val, sep=sep, parent_key=new_key))
        else:
            flat_dict[new_key] = val
    return flat_dict

def unflatten_dict(target: Mapping[str, Any], sep: str = '_') -> Dict[str, Any]:
    """
    Reconstructs a nested dictionary from a flattened dictionary.

    Args:
        target: The flattened dictionary to expand.
        sep: The separator used in the keys.
    """
    nested_dict: Dict[str, Any] = {}
    for key, val in target.items():
        parts = key.split(sep)
        cursor = nested_dict
        for part in parts[:-1]:
            if part not in cursor or not isinstance(cursor[part], dict):
                cursor[part] = {}
            cursor = cursor[part]
        cursor[parts[-1]] = val
    return nested_dict
