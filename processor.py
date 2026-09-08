import time
import urllib.error
import urllib.request
from typing import Callable, Any, Type, Tuple


def retry_network_operation(
    func: Callable[..., Any],
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (urllib.error.URLError, TimeoutError, ConnectionError),
) -> Any:
    """Executes a network operation with exponential backoff retry logic."""
    current_delay = delay
    for attempt in range(1, max_retries + 1):
        try:
            return func()
        except exceptions as e:
            if attempt == max_retries:
                raise e
            time.sleep(current_delay)
            current_delay *= backoff_factor


def fetch_url_data(url: str, timeout: float = 5.0) -> bytes:
    """Fetches raw data from a URL using retry_network_operation."""
    def _operation():
        req = urllib.request.Request(url, headers={'User-Agent': 'python-utils-24/1.0'})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()

    return retry_network_operation(_operation)
