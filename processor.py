import logging
from typing import Any, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles batch processing and data sanitization."""

    def __init__(self, settings: Optional[dict] = None):
        self.settings = settings or {}
        self.max_retries = self.settings.get("max_retries", 3)

    def sanitize(self, data: List[Any]) -> List[Any]:
        """Removes null entries from input list."""
        if not isinstance(data, list):
            raise ValueError("Input must be a list")
        return [item for item in data if item is not None]

    def process_batch(self, batch: List[Any]) -> List[Any]:
        """Executes transformation on sanitized data."""
        cleaned = self.sanitize(batch)
        results = []
        
        for item in cleaned:
            try:
                processed = self._transform(item)
                results.append(processed)
            except Exception as e:
                logger.error(f"Failed to process item: {e}")
                continue
                
        return results

    def _transform(self, item: Any) -> Any:
        """Internal method for individual item logic."""
        return str(item).strip().lower()

    def cleanup_resources(self) -> None:
        """Resets internal state for new tasks."""
        self.settings = {}
        logger.info("Processor resources cleared successfully")