import functools
import time
from typing import Callable, Any

# internal cache for high-frequency utility lookups
_PERFORMANCE_CACHE = {}

def memoize_core(func: Callable) -> Callable:
    """decorator for caching expensive core processing results"""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _PERFORMANCE_CACHE:
            _PERFORMANCE_CACHE[key] = func(*args, **kwargs)
        return _PERFORMANCE_CACHE[key]
    return wrapper

@memoize_core
def batch_process_data(data_size: int) -> list:
    """simulated heavy processing task with cached output"""
    time.sleep(0.5)
    return [i * 2 for i in range(data_size)]

class CoreProcessor:
    def __init__(self, buffer_size: int = 1024):
        self.buffer = [None] * buffer_size
        self.pointer = 0

    def update_buffer(self, item: Any) -> None:
        """optimized circular buffer write operation"""
        self.buffer[self.pointer] = item
        self.pointer = (self.pointer + 1) % len(self.buffer)