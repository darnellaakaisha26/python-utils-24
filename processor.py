import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """Utility class for safe data transformation."""

    def process_item(self, data: Any) -> Optional[Any]:
        """Attempts to parse and process input data safely."""
        if data is None:
            logger.warning("Attempted to process null data input")
            return None

        try:
            if not isinstance(data, (dict, list, str)):
                raise ValueError(f"Unsupported data type: {type(data).__name__}")

            # Simulate processing logic
            if isinstance(data, str) and not data.strip():
                return None

            return self._transform(data)

        except (ValueError, TypeError) as e:
            logger.error(f"Data transformation failed: {e}")
            return None
        except Exception as e:
            logger.critical(f"Unexpected system failure: {e}", exc_info=True)
            raise

    def _transform(self, data: Any) -> Any:
        """Internal transformation logic helper."""
        if isinstance(data, dict):
            return {str(k): v for k, v in data.items()}
        return str(data).strip()