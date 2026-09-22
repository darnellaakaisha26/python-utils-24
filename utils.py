import functools
import time
from typing import Callable, Any, Dict

# Cache for storing expensive function results
_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator to cache results of functions with hashable arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(items: list, chunk_size: int = 100) -> list:
    """Memory efficient chunking for large datasets."""
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

@memoize
def compute_heavy_data(n: int) -> int:
    """Simulation of performance-intensive calculation."""
    time.sleep(1)
    return sum(i * i for i in range(n))

def clear_cache() -> None:
    """Clear all cached results from memory."""
    _CACHE.clear()