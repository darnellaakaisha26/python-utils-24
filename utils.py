import time
import functools
from typing import Callable, Any, Type

def retry(exceptions: tuple[Type[Exception], ...], max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
                    else:
                        break
            raise last_exception
        return wrapper
    return decorator