import logging
from typing import Any, Dict, List, Tuple

logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception raised when record validation fails."""
    pass


class BatchProcessor:
    """Processes payload items with pre-execution input validation."""

    def __init__(self, required_fields: List[str]):
        self.required_fields = required_fields

    def _validate_item(self, item: Any) -> Dict[str, Any]:
        """Validate type and schema requirements for an individual record."""
        if not isinstance(item, dict):
            raise ValidationError(f"Invalid type '{type(item).__name__}', expected dictionary")

        for field in self.required_fields:
            if field not in item:
                raise ValidationError(f"Missing required field: '{field}'")
            if item[field] is None:
                raise ValidationError(f"Field '{field}' cannot be None")

        return item

    def process_batch(self, items: List[Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Main processing loop executing validation before item handling."""
        processed = []
        errors = []

        for index, raw_item in enumerate(items):
            try:
                # Validate input integrity prior to processing
                valid_item = self._validate_item(raw_item)
                
                # Transform valid data
                clean_record = {k.strip(): str(v).strip() for k, v in valid_item.items()}
                processed.append(clean_record)
                logger.debug(f"Successfully processed batch index {index}")

            except ValidationError as exc:
                logger.warning(f"Validation error at index {index}: {exc}")
                errors.append({"index": index, "raw": raw_item, "reason": str(exc)})
            except Exception as exc:
                logger.error(f"Unexpected processing failure at index {index}: {exc}")
                errors.append({"index": index, "raw": raw_item, "reason": "Internal error"})

        return processed, errors