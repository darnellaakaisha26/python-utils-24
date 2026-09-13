import time
from functools import wraps
from typing import Any, Dict, Callable, Type, Tuple, Union

def deep_merge(dict_a: Dict[Any, Any], dict_b: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Recursively merges dict_b into dict_a.

    Values from dict_b will overwrite dict_a if keys conflict and values are not dicts.
    """
    result = dict_a.copy()
    for key, value in dict_b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def retry(
    exceptions: Union[Type[BaseException], Tuple[Type[BaseException], ...]],
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
) -> Callable:
    """
    Decorator that retries a function if specified exceptions are raised.

    Uses exponential backoff by default.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt, current_delay = 0, delay
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt >= tries:
                        raise e
                    time.sleep(current_delay)
                    current_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator