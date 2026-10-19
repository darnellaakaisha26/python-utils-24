import logging
from typing import Any, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Handles batch processing of raw data inputs."""

    def __init__(self, debug_mode: bool = False):
        self.debug_mode = debug_mode

    def sanitize_input(self, data: Any) -> Optional[str]:
        """Cleans string data and validates existence."""
        if not data:
            return None
        return str(data).strip()

    def process_batch(self, items: List[Any]) -> List[str]:
        """Filters and processes a list of raw items."""
        processed = []
        for item in items:
            cleaned = self.sanitize_input(item)
            if cleaned:
                processed.append(cleaned)
        
        if self.debug_mode:
            logger.info(f"Processed {len(processed)} items successfully")
        return processed

    def clear_cache(self) -> None:
        """Reset internal state for memory efficiency."""
        # Placeholder for future state management
        logger.debug("Cache clearing operation completed")

if __name__ == "__main__":
    proc = DataProcessor(debug_mode=True)
    sample_data = ["  alpha ", "beta", None, "gamma  "]
    print(proc.process_batch(sample_data))