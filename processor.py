from typing import List, Dict, Any, Optional

class DataProcessor:
    """Utility class for standardizing list-based data structures."""

    def __init__(self, key_prefix: str = "item") -> None:
        self.key_prefix: str = key_prefix

    def transform(self, items: List[Any]) -> Dict[str, Any]:
        """
        Converts a list of items into a dictionary with indexed keys.

        :param items: List of data objects to process
        :return: Dictionary containing the mapped data
        """
        if not isinstance(items, list):
            raise ValueError("Input must be a list")

        return {f"{self.key_prefix}_{i}": val for i, val in enumerate(items)}

    def filter_nulls(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Removes key-value pairs where the value is None.

        :param data: Dictionary to clean
        :return: Filtered dictionary
        """
        return {k: v for k, v in data.items() if v is not None}

def process_batch(data_list: List[Any], prefix: Optional[str] = None) -> Dict[str, Any]:
    """
    Batch transformation of raw list data.

    :param data_list: Input collection
    :param prefix: Optional string prefix for dictionary keys
    :return: Processed result dictionary
    """
    proc = DataProcessor(key_prefix=prefix or "entry")
    mapped_data = proc.transform(data_list)
    return proc.filter_nulls(mapped_data)