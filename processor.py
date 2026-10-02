import functools
import itertools
from typing import Any, Callable, Generator, Iterable, List, Sequence


class DataProcessor:
    """Efficient data stream processor with batching and caching optimizations."""

    def __init__(self, batch_size: int = 1000):
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size

    def chunk_iterable(self, iterable: Iterable[Any]) -> Generator[List[Any], None, None]:
        """Yield successive n-sized chunks from an iterable without loading all in memory."""
        iterator = iter(iterable)
        while True:
            chunk = list(itertools.islice(iterator, self.batch_size))
            if not chunk:
                break
            yield chunk

    @functools.lru_cache(maxsize=1024)
    def cached_transform(self, item: Any, transform_fn: Callable[[Any], Any]) -> Any:
        """Apply transformation with caching for repetitive high-cost inputs."""
        return transform_fn(item)

    def process_stream(
        self, iterable: Iterable[Any], transform_fn: Callable[[Any], Any]
    ) -> Generator[Any, None, None]:
        """Process large data stream efficiently by batching and applying cached transformations."""
        for chunk in self.chunk_iterable(iterable):
            for item in chunk:
                yield self.cached_transform(item, transform_fn)

    def process_in_batches(
        self, items: Sequence[Any], batch_func: Callable[[List[Any]], List[Any]]
    ) -> List[Any]:
        """Process fixed-size batches using optimized bulk execution callback."""
        results = []
        for chunk in self.chunk_iterable(items):
            batch_result = batch_func(chunk)
            results.extend(batch_result)
        return results
