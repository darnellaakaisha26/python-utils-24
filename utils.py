import functools
import time
from typing import Callable, Any, Dict

# Internal cache storage for function results
_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Performance optimization: cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{tuple(sorted(kwargs.items()))}"
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Generator for efficient memory handling of large datasets."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTimer:
    """Context manager for tracking block execution time."""
    def __init__(self, label: str = "Operation"):
        self.label = label
        self.start = 0.0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"{self.label} took {elapsed:.4f} seconds")