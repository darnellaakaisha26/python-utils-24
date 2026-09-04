import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator to retry network-dependent functions."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {delay}s...")
                    if attempt < max_attempts:
                        time.sleep(delay)
            
            logger.error(f"Operation failed after {max_attempts} attempts.")
            raise last_exception
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def fetch_data(url: str):
    """Example usage for network data fetching."""
    # Placeholder for actual network logic
    pass