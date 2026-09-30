import functools
import time
from typing import Callable, Any, Dict

# global cache for memoization
_MEMO_CACHE: Dict[str, Any] = {}

def memoize_with_expiry(ttl: int = 300) -> Callable:
    """decorator for caching function results with ttl expiry"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = f"{func.__name__}:{str(args)}:{str(kwargs)}"
            now = time.time()
            
            if key in _MEMO_CACHE:
                val, timestamp = _MEMO_CACHE[key]
                if now - timestamp < ttl:
                    return val
            
            result = func(*args, **kwargs)
            _MEMO_CACHE[key] = (result, now)
            return result
        return wrapper
    return decorator

def batch_process(data: list, chunk_size: int = 100):
    """generator for memory-efficient list processing"""
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def fast_flatten(nested_list: list) -> list:
    """optimized list flattening using list comprehension"""
    return [item for sublist in nested_list for item in sublist]