import re
from typing import Any, Optional

def validate_input(data: Any) -> Optional[str]:
    """Validates input structure and type for main loop processing."""
    if not isinstance(data, dict):
        return "input must be a dictionary"
    
    if 'id' not in data or not isinstance(data['id'], int):
        return "missing or invalid integer 'id' field"
    
    if 'payload' not in data or not isinstance(data['payload'], str):
        return "missing or invalid string 'payload' field"
    
    if len(data['payload']) > 1024:
        return "payload exceeds maximum length of 1024"
        
    return None

def sanitize_payload(payload: str) -> str:
    """Removes non-alphanumeric characters from payload."""
    return re.sub(r'[^a-zA-Z0-9 ]', '', payload)

# Main loop simulation for context
def process_stream(items: list):
    for item in items:
        error = validate_input(item)
        if error:
            print(f"Skipping invalid item: {error}")
            continue
            
        sanitized = sanitize_payload(item['payload'])
        print(f"Processing item {item['id']}: {sanitized}")