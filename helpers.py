import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None) -> Any:
    """
    executes a function safely with error handling for edge cases.
    returns a default value if an exception occurs during execution.
    """
    try:
        return func(*args)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        logger.error(f"execution error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error: {e}")
        raise

def validate_input(data: Optional[dict], keys: list[str]) -> bool:
    """
    checks if input data contains all required keys and is not empty.
    """
    if not data or not isinstance(data, dict):
        return False
    return all(key in data for key in keys)

def parse_int_robust(value: Any, fallback: int = 0) -> int:
    """
    attempts to convert value to integer, returning fallback on failure.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return fallback