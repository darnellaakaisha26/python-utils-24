import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Executes a function safely with error trapping."""
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Execution error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")
        raise

def validate_input(data: Any, expected_type: type) -> bool:
    """Checks input against expected type with edge case handling."""
    if data is None:
        return False
    try:
        return isinstance(data, expected_type)
    except TypeError:
        return False

def process_payload(payload: Optional[dict]) -> dict:
    """Processes dict payload with null safety."""
    if not isinstance(payload, dict):
        return {}
    return {k: v for k, v in payload.items() if v is not None}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = safe_execute(len, None, default=0)
    print(f"Result: {result}")