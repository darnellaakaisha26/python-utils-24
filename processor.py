from typing import List, Dict, Any, Optional

class DataProcessor:
    """Utility class for sanitizing and transforming input dictionaries."""

    def __init__(self, key_mapping: Dict[str, str]) -> None:
        """Initialize processor with a key translation map."""
        self.key_mapping = key_mapping

    def process_data(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Transform list of dicts using key_mapping and stripping whitespace."""
        results: List[Dict[str, Any]] = []

        for item in items:
            processed: Dict[str, Any] = {}
            for key, value in item.items():
                new_key = self.key_mapping.get(key, key)
                if isinstance(value, str):
                    processed[new_key] = value.strip()
                else:
                    processed[new_key] = value
            results.append(processed)

        return results

    def filter_nulls(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Remove keys with None values from the provided items."""
        return [{k: v for k, v in item.items() if v is not None} for item in items]

    def get_summary(self, items: List[Dict[str, Any]]) -> Optional[int]:
        """Return the count of items in the current batch."""
        return len(items) if items else None