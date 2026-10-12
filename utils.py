import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure logger for performance monitoring
logger = logging.getLogger(__name__)

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results using a dictionary."""
    cache: Dict[Any, Any] = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def performance_timer(func: Callable) -> Callable:
    """Decorator to measure and log execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.debug(f"Function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator to yield chunks for memory efficiency."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Optimization constant for default cache size limits
DEFAULT_CACHE_LIMIT = 1024