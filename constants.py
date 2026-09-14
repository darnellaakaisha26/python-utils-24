import os
from typing import Final

# Application path configurations
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, 'logs')

# Default operation timeouts
DEFAULT_TIMEOUT: Final[int] = 30
MAX_RETRIES: Final[int] = 3

# Supported data formats
SUPPORTED_EXTENSIONS: Final[set] = {'.json', '.yaml', '.yml', '.csv'}

# Standard HTTP headers
DEFAULT_HEADERS: Final[dict] = {
    'Content-Type': 'application/json',
    'User-Agent': 'python-utils-24-client'
}

# Error and status messaging templates
STATUS_SUCCESS: Final[str] = 'OPERATION_SUCCESS'
STATUS_FAILURE: Final[str] = 'OPERATION_FAILURE'

class AppDefaults:
    """Container for environmental application defaults."""
    MAX_WORKERS: int = 4
    BUFFER_SIZE: int = 1024
    ENCODING: str = 'utf-8'

def get_timeout() -> int:
    """Retrieve timeout from environment or default."""
    return int(os.getenv('APP_TIMEOUT', DEFAULT_TIMEOUT))