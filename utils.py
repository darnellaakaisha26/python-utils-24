import functools
import time
import logging
from typing import Callable, Any, Dict

# Configure basic logger for module diagnostics
logger = logging.getLogger(__name__)

# Cache for memoization with automatic expiration logic
_memoization_cache: Dict[tuple, Any] = {}

def memoize_with_ttl(ttl: int = 300):
    """Performance decorator for caching function calls with TTL."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in _memoization_cache:
                result, timestamp = _memoization_cache[key]
                if now - timestamp < ttl:
                    return result
            
            result = func(*args, **kwargs)
            _memoization_cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(items: list, chunk_size: int = 100):
    """Memory-efficient generator for large dataset processing."""
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def fast_flatten(nested_list: list) -> list:
    """Flattening utility using list comprehension for speed."""
    return [item for sublist in nested_list for item in sublist]