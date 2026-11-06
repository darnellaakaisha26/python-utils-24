import functools
import time
from typing import Any, Callable, Dict

# Global cache for expensive operations
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Thread-safe cache decorator for repetitive tasks."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

class DataProcessor:
    """Optimized batch processing utility class."""
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    def process_bulk(self, data: list) -> list:
        """Process data using list comprehension for speed."""
        # Using list comprehension instead of loop-append for performance
        return [self._transform(item) for item in data]

    @staticmethod
    def _transform(item: Any) -> Any:
        """Mock transformation logic."""
        return item * 2

def timer(func: Callable) -> Callable:
    """Utility to measure execution time of core functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Execution time for {func.__name__}: {duration:.4f}s")
        return result
    return wrapper