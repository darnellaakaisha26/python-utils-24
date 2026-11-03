import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry(exceptions: Tuple[Type[Exception], ...], max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying functions on specific exceptions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        logger.error(f"Failed after {max_attempts} attempts: {e}")
                        raise
                    sleep_time = delay * (2 ** (attempts - 1))
                    logger.warning(f"Retry {attempts}/{max_attempts} after {sleep_time}s due to {type(e).__name__}")
                    time.sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator