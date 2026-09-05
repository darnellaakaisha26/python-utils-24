from typing import Any, Dict, List, Optional, Union

class DataProcessor:
    """Handles transformation of dictionary datasets."""

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config: Dict[str, Any] = config or {}

    def flatten_dict(self, data: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
        """Recursively flattens a nested dictionary into a single-level map."""
        items: List[tuple] = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self.flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def format_values(self, data: Dict[str, Any], prefix: str = "val") -> Dict[str, str]:
        """Converts all dictionary values to string representations with prefixes."""
        return {k: f"{prefix}_{v}" for k, v in data.items()}

    def filter_keys(self, data: Dict[str, Any], keys: List[str]) -> Dict[str, Any]:
        """Returns a subset of the dictionary based on allowed keys."""
        return {k: v for k, v in data.items() if k in keys}

def process_payload(payload: Union[Dict, List]) -> Dict[str, Any]:
    """Entry point for processing incoming payload structures."""
    if isinstance(payload, list):
        return {"count": len(payload), "data": payload}
    processor = DataProcessor()
    return processor.flatten_dict(payload)