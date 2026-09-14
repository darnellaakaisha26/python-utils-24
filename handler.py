import logging
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

def safe_execute(func: Callable, *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """
    Executes a callable safely by catching common exceptions.
    Returns the default value if an error occurs.
    """
    try:
        return func(*args, **kwargs)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"Execution error in {func.__name__}: {e}")
        return default
    except Exception as e:
        logger.critical(f"Unexpected system error in {func.__name__}: {e}", exc_info=True)
        return default

def validate_input_data(data: Any, expected_type: type) -> bool:
    """
    Validates input type and content before processing.
    """
    if data is None:
        return False
    if not isinstance(data, expected_type):
        logger.warning(f"Invalid input type: expected {expected_type}, got {type(data)}")
        return False
    return True

def process_with_fallback(items: list, processor: Callable, fallback_val: Any = None) -> list:
    """
    Processes list items with individual error shielding.
    """
    results = []
    for item in items:
        try:
            results.append(processor(item))
        except Exception:
            results.append(fallback_val)
    return results