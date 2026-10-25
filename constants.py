import os
import logging
from pathlib import Path

# Application path definitions
BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

# System default configurations
DEFAULT_ENCODING = "utf-8"
TIMEOUT_SECONDS = 30
MAX_RETRIES = 3

# Logging configuration constants
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

# Environment variable keys
ENV_PREFIX = "APP_"
DB_URL_KEY = f"{ENV_PREFIX}DATABASE_URL"
API_KEY_NAME = f"{ENV_PREFIX}API_KEY"

# Supported file extensions for processing
SUPPORTED_EXTENSIONS = {'.json', '.yaml', '.csv', '.txt'}

def get_env_var(key: str, default: str = None) -> str:
    """Retrieve environment variable with fallback."""
    return os.getenv(key, default)

# Ensure log directory exists on import
if not LOG_DIR.exists():
    LOG_DIR.mkdir(parents=True, exist_ok=True)