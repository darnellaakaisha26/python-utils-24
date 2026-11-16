import functools
import time
from typing import Callable, Any, Dict

# Internal cache to store computed results for performance optimization
_MEMOIZATION_CACHE: Dict[tuple, Any] = {}

def memoize(func: Callable) -> Callable:
    """Decorator for caching function return values."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _MEMOIZATION_CACHE:
            _MEMOIZATION_CACHE[key] = func(*args, **kwargs)
        return _MEMOIZATION_CACHE[key]
    return wrapper

class DataHandler:
    def __init__(self, process_interval: float = 0.1):
        self.process_interval = process_interval

    @memoize
    def expensive_transformation(self, data: tuple) -> list:
        """Simulates a heavy computational task optimized by caching."""
        time.sleep(self.process_interval)
        return [x * 2 for x in data]

    def batch_process(self, input_data: list) -> list:
        """Efficiently process a batch using cached results where applicable."""
        results = []
        for item in input_data:
            # Convert to tuple for hashability in cache
            data_tuple = tuple(item) if isinstance(item, list) else (item,)
            results.append(self.expensive_transformation(data_tuple))
        return results