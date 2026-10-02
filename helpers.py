import time
from typing import Iterable, Any, Type, Callable, Generator

def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[list[Any], None, None]:
    """Yield successive n-sized chunks from an iterable."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def get_nested(data: dict[str, Any], path: str, default: Any = None) -> Any:
    """Retrieve nested dictionary values using a dot-separated path."""
    keys = path.split('.')
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def retry(retries: int = 3, delay: float = 1.0, exceptions: tuple[Type[Exception], ...] = (Exception,)) -> Callable:
    """Decorator that retries a function call on failure."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_error = e
                    if attempt < retries - 1:
                        time.sleep(delay)
            if last_error:
                raise last_error
        return wrapper
    return decorator