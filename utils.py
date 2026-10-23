import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator for retrying functions on exception."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry(retries=3, delay=2.0)
def fetch_network_data(url: str):
    """Simulated network request with retry logic."""
    # Example implementation: 
    # response = requests.get(url)
    # response.raise_for_status()
    # return response.json()
    pass