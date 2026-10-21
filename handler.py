from typing import Any, Callable, Dict, Optional

class DataHandler:
    """Handles data transformation and processing tasks."""

    def __init__(self, prefix: str = "data") -> None:
        self.prefix: str = prefix
        self.registry: Dict[str, Callable[[Any], Any]] = {}

    def register_processor(self, name: str, func: Callable[[Any], Any]) -> None:
        """Registers a transformation function for a specific name."""
        self.registry[name] = func

    def process(self, name: str, value: Any) -> Optional[Any]:
        """Executes the registered processor for the given value."""
        processor = self.registry.get(name)
        if not processor:
            return None
        return processor(value)

    def format_key(self, key: str) -> str:
        """Returns the key string prefixed by instance settings."""
        return f"{self.prefix}_{key}"

    def batch_process(self, items: Dict[str, Any]) -> Dict[str, Any]:
        """Processes a collection of items through registered handlers."""
        results: Dict[str, Any] = {}
        for key, value in items.items():
            processed_val = self.process(key, value)
            if processed_val is not None:
                results[key] = processed_val
        return results