import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, backoff=2, exceptions=(ConnectionError, TimeoutError)):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = 1
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}, retrying in {delay}s...")
                    time.sleep(delay)
                    delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator