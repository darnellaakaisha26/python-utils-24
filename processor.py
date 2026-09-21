import logging
from typing import Any, Optional, Union

logger = logging.getLogger(__name__)

class DataProcessor:
    """Utility for processing raw input data with validation."""

    def __init__(self, strict: bool = False):
        self.strict = strict

    def process_item(self, item: Any) -> Optional[Any]:
        """Process a single item with error handling for edge cases."""
        try:
            if item is None:
                raise ValueError("input item cannot be None")
            
            if not isinstance(item, (str, int, float)):
                raise TypeError(f"unsupported data type: {type(item).__name__}")

            # Simulate processing logic
            return str(item).strip()

        except (ValueError, TypeError) as e:
            logger.error(f"processing error: {e}")
            if self.strict:
                raise
            return None

    def batch_process(self, items: list) -> list:
        """Handle lists ensuring container integrity."""
        if not isinstance(items, list):
            logger.warning("invalid input type provided to batch processor")
            return []
        
        results = []
        for item in items:
            res = self.process_item(item)
            if res is not None:
                results.append(res)
        return results