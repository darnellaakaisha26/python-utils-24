import os
import re

# Standard environmental configurations
DEFAULT_ENCODING = 'utf-8'
DEFAULT_TIMEOUT = 30

# Standard regex patterns
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
URL_REGEX = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

# Logging levels and formats
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Common path constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, 'tmp')

# Exit codes
SUCCESS = 0
ERROR_GENERAL = 1
ERROR_CONFIG = 2

def get_environment_variable(key: str, default: str = None) -> str:
    """Retrieve env var with fallback support."""
    return os.getenv(key, default)

# Configuration dictionary for standard library use
SETTINGS = {
    "encoding": DEFAULT_ENCODING,
    "timeout": DEFAULT_TIMEOUT,
    "base_path": BASE_DIR,
    "temp_path": TEMP_DIR
}