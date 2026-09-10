import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(max_attempts=3, delay=1.0, exceptions=(Exception,)):
    """Decorator to retry a function if it raises specified exceptions."""
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
                        logger.error(f"Final attempt {attempts} failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempts} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2.0)
def fetch_url_data(url):
    """Example network operation function."""
    # Simulating network call
    print(f"Fetching data from {url}...")
    raise ConnectionError("Server unreachable")