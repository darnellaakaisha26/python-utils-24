import functools
import time
from typing import Callable, Any, Dict

# Cache for performance optimization of expensive operations
_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        return _cache[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator to yield chunks for efficient memory usage."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTimer:
    """Context manager for tracking execution duration."""
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start

def fast_lookup_dict(items: list, key_attr: str) -> dict:
    """Converts list to dict for O(1) complexity lookup."""
    return {getattr(item, key_attr): item for item in items}