import logging
from typing import Any, List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles transformation and validation of data payloads."""

    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        self.strict_mode = settings.get("strict", True)

    def process_batch(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Cleans and filters a list of data entries."""
        results = []
        for entry in data:
            try:
                cleaned = self._sanitize(entry)
                if cleaned:
                    results.append(cleaned)
            except ValueError as e:
                if self.strict_mode:
                    logger.error(f"Processing error: {e}")
                    raise
                logger.warning(f"Skipping invalid entry: {e}")
        return results

    def _sanitize(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        """Internal logic for data normalization."""
        if not isinstance(entry, dict):
            raise ValueError("Entry must be a dictionary")
        
        # Remove empty keys and normalize types
        return {k: str(v).strip() for k, v in entry.items() if v is not None}

def run_pipeline(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Entry point for processing batch operations."""
    processor = DataProcessor({"strict": False})
    return processor.process_batch(data)