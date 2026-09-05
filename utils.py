import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure basic logger for utility functions
logger = logging.getLogger(__name__)

def memoize_with_ttl(ttl_seconds: int = 300) -> Callable:
    """Decorator for caching function results with a time-to-live period."""
    def decorator(func: Callable) -> Callable:
        cache: Dict[tuple, tuple[Any, float]] = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            now = time.time()
            key = (args, frozenset(kwargs.items()))
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(iterable: list, chunk_size: int = 100):
    """Memory-efficient generator for processing large lists in chunks."""
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]

def timing_decorator(func: Callable) -> Callable:
    """Performance monitoring wrapper for core operations."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        logger.debug(f"Function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper