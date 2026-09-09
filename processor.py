from typing import List, Dict, Any, Optional

class DataProcessor:
    """Handles transformation and validation of data payloads."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize processor with optional configuration."""
        self.settings: Dict[str, Any] = settings or {}

    def process_items(self, items: List[str]) -> List[str]:
        """Convert input strings to uppercase and filter length."""
        return [item.upper() for item in items if len(item) > 0]

    def extract_keys(self, data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
        """Return a subset dictionary based on allowed keys."""
        return {k: data[k] for k in keys if k in data}

    def validate_batch(self, batch: List[Dict[str, Any]]) -> bool:
        """Ensure all batch items contain the required key."""
        required = self.settings.get("required_key", "id")
        return all(required in item for item in batch)

    def format_output(self, data: Any) -> str:
        """Cast any input to string representation."""
        return str(data).strip()