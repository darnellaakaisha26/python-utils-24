import re
from typing import Any, Optional

# regex pattern for basic alphanumeric input
VALID_PATTERN = re.compile(r'^[a-zA-Z0-9_\-]+$')

class ValidationError(Exception):
    """Custom exception for input validation failures."""
    pass

def validate_input(data: Any, min_length: int = 3, max_length: int = 50) -> str:
    """Validates string input based on length and regex patterns."""
    if not isinstance(data, str):
        raise ValidationError(f"Expected string, got {type(data).__name__}")
    
    cleaned = data.strip()
    
    if not (min_length <= len(cleaned) <= max_length):
        raise ValidationError(f"Input length must be between {min_length} and {max_length}")
    
    if not VALID_PATTERN.match(cleaned):
        raise ValidationError("Input contains forbidden characters")
        
    return cleaned

def process_main_loop(items: list) -> list:
    """Main processing loop with integrated validation logic."""
    results = []
    for item in items:
        try:
            valid_item = validate_input(item)
            results.append(f"processed_{valid_item}")
        except ValidationError as e:
            print(f"Skipping invalid item '{item}': {e}")
            continue
    return results