from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)

class RequestHandler:
    """Manages execution of callback tasks with basic error handling."""

    def __init__(self, timeout: int = 30) -> None:
        self.timeout: int = timeout
        self.registry: Dict[str, Callable] = {}

    def register_task(self, name: str, func: Callable) -> None:
        """Registers a callable task under a specific name."""
        self.registry[name] = func

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Optional[Any]:
        """Executes a registered task by name with provided arguments."""
        task = self.registry.get(name)
        if not task:
            logger.error(f"Task {name} not found in registry")
            return None

        try:
            return task(*args, **kwargs)
        except Exception as e:
            logger.exception(f"Execution error in {name}: {str(e)}")
            return None

    def get_task_names(self) -> list[str]:
        """Retrieves list of all registered task identifiers."""
        return list(self.registry.keys())