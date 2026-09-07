import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry_network_operation(
    max_retries: int = 3, 
    delay: float = 1.0, 
    exceptions: Tuple[Type[Exception], ...] = (ConnectionError, TimeoutError)
):
    """Decorator to retry network-related operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator