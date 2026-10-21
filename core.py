import logging
from typing import Any, Dict, Optional

# Configure global logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-24')

class DataProcessor:
    """Standard processor for data transformation tasks."""

    def __init__(self, settings: Optional[Dict[str, Any]] = None):
        self.settings = settings or {}
        self.is_active = True

    def process_payload(self, data: Any) -> Any:
        """Sanitize and validate input payload."""
        if not self.is_active:
            logger.warning("Processor inactive, skipping payload")
            return None

        try:
            return self._transform(data)
        except Exception as e:
            logger.error(f"Transformation failure: {e}")
            return None

    def _transform(self, data: Any) -> Any:
        """Internal transformation logic."""
        if isinstance(data, dict):
            return {k: str(v).strip() for k, v in data.items()}
        return str(data).strip()

    def toggle_status(self, state: bool) -> None:
        """Update operational status of processor."""
        self.is_active = state
        logger.info(f"Status updated to: {state}")

def get_default_config() -> Dict[str, Any]:
    """Return base configuration dictionary."""
    return {
        "version": "24.0.1",
        "mode": "production",
        "retries": 3
    }