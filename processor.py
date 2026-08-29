import json
from typing import Any, Dict, List, Optional

class DataProcessor:
    """Utility class for general data handling."""

    def __init__(self, initial_data: Any = None) -> None:
        self.data = initial_data

    def set_data(self, data: Any) -> None:
        """Update the current data for processing."""
        self.data = data

    def flatten_nested_dict(self, data: Optional[Dict[str, Any]] = None, parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
        """Recursively flatten nested dictionaries."""
        if data is None:
            data = self.data
        if not isinstance(data, dict):
            return {parent_key: data} if parent_key else data
        items = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self.flatten_nested_dict(v, new_key, sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def filter_by_keys(self, keys: List[str], data: Optional[List[Dict[str, Any]]] = None) -> List[Dict[str, Any]]:
        """Filter list of dicts keeping only given keys."""
        if data is None:
            data = self.data
        if not isinstance(data, list):
            return []
        return [{k: item.get(k) for k in keys} for item in data]

    def merge_lists(self, *data_lists: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Combine multiple lists of dictionaries."""
        merged: List[Dict[str, Any]] = []
        for lst in data_lists:
            if isinstance(lst, list):
                merged.extend(lst)
        return merged

    def clean_data(self, data: Optional[Any] = None, remove_none: bool = True) -> Any:
        """Recursively remove None values from data structures."""
        if data is None:
            data = self.data
        if isinstance(data, dict):
            return {k: self.clean_data(v, remove_none) for k, v in data.items() if v is not None or not remove_none}
        elif isinstance(data, list):
            return [self.clean_data(item, remove_none) for item in data if item is not None or not remove_none]
        else:
            return data

    def to_json(self, data: Optional[Any] = None, indent: int = 2) -> str:
        """Serialize data to JSON string."""
        if data is None:
            data = self.data
        return json.dumps(data, indent=indent, default=str)


if __name__ == "__main__":
    processor = DataProcessor({"a": {"b": 1, "c": {"d": 2}}, "e": None})
    print(processor.flatten_nested_dict())
    processor.set_data([{"name": "test", "value": 42, "empty": None}])
    print(processor.filter_by_keys(["name", "value"]))
    print(processor.clean_data())
    print(processor.to_json())