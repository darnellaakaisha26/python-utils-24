import logging
from typing import Any, List, Optional

# Configure standard processor logging
logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles bulk transformation of input datasets."""

    def __init__(self, settings: Optional[dict] = None):
        self.settings = settings or {}
        self.strict_mode = self.settings.get("strict", True)

    def sanitize(self, data: Any) -> Any:
        """Removes whitespace and ensures consistent string formatting."""
        if isinstance(data, str):
            return data.strip()
        return data

    def process_batch(self, items: List[Any]) -> List[Any]:
        """Execution pipeline for collection processing."""
        results = []
        for item in items:
            try:
                cleaned = self.sanitize(item)
                if cleaned is not None:
                    results.append(cleaned)
            except Exception as e:
                logger.error(f"failed to process item: {item}, error: {e}")
                if self.strict_mode:
                    raise
        return results

def run_pipeline(data: List[Any]) -> List[Any]:
    """Utility wrapper for quick processor execution."""
    processor = DataProcessor()
    return processor.process_batch(data)