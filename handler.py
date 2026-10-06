from typing import Any, Dict, List, Tuple


class ProcessingError(Exception):
    """Exception raised for unrecoverable processing errors."""
    pass


class PayloadHandler:
    """Handles and validates incoming data payloads before processing."""

    def __init__(self, min_value_length: int = 1):
        self.min_value_length = min_value_length

    def validate_item(self, item: Any) -> Dict[str, Any]:
        """Validates individual payload items for schema compliance."""
        if not isinstance(item, dict):
            raise TypeError("Payload must be a dictionary")

        if "id" not in item or "value" not in item:
            raise KeyError("Missing required keys: 'id' and 'value'")

        if not isinstance(item["id"], int):
            raise TypeError("Field 'id' must be an integer")

        if not isinstance(item["value"], str):
            raise TypeError("Field 'value' must be a string")

        if len(item["value"].strip()) < self.min_value_length:
            raise ValueError(
                f"Field 'value' must be at least {self.min_value_length} chars"
            )

        return item

    def process_batch(
        self, batch: List[Any]
    ) -> Tuple[List[Dict[str, Any]], List[str]]:
        """Processes and validates a batch of inputs in the main loop."""
        successful_items = []
        errors = []

        for index, item in enumerate(batch):
            try:
                validated_item = self.validate_item(item)
                processed_item = {
                    "id": validated_item["id"],
                    "value": validated_item["value"].strip().upper()
                }
                successful_items.append(processed_item)
            except (TypeError, KeyError, ValueError) as err:
                errors.append(f"Index {index} rejected: {err}")

        return successful_items, errors
