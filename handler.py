from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class RequestHandler:
    """Handles incoming requests with optional pre-processing."""

    def __init__(self, callback: Optional[Callable[[Dict[str, Any]], Any]] = None) -> None:
        self.callback = callback

    def process_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validates and processes input dictionary data.

        Args:
            data: A dictionary containing request payload.

        Returns:
            A dictionary containing the processed result or status.
        """
        if not isinstance(data, dict):
            raise ValueError("Request data must be a dictionary")

        try:
            if self.callback:
                result = self.callback(data)
                return {"status": "success", "data": result}
            
            logger.info("Request processed without callback")
            return {"status": "processed", "data": data}
        except Exception as e:
            logger.error(f"Processing failed: {str(e)}")
            return {"status": "error", "message": str(e)}

    def update_callback(self, callback: Callable[[Dict[str, Any]], Any]) -> None:
        """Updates the request callback function."""
        self.callback = callback