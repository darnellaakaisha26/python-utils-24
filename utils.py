import time
import random
from functools import wraps
from typing import Callable, Any, Tuple, Type

def retry(
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
    tries: int = 4,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True
) -> Callable:
    """
    Decorator to retry a function with exponential backoff and jitter.

    :param exceptions: Exception(s) that trigger a retry.
    :param tries: Total number of attempts before giving up.
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    :param jitter: If True, adds random variation to the delay.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    sleep_time = _delay
                    if jitter:
                        sleep_time *= random.uniform(0.5, 1.5)
                    time.sleep(sleep_time)
                    _tries -= 1
                    _delay *= backoff
            # Final attempt that raises the error if it fails
            return func(*args, **kwargs)
        return wrapper
    return decorator
