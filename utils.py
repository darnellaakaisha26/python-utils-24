import time
import functools
import random
from typing import Callable, Any, Type

def retry_on_failure(retries: int = 3, delay: float = 1.0, backoff: float = 2.0, exceptions: tuple = (Exception,)): 
    """Decorator for retrying functions with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries - 1:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

def execute_with_retry(func: Callable, *args, **kwargs) -> Any:
    """Utility for executing callables with retry logic."""
    retries = kwargs.pop('retries', 3)
    delay = kwargs.pop('delay', 1.0)
    
    for i in range(retries):
        try:
            return func(*args, **kwargs)
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(delay * (2 ** i))
    return None