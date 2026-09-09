import logging
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

class DataHandler:
    """Manages data transformation and flow control."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.is_active = True

    def process_payload(self, data: Any) -> Dict[str, Any]:
        """Validates and formats incoming data packets."""
        if not self.is_active:
            raise RuntimeError("Handler is currently disabled")

        try:
            processed = {
                "status": "success",
                "payload": data,
                "meta": {"version": "2.4", "source": "internal"}
            }
            return processed
        except Exception as e:
            logger.error(f"Processing error: {e}")
            return {"status": "error", "message": str(e)}

    def shutdown(self) -> None:
        """Graceful cleanup of handler resources."""
        self.is_active = False
        logger.info("Handler resources successfully released")

def create_handler(config: Optional[Dict[str, Any]] = None) -> DataHandler:
    """Factory function for DataHandler initialization."""
    return DataHandler(config=config)