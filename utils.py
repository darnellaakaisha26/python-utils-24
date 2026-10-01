import functools
import time
from typing import Callable, Any, Dict

# Cache dictionary to store results for performance
_CACHE: Dict[str, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function results to improve throughput."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = f"{func.__name__}:{args}:{frozenset(kwargs.items())}"
        if key not in _CACHE:
            _CACHE[key] = func(*args, **kwargs)
        return _CACHE[key]
    return wrapper

def batch_process(data: list, chunk_size: int = 100):
    """Memory-efficient generator for processing large datasets in chunks."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

@memoize
def compute_heavy_task(n: int) -> int:
    """Simulated computationally expensive operation."""
    time.sleep(1)
    return n * n

def clear_cache() -> None:
    """Reset internal state to free memory."""
    global _CACHE
    _CACHE = {}