import logging
from typing import Any, Optional, Callable

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None) -> Any:
    """Execute a callable with broad exception catching."""
    try:
        return func(*args)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Data processing error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}", exc_info=True)
        raise

def validate_input_range(value: Any, min_val: int, max_val: int) -> bool:
    """Validate that a value falls within expected numeric bounds."""
    try:
        if not isinstance(value, (int, float)):
            return False
        return min_val <= value <= max_val
    except Exception:
        return False

def get_nested_key(data: dict, path: list, default: Any = None) -> Any:
    """Safely extract nested dictionary values."""
    if not isinstance(data, dict):
        return default
    
    current = data
    try:
        for key in path:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default