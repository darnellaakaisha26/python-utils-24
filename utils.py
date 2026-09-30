from typing import List, Any, Optional, Dict
import json

def format_data(data: List[Any], prefix: str = "") -> str:
    """Convert list to a formatted string representation with prefix."""
    items = ", ".join(str(item) for item in data)
    return f"{prefix}{items}"

def parse_json(raw_input: str) -> Optional[Dict[str, Any]]:
    """Safe parsing of JSON strings into dictionary objects."""
    try:
        return json.loads(raw_input)
    except (json.JSONDecodeError, TypeError):
        return None

def get_unique_elements(items: List[Any]) -> List[Any]:
    """Return a list of unique items preserving insertion order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    """Split a list into smaller chunks of a fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    return [data[i:i + size] for i in range(0, len(data), size)]