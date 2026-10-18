import functools
import time
from typing import Callable, Any, Dict

# Cache for performance optimization of expensive lookups
_memoization_cache: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching results of deterministic functions."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100):
    """Generator to yield chunks for efficient memory usage."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

class PerformanceTimer:
    """Context manager for tracking code block execution time."""
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] execution took {elapsed:.4f} seconds")

def clear_cache() -> None:
    """Manual reset for memoization storage."""
    _memoization_cache.clear()