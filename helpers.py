import json
import os
from typing import Any, Dict, Optional

def load_json_file(file_path: str) -> Dict[str, Any]:
    """Load and parse a JSON configuration file."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def ensure_directory(dir_path: str) -> None:
    """Create directory path if it does not exist."""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary with concatenated keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Retrieve environment variable with fallback default."""
    return os.environ.get(key, default or '')