import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}
        self._cache: Dict[str, Any] = {}

    def process_item(self, key: str, value: Any) -> Any:
        """Sanitizes and stores input data in internal cache."""
        if not key or not isinstance(key, str):
            logger.error("Invalid key provided")
            return None
        
        processed = str(value).strip()
        self._cache[key] = processed
        return processed

    def clear_cache(self) -> None:
        """Resets the internal storage to empty state."""
        self._cache.clear()
        logger.info("Cache cleanup completed")

    def get_status(self) -> Dict[str, int]:
        return {"count": len(self._cache)}

def initialize_service(config: Dict[str, Any]) -> DataProcessor:
    """Factory function for creating processor instances."""
    return DataProcessor(settings=config)