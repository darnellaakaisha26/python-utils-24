"""Module providing helper functions for common operations."""
import json
import time
from datetime import datetime
from typing import Any, Dict, List, Optional, Callable

def safe_divide(a: float, b: float) -> Optional[float]:
    """Divide two numbers safely, returning None on zero divisor."""
    if b == 0:
        return None
    return a / b

def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list of lists into one list."""
    return [item for sublist in nested_list for item in sublist]

def get_nested_value(data: Dict[str, Any], path: List[str]) -> Any:
    """Retrieve value from nested dict using key path list."""
    current = data
    for key in path:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current

def format_timestamp(timestamp: float, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Convert timestamp to formatted datetime string."""
    return datetime.fromtimestamp(timestamp).strftime(fmt)

def chunk_list(items: List[Any], size: int) -> List[List[Any]]:
    """Split list into smaller chunks of specified size."""
    if size <= 0:
        return [items]
    return [items[i:i + size] for i in range(0, len(items), size)]

def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dicts with override taking precedence."""
    result = base.copy()
    result.update(override)
    return result

def basic_email_check(email: str) -> bool:
    """Check if string looks like a basic email address."""
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and "." in parts[1]

def read_json_safely(filepath: str) -> Optional[Dict[str, Any]]:
    """Read JSON file and return dict or None on error."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError, TypeError):
        return None

def write_json_safely(filepath: str, data: Dict[str, Any]) -> bool:
    """Write dict to JSON file, return success status."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        return True
    except (OSError, TypeError):
        return False

def retry_call(func: Callable[[], Any], retries: int = 3, delay: float = 0.5) -> Any:
    """Retry function call on exception up to retries times."""
    for attempt in range(retries):
        try:
            return func()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(delay)
    return None
