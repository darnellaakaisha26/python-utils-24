import json
from typing import Any, Optional, Dict

def safe_json_load(data: str, default: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parses JSON string into dictionary with fallback support."""
    try:
        return json.loads(data) if data else (default or {})
    except (json.JSONDecodeError, TypeError):
        return default or {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionary structure using separator."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_by_keys(data: Dict[str, Any], keys: list) -> Dict[str, Any]:
    """Filters dictionary keys based on allowlist."""
    return {k: v for k, v in data.items() if k in keys}

def format_data_payload(data: Any) -> str:
    """Standardizes data into a string format."""
    if isinstance(data, (dict, list)):
        return json.dumps(data, indent=4)
    return str(data)