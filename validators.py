import re
from typing import Any, Dict, Optional

def validate_payload(data: Dict[str, Any]) -> bool:
    """Validates input structure and types for processing loop."""
    required_fields = {"id": int, "payload": str, "timestamp": float}
    
    for field, expected_type in required_fields.items():
        if field not in data:
            return False
        if not isinstance(data[field], expected_type):
            return False
            
    if not re.match(r"^[a-zA-Z0-9_]+$", data["payload"]):
        return False
        
    return True

def sanitize_input(data: Dict[str, Any]) -> Dict[str, Any]:
    """Cleans input data by stripping whitespace and normalizing keys."""
    return {
        "id": int(data["id"]),
        "payload": str(data["payload"]).strip(),
        "timestamp": float(data["timestamp"])
    }

def process_with_validation(data: Any) -> Optional[Dict[str, Any]]:
    """Main validation entry point for the processing loop."""
    if not isinstance(data, dict):
        return None
        
    if not validate_payload(data):
        return None
        
    return sanitize_input(data)