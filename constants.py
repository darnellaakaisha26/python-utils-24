import os

# Application configuration constants
APP_NAME = "python-utils-24"
DEFAULT_ENCODING = "utf-8"

# File system related paths and limits
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB limit
TEMP_DIR = os.getenv("TEMP_PATH", "/tmp/utils_cache")

# Common time constants
SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600

# Supported patterns and defaults
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DEFAULT_RETRIES = 3

# Network timeout settings
REQUEST_TIMEOUT_SECONDS = 30
CONNECTION_RETRY_DELAY = 1

# Status codes for internal processes
STATUS_SUCCESS = 0
STATUS_ERROR = 1
STATUS_WARNING = 2