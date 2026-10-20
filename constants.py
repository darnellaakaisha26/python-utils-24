import os
from typing import Final

# Application path constants
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Execution defaults
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# System configuration keys
ENV_PREFIX: Final[str] = 'PYUTILS'
REQUIRED_ENV_VARS: Final[list[str]] = ['API_KEY', 'DB_URL']

# Content-type mapping for file processing
SUPPORTED_EXTENSIONS: Final[set[str]] = {'.json', '.csv', '.yaml', '.txt'}

# Formatting defaults
DATE_FORMAT: Final[str] = '%Y-%m-%d %H:%M:%S'
ENCODING: Final[str] = 'utf-8'

def get_abs_path(filename: str) -> str:
    """Return full system path for a local file."""
    return os.path.join(BASE_DIR, filename)

# Status codes for internal handlers
STATUS_SUCCESS: Final[int] = 200
STATUS_ERROR: Final[int] = 500
STATUS_NOT_FOUND: Final[int] = 404