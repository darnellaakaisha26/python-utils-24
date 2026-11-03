import os
from typing import Final

# Application configuration defaults
APP_NAME: Final[str] = "python-utils-24"
DEFAULT_LOG_LEVEL: Final[str] = "INFO"
MAX_RETRIES: Final[int] = 3
TIMEOUT_SECONDS: Final[int] = 30

# File system paths
BASE_DIR: Final[str] = os.path.dirname(os.path.abspath(__file__))
LOG_DIR: Final[str] = os.path.join(BASE_DIR, "logs")
DATA_DIR: Final[str] = os.path.join(BASE_DIR, "data")

# Regex patterns
EMAIL_PATTERN: Final[str] = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

# Exit codes
SUCCESS: Final[int] = 0
ERROR_GENERAL: Final[int] = 1
ERROR_CONFIG: Final[int] = 2

def get_env_variable(key: str, default: str) -> str:
    """Fetch environment variable with a fallback."""
    return os.getenv(key, default)

# Ensure directories exist
for directory in [LOG_DIR, DATA_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)