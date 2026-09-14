import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles batch processing of application records."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}
        self.batch_size = self.settings.get('batch_size', 100)

    def clean_data(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Sanitizes record keys and filters out empty values."""
        cleaned = []
        for record in records:
            item = {k.strip().lower(): v for k, v in record.items() if v is not None}
            if item:
                cleaned.append(item)
        return cleaned

    def process_batch(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Organizes and validates chunks of data."""
        if not data:
            return []
        
        try:
            processed = self.clean_data(data)
            logger.info(f"Processed {len(processed)} records successfully")
            return processed
        except Exception as e:
            logger.error(f"Batch processing failure: {str(e)}")
            return []

    def transform(self, records: List[Dict[str, Any]]) -> Dict[int, List[Dict[str, Any]]]:
        """Groups processed records by internal category."""
        results = {}
        for record in self.process_batch(records):
            cat_id = record.get('category_id', 0)
            if cat_id not in results:
                results[cat_id] = []
            results[cat_id].append(record)
        return results