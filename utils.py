import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator to retry network-related functions with exponential backoff.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Retry {attempts}/{max_attempts} for {func.__name__} after {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= 2
            
            return None
        return wrapper
    return decorator