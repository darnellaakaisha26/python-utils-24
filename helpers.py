import logging
from typing import Any, Callable, Optional, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar('T')

def safe_execute(func: Callable[[], T], default: Any = None, error_msg: str = 'operation failed') -> Optional[T]:
    """Executes a callable safely, returning default on exception."""
    try:
        return func()
    except (ValueError, TypeError, AttributeError, KeyError) as e:
        logger.error(f"{error_msg}: {str(e)}")
        return default
    except Exception as e:
        logger.critical(f"unexpected system error: {str(e)}")
        raise

def validate_input(data: Any, expected_type: type) -> bool:
    """Checks input type and integrity for edge cases."""
    if data is None:
        return False
    if not isinstance(data, expected_type):
        return False
    # Additional validation for empty collections
    if isinstance(data, (list, dict, str)) and not data:
        return False
    return True

def robust_conversion(value: Any, target_type: type) -> Any:
    """Safely converts types with fallback mechanisms."""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return None