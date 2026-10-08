import functools
from typing import Callable, Any

class PerformanceOptimizationError(Exception):
    """Base exception for utility performance errors."""
    pass

def memoize_with_ttl(ttl_seconds: int) -> Callable:
    """
    Decorator to cache function results with simple TTL expiration.
    Uses a dictionary for O(1) lookups and performance efficiency.
    """
    def decorator(func: Callable) -> Callable:
        cache = {}

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            import time
            key = (args, frozenset(kwargs.items()))
            current_time = time.time()

            if key in cache:
                result, timestamp = cache[key]
                if current_time - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator

class OptimizedProcessor:
    """Interface for high-performance utility operations."""
    def __init__(self, data_limit: int = 1000):
        self._limit = data_limit

    @memoize_with_ttl(ttl_seconds=60)
    def compute_heavy_metric(self, input_val: int) -> int:
        """Simulates computation that benefits from memoization."""
        if input_val > self._limit:
            raise PerformanceOptimizationError("Input exceeds limit")
        # Simulated intensive operation
        return sum(i * i for i in range(input_val))