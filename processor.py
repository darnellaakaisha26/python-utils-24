import functools
from typing import Callable, Any, Dict

# Cache for compute-intensive transformations
_transformation_cache: Dict[tuple, Any] = {}

def memoize_transform(func: Callable) -> Callable:
    """Decorator to cache function results based on arguments."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _transformation_cache:
            _transformation_cache[key] = func(*args, **kwargs)
        return _transformation_cache[key]
    return wrapper

class DataProcessor:
    """High-performance data processor for batch operations."""
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size

    @memoize_transform
    def transform_record(self, record: dict) -> dict:
        """Process individual record with cached transformations."""
        return {k: v.strip().lower() if isinstance(v, str) else v 
                for k, v in record.items()}

    def process_batch(self, data: list) -> list:
        """Execute batch processing using optimized path."""
        results = []
        for i in range(0, len(data), self.batch_size):
            batch = data[i:i + self.batch_size]
            results.extend([self.transform_record(r) for r in batch])
        return results