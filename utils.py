import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_call(max_retries: int = 3, delay: float = 1.0):
    """Decorator to retry network functions on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error("Max retries reached. Operation failed.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_call(max_retries=3, delay=0.5)
def fetch_data(url: str) -> str:
    """Simulated network operation for demonstration purposes."""
    # Example implementation of a network request
    return f"data from {url}"