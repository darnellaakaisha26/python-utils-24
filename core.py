import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_on_failure(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations on specific exceptions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"All {max_retries} retries failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator

# Example usage for network tasks
if __name__ == "__main__":
    @retry_on_failure(exceptions=(ConnectionError,), max_retries=3, delay=0.5)
    def fetch_data(url: str):
        raise ConnectionError(f"Failed to connect to {url}")