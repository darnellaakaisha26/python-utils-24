from typing import Any, Dict, List, Optional

def validate_schema(data: Dict[str, Any], schema: Dict[str, type]) -> List[str]:
    """Validate dictionary keys and value types against a schema."""
    errors = []
    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"missing required key: {key}")
        elif not isinstance(data[key], expected_type):
            errors.append(f"invalid type for {key}: expected {expected_type.__name__}")
    return errors

def sanitize_input(data: Any, default: Any = None) -> Any:
    """Return stripped string or default if input is empty or None."""
    if isinstance(data, str):
        clean = data.strip()
        return clean if clean else default
    return data if data is not None else default

def check_list_types(items: List[Any], element_type: type) -> bool:
    """Verify all elements in a list match a specific type."""
    if not isinstance(items, list):
        return False
    return all(isinstance(item, element_type) for item in items)

def enforce_range(value: int, min_val: int, max_val: int) -> int:
    """Constrain numeric value within defined inclusive bounds."""
    return max(min_val, min(value, max_val))