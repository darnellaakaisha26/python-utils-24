import datetime
import hashlib
import re
from typing import Any, Dict, List

def get_current_timestamp() -> str:
    """Return current UTC timestamp in ISO format."""
    return datetime.datetime.utcnow().isoformat() + 'Z'

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Divide numerator by denominator safely returning default on zero."""
    if denominator == 0:
        return default
    return numerator / denominator

def merge_dicts(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, override takes precedence."""
    result = dict(base)
    result.update(override)
    return result

def remove_duplicates(items: List[Any]) -> List[Any]:
    """Remove duplicate values preserving original order."""
    seen = set()
    result: List[Any] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def is_valid_email(email: str) -> bool:
    """Validate if the provided string is a valid email address."""
    if not isinstance(email, str) or not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def truncate_string(text: str, max_length: int, suffix: str = '...') -> str:
    """Truncate the string if it exceeds max length."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def split_into_chunks(data: List[Any], chunk_size: int) -> List[List[Any]]:
    """Divide list into smaller chunks of specified size."""
    if chunk_size <= 0:
        return []
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def compute_hash(value: str, algorithm: str = 'sha256') -> str:
    """Generate a hash of the string value."""
    if algorithm not in hashlib.algorithms_guaranteed:
        algorithm = 'sha256'
    hasher = hashlib.new(algorithm)
    hasher.update(value.encode('utf-8'))
    return hasher.hexdigest()

def get_common_items(a: List[Any], b: List[Any]) -> List[Any]:
    """Find items present in both lists, order from first."""
    set_b = set(b)
    return [item for item in a if item in set_b]