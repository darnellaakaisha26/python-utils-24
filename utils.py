import time
import random
import logging
from functools import wraps
from typing import Callable, Any, Type, Tuple, Union

logger = logging.getLogger(__name__)


def retry(
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = Exception,
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    jitter: bool = True,
) -> Callable:
    """
    Decorator to retry a function call with exponential backoff.

    :param exceptions: Exception or tuple of exceptions to catch and retry.
    :param tries: Total number of attempts (minimum 1).
    :param delay: Initial delay between retries in seconds.
    :param backoff: Multiplier applied to delay after each failure.
    :param jitter: If True, adds randomness to prevent thundering herd issues.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(
                            f"Function '{func.__name__}' failed after {tries} attempts. "
                            f"Last error: {e}"
                        )
                        raise

                    sleep_time = current_delay
                    if jitter:
                        # Apply random variation to prevent synchronized retries
                        sleep_time *= random.uniform(0.5, 1.5)

                    logger.warning(
                        f"Attempt {attempt}/{tries} failed for '{func.__name__}': {e}. "
                        f"Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    current_delay *= backoff

        return wrapper

    return decorator
