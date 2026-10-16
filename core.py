import functools
import time
import logging
from typing import Callable, Any

# Configure logger for core operations
logger = logging.getLogger(__name__)

# Cache dictionary to store results for performance
_cache = {}

def memoize(func: Callable) -> Callable:
    """Performance decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Optimized iterator for large dataset processing."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTracker:
    """Context manager for monitoring execution timing."""
    def __init__(self, name: str):
        self.name = name
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        logger.info(f"Operation {self.name} completed in {elapsed:.4f}s")