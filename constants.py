import os
import logging
from pathlib import Path

# Application path definitions
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"

# Standardized date/time formats
ISO_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

# Network and environment constants
DEFAULT_TIMEOUT = 30
MAX_RETRIES = 3
ENV_PREFIX = "PY_UTILS"

# Logging configuration constants
LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

def get_env_variable(key: str, default: str = None) -> str:
    """Fetch environment variable with prefixed key."""
    full_key = f"{ENV_PREFIX}_{key.upper()}"
    return os.getenv(full_key, default)

# HTTP status code references
HTTP_OK = 200
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

# Generic character sets
ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
REQUIRED_FIELDS = ["id", "timestamp", "payload"]