import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_network_failure(retries: int = 3, delay: float = 1.0, exceptions: tuple = (ConnectionError, TimeoutError)) -> Callable:
    """Decorator for retrying network-bound functions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"All {retries} retries exhausted.")
            raise last_exception
        return wrapper
    return decorator