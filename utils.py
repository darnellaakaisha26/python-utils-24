import time
import random
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=4, delay=1.0, backoff=2.0, jitter=True):
    """
    Decorator to retry a function call with exponential backoff and jitter.

    :param exceptions: Exception or tuple of exceptions to catch.
    :param tries: Maximum number of times to try before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to the delay after each failure.
    :param jitter: If True, introduces randomness to prevent thundering herd problems.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    # Calculate delay with randomized jitter
                    current_delay = mdelay
                    if jitter:
                        current_delay *= random.uniform(0.5, 1.5)

                    logger.warning(
                        f"Network operation failed: {e}. "
                        f"Retrying in {current_delay:.2f} seconds... ({mtries - 1} attempts remaining)"
                    )
                    time.sleep(current_delay)
                    mtries -= 1
                    mdelay *= backoff
            # Final try, raising the error if it fails again
            return func(*args, **kwargs)
        return wrapper
    return decorator
