from typing import Any, Dict, List, Optional

def validate_input_schema(data: Any, required_fields: List[str]) -> bool:
    """Validates that input is a dictionary and contains required keys."""
    if not isinstance(data, dict):
        return False
    return all(field in data for field in required_fields)

def sanitize_numeric_input(value: Any, min_val: int = 0, max_val: int = 1000) -> Optional[int]:
    """Converts input to int and enforces range boundaries."""
    try:
        val = int(value)
        if min_val <= val <= max_val:
            return val
    except (ValueError, TypeError):
        pass
    return None

def validate_processing_loop(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Filters a list of inputs based on schema and value constraints."""
    valid_items = []
    required = ['id', 'value']
    
    for item in data:
        if validate_input_schema(item, required):
            clean_val = sanitize_numeric_input(item['value'])
            if clean_val is not None:
                item['value'] = clean_val
                valid_items.append(item)
    
    return valid_items