import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger(__name__)

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 4,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True
) -> Callable:
    """
    Decorator for retrying a function with exponential backoff and optional jitter.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(f"Failed '{func.__name__}' after {tries} attempts. Error: {e}")
                        raise e
                    
                    current_delay = attempt_delay
                    if jitter:
                        current_delay *= random.uniform(0.5, 1.5)
                    
                    logger.warning(
                        f"Retrying '{func.__name__}' in {current_delay:.2f} seconds... "
                        f"(Attempt {attempt}/{tries} failed due to: {e})"
                    )
                    time.sleep(current_delay)
                    attempt_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator