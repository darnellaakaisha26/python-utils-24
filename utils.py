import time
import functools
import random

def retry_operation(max_retries=3, base_delay=1.0, exceptions=(Exception,)):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    if retries >= max_retries:
                        raise e
                    
                    # Exponential backoff with jitter
                    delay = base_delay * (2 ** (retries - 1))
                    jitter = delay * 0.1 * random.random()
                    time.sleep(delay + jitter)
        return wrapper
    return decorator

# Example usage:
# @retry_operation(max_retries=3)
# def fetch_url(url):
#     pass