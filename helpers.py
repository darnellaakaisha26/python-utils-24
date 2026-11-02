import functools
import random
import time
from typing import Any, Callable, Tuple, Type


def retry_on_exception(
    retries: int = 3,
    backoff_factor: float = 1.0,
    jitter: bool = True,
    exceptions: Tuple[Type[Exception], ...] = (Exception,),
) -> Callable:
    """Decorator to retry a network or standard function call with exponential backoff.

    :param retries: Maximum number of attempts before raising the exception.
    :param backoff_factor: Multiplier for exponential backoff delay.
    :param jitter: Adds random variation to sleep time to prevent thundering herds.
    :param exceptions: Tuple of exception types to catch and retry.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    attempt += 1
                    if attempt >= retries:
                        raise exc

                    # Calculate exponential backoff delay
                    delay = backoff_factor * (2 ** (attempt - 1))
                    if jitter:
                        delay += random.uniform(0, 0.1 * delay)

                    time.sleep(delay)

        return wrapper

    return decorator
