import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure basic logging for performance monitoring
logger = logging.getLogger(__name__)

# Cache for memoized function results
_memo_cache: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results for identical inputs."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _memo_cache:
            _memo_cache[key] = func(*args, **kwargs)
        return _memo_cache[key]
    return wrapper

def time_execution(func: Callable) -> Callable:
    """Decorator for logging execution time of critical paths."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        logger.debug(f"function {func.__name__} took {duration:.4f}s")
        return result
    return wrapper

def batch_process(items: list, batch_size: int = 100):
    """Memory-efficient generator for processing large datasets."""
    for i in range(0, len(items), batch_size):
        yield items[i : i + batch_size]

def clear_cache() -> None:
    """Utility for manual cache clearing in memory-constrained environments."""
    _memo_cache.clear()