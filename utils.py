import time
import functools
import logging
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry(exceptions: Tuple[Type[Exception], ...] = (Exception,), 
          tries: int = 3, 
          delay: float = 1.0, 
          backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            for i in range(tries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if i == tries - 1:
                        logger.error(f"Failed after {tries} attempts: {e}")
                        raise
                    
                    logger.warning(f"Attempt {i+1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator