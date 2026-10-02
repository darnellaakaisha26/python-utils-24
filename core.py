from typing import Any, Dict, List, Optional, Callable

class DataProcessor:
    """Handles data transformation and validation tasks."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None) -> None:
        """Initialize with optional configuration settings."""
        self.settings = settings or {}

    def transform_items(self, items: List[Any], func: Callable[[Any], Any]) -> List[Any]:
        """Apply a function to each item in a list with error catching."""
        results: List[Any] = []
        for item in items:
            try:
                results.append(func(item))
            except Exception:
                continue
        return results

    def filter_by_key(self, data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
        """Return dicts matching a specific key-value pair."""
        return [item for item in data if item.get(key) == value]

    def get_summary(self, data: List[Dict[str, Any]]) -> Dict[str, int]:
        """Calculate counts based on internal settings criteria."""
        return {"total": len(data), "processed": len([i for i in data if i.get("active")])}

    @staticmethod
    def validate_payload(payload: Any) -> bool:
        """Check if payload is a non-empty dictionary."""
        return isinstance(payload, dict) and len(payload) > 0