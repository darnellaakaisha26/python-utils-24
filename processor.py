import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...], 
                     max_retries: int = 3, 
                     delay: float = 1.0) -> Callable:
    """Decorator for retrying functions on specific exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        time.sleep(delay * (2 ** attempt))
                        logger.warning(f"Retry {attempt + 1}/{max_retries} due to {e}")
                    else:
                        logger.error("Max retries reached")
            raise last_exception  # type: ignore
        return wrapper
    return decorator

@retry_on_failure(exceptions=(ConnectionError, TimeoutError), max_retries=3)
def fetch_data(url: str) -> str:
    """Example function that might fail due to network."""
    # Simulating a network operation
    return f"Data from {url}"