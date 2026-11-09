"""Data processing module with input validation logic."""

from typing import Any, Callable, Dict, List, Tuple


class DataProcessor:
    """Processes batches of input data with built-in validation."""

    def __init__(self, validator: Callable[[Any], bool] | None = None):
        self.validator = validator or self._default_validator
        self.processed_count = 0
        self.failed_count = 0

    @staticmethod
    def _default_validator(item: Any) -> bool:
        """Default validation ensuring item presence and proper type."""
        if item is None:
            return False
        if isinstance(item, dict) and "id" not in item:
            return False
        if isinstance(item, (str, list, dict)) and len(item) == 0:
            return False
        return True

    def process_batch(self, items: List[Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Main processing loop that validates and transforms input items."""
        valid_results = []
        invalid_records = []

        for index, item in enumerate(items):
            # Perform input validation before attempting execution
            if not self.validator(item):
                self.failed_count += 1
                invalid_records.append({
                    "index": index,
                    "item": item,
                    "reason": "Failed input validation rules"
                })
                continue

            # Transform valid input payloads
            try:
                processed_item = self._transform(item)
                valid_results.append(processed_item)
                self.processed_count += 1
            except Exception as exc:
                self.failed_count += 1
                invalid_records.append({
                    "index": index,
                    "item": item,
                    "reason": f"Transformation error: {exc}"
                })

        return valid_results, invalid_records

    def _transform(self, item: Any) -> Dict[str, Any]:
        """Transform validated items into standardized output structure."""
        if isinstance(item, dict):
            return {**item, "status": "processed"}
        return {"value": item, "status": "processed"}
