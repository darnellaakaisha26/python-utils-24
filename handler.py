from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Utility class for processing dictionaries with functional hooks."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize handler with optional settings mapping."""
        self.settings = settings or {}

    def execute(self, payload: Dict[str, Any], callback: Optional[Callable[[Any], Any]] = None) -> Dict[str, Any]:
        """Apply processing logic to payload and optional callback transformation."""
        processed_data: Dict[str, Any] = payload.copy()
        
        # Apply core transformations based on settings
        if self.settings.get("strip_whitespace", False):
            processed_data = {k: str(v).strip() for k, v in processed_data.items()}
            
        if callback:
            return {k: callback(v) for k, v in processed_data.items()}
            
        return processed_data

    def update_settings(self, key: str, value: Any) -> None:
        """Update specific internal configuration key-value pairs."""
        self.settings[key] = value

def create_handler(config: Optional[Dict[str, Any]] = None) -> DataHandler:
    """Factory function for creating pre-configured DataHandler instances."""
    return DataHandler(settings=config)