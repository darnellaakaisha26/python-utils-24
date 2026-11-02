import json
from typing import Any, Dict, Optional

def safe_json_load(data: str, default: Optional[Dict] = None) -> Dict[str, Any]:
    """Parses a JSON string with a fallback default value."""
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default if default is not None else {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single depth dictionary."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_data(data: Dict[str, Any], keys_to_mask: Optional[list] = None) -> Dict[str, Any]:
    """Masks specific keys in a dictionary for logging security."""
    keys_to_mask = keys_to_mask or ['password', 'token', 'secret']
    return {
        k: ('***' if k in keys_to_mask else v)
        for k, v in data.items()
    }