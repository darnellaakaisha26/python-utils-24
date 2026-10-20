import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1, exceptions=(Exception,)): 
    """Decorator for retrying network operations."""
    def decorator(func):
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
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def fetch_data(url):
    """Example of a network call with retry logic."""
    # Placeholder for requests logic
    raise ConnectionError(f"Failed to connect to {url}")