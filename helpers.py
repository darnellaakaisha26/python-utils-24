import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def with_retry(retries: int = 3, delay: float = 1.0, exceptions: Tuple[Type[Exception], ...] = (Exception,)):
    """
    Decorator for retrying network operations on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Function {func.__name__} failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

@with_retry(retries=3, delay=2.0)
def fetch_data(url: str):
    """
    Example network operation wrapper.
    """
    import urllib.request
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')