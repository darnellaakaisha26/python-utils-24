from typing import Final, Dict, List

# Application configuration constants
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported environment settings
ENV_PRODUCTION: Final[str] = "production"
ENV_DEVELOPMENT: Final[str] = "development"

# Allowed content types for API communication
ALLOWED_CONTENT_TYPES: Final[List[str]] = [
    "application/json",
    "application/xml",
    "text/plain"
]

# Default mapping for logging levels
LOG_LEVEL_MAP: Final[Dict[str, int]] = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50
}

def get_timeout_buffer(base: int = DEFAULT_TIMEOUT) -> float:
    """
    Calculate timeout buffer based on default constants.

    :param base: The base timeout duration in seconds
    :return: Calculated buffer as a float
    """
    return float(base * 1.1)