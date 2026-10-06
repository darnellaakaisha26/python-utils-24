import time
from functools import wraps
from typing import Any, Dict, Generator, Iterable, Callable

def deep_merge(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    """Recursively merges dict_b into dict_a, returning a new dictionary."""
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[list, None, None]:
    """Yields successive chunks of a given size from an iterable."""
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def retry(retries: int = 3, delay: float = 1.0) -> Callable:
    """Decorator to retry a function call on failure with a delay."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            raise last_exception or RuntimeError("Retry failed")
        return wrapper
    return decorator