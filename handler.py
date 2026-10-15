import logging
from typing import Any, Dict, Optional

# Configure logging for module tracking
logger = logging.getLogger(__name__)

class DataHandler:
    """Base handler for processing generic data payloads."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.results: list = []

    def validate_payload(self, data: Any) -> bool:
        """Check if payload meets minimum requirements."""
        if not data:
            logger.warning("Empty payload received")
            return False
        return True

    def process(self, data: Any) -> Dict[str, Any]:
        """Primary execution method for data transformation."""
        if not self.validate_payload(data):
            return {"status": "error", "message": "invalid input"}

        try:
            processed = {"data": data, "processed": True}
            self.results.append(processed)
            return {"status": "success", "result": processed}
        except Exception as e:
            logger.error(f"Processing failed: {str(e)}")
            return {"status": "error", "message": str(e)}

    def clear_cache(self) -> None:
        """Reset internal state storage."""
        self.results = []
        logger.info("Handler cache cleared")