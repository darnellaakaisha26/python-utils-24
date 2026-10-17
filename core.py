import logging
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-24')

class DataProcessor:
    """Utility class for standardized data transformation."""
    
    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}

    def sanitize_input(self, data: Any) -> Any:
        """Removes whitespace and strips null-like entries."""
        if isinstance(data, str):
            return data.strip()
        if isinstance(data, dict):
            return {k: self.sanitize_input(v) for k, v in data.items() if v is not None}
        if isinstance(data, list):
            return [self.sanitize_input(item) for item in data]
        return data

    def execute(self, payload: Any) -> Dict[str, Any]:
        """Orchestrates processing pipeline."""
        try:
            clean_data = self.sanitize_input(payload)
            logger.info("Processing successfully completed")
            return {"status": "success", "data": clean_data}
        except Exception as e:
            logger.error(f"Processing failure: {e}")
            return {"status": "error", "message": str(e)}

def get_instance(config: Optional[Dict[str, Any]] = None) -> DataProcessor:
    """Factory method for processor lifecycle management."""
    return DataProcessor(settings=config)