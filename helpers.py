import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, retries=3, delay=1.0, backoff=2):
    """Decorator for retrying functions with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def network_request_wrapper(func):
    """Helper to standardize network calls with automatic retries."""
    # Common network exceptions to catch
    import socket
    return retry((socket.timeout, ConnectionError, OSError), retries=3, delay=2.0)(func)