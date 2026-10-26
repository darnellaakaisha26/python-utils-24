import time
import random
import functools
from typing import Callable, Any

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator for retrying network operations with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            attempts = 0
            current_delay = delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(current_delay + random.uniform(0, 0.1))
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_operation(max_attempts=3, delay=2.0)
def fetch_data(url: str):
    """
    Example network call utility.
    """
    # Simulate network instability
    if random.random() < 0.5:
        raise ConnectionError(f"Failed to connect to {url}")
    return {"status": 200, "data": "sample"}