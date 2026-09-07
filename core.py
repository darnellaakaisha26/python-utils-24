import time
from typing import Any, Callable, Dict, Hashable, List, Tuple


class FastTaskRunner:
    """Core task execution engine optimized with LRU caching and batching."""

    def __init__(self, max_cache_size: int = 1024):
        self.max_cache_size = max_cache_size
        self._cache: Dict[Hashable, Tuple[float, Any]] = {}

    def memoized_run(
        self, func: Callable, *args: Any, ttl: float = 60.0, **kwargs: Any
    ) -> Any:
        """Execute a function or return cached result if within TTL."""
        kw_tuple = tuple(sorted(kwargs.items()))
        key = (func.__name__, args, kw_tuple)
        now = time.time()

        if key in self._cache:
            timestamp, result = self._cache[key]
            if now - timestamp < ttl:
                return result

        result = func(*args, **kwargs)

        if len(self._cache) >= self.max_cache_size:
            oldest_key = min(self._cache, key=lambda k: self._cache[k][0])
            del self._cache[oldest_key]

        self._cache[key] = (now, result)
        return result

    def batch_process(
        self, func: Callable, items: List[Any], chunk_size: int = 100
    ) -> List[Any]:
        """Process items in optimized chunks to minimize execution overhead."""
        results = []
        for i in range(0, len(items), chunk_size):
            chunk = items[i : i + chunk_size]
            results.extend([func(item) for item in chunk])
        return results

    def clear_cache(self) -> None:
        """Clear all cached evaluation results."""
        self._cache.clear()
