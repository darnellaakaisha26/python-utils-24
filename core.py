import functools
import time
from typing import Callable, Any, Dict

# Cache to store results of expensive computations
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100) -> list:
    """Generator for processing data in manageable chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

class PerformanceTracker:
    """Simple context manager for execution time logging."""
    def __init__(self, label: str):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"[Performance] {self.label}: {elapsed:.4f}s")

def optimized_sum(numbers: list) -> float:
    """Use built-in summation for speed efficiency."""
    return float(sum(numbers))