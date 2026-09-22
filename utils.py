import time
import functools
import logging
from typing import Callable, Any, Type

logger = logging.getLogger(__name__)

def retry_network_op(exceptions: tuple[Type[Exception], ...], 
                     retries: int = 3, 
                     delay: float = 1.0) -> Callable:
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= retries:
                        logger.error(f"Max retries reached for {func.__name__}")
                        raise e
                    
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
            return None
        return wrapper
    return decorator