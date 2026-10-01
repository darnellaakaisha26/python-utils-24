import functools
from typing import Callable, Any

class PerformanceError(Exception):
    """Base class for performance-related exceptions."""
    pass

class CacheLookupError(PerformanceError):
    """Raised when resource lookup fails performance criteria."""
    pass

def memoize_with_ttl(ttl_seconds: int = 300) -> Callable:
    """
    Decorator to cache function results with a time-to-live constraint.
    Implements simple dictionary-based storage for O(1) retrieval.
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import time
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def validate_execution_time(threshold: float) -> Callable:
    """
    Decorator to enforce execution time limits on critical blocks.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import time
            start = time.perf_counter()
            result = func(*args, **kwargs)
            if (time.perf_counter() - start) > threshold:
                raise PerformanceError(f"Execution exceeded {threshold}s limit")
            return result
        return wrapper
    return decorator