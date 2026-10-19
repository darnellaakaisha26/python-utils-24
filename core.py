import functools
import time
from typing import Callable, Any

# global cache for intensive compute results
_CACHE = {}

def memoize_with_expiry(timeout: int = 300):
    """Performance decorator with time-based invalidation."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in _CACHE:
                result, timestamp = _CACHE[key]
                if now - timestamp < timeout:
                    return result
            
            result = func(*args, **kwargs)
            _CACHE[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(data: list, chunk_size: int = 100):
    """Generator for memory-efficient chunked iteration."""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def clear_core_cache():
    """Manual memory management for global cache."""
    _CACHE.clear()