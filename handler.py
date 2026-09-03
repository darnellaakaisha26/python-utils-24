import json
from typing import Any, Dict, Optional, Union

def sanitize_data(data: Any, default: Any = None) -> Any:
    """
    Recursively cleans input data to ensure dictionary keys are strings
    and handles basic serialization for non-serializable objects.
    """
    if isinstance(data, dict):
        return {str(k): sanitize_data(v, default) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i, default) for i in data]
    if isinstance(data, (str, int, float, bool, type(None))):
        return data
    return str(data)

def safe_load_json(file_path: str) -> Dict[str, Any]:
    """
    Reads a file and attempts to parse it as JSON.
    Returns an empty dictionary if file does not exist or parse fails.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError):
        return {}

def process_payload(payload: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Unified interface to parse input and sanitize fields.
    """
    if isinstance(payload, str):
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = {}
    else:
        data = payload
    
    return sanitize_data(data) if isinstance(data, dict) else {}