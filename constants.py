from typing import Final, Dict

# Standard error exit codes for application lifecycle management
EXIT_SUCCESS: Final[int] = 0
EXIT_FAILURE: Final[int] = 1
EXIT_INVALID_CONFIG: Final[int] = 2
EXIT_NETWORK_TIMEOUT: Final[int] = 3

# Mapping of exception types to human-readable error messages
ERROR_MESSAGES: Final[Dict[str, str]] = {
    "connection_error": "Failed to establish network connection. Please check your firewall.",
    "config_error": "Configuration file missing or contains invalid syntax.",
    "timeout_error": "Operation timed out while waiting for a response.",
    "permission_error": "Insufficient permissions to access the required resource.",
    "unexpected_error": "An unforeseen error occurred. Please contact the administrator."
}

# Thresholds for resource monitoring to prevent memory exhaustion
MAX_RETRY_ATTEMPTS: Final[int] = 5
DEFAULT_TIMEOUT_SECONDS: Final[float] = 30.0
MAX_BUFFER_SIZE_BYTES: Final[int] = 1048576  # 1MB limit for buffers

# System wide configuration status flags
IS_DEBUG_MODE: Final[bool] = False
DEFAULT_ENCODING: Final[str] = "utf-8"

def get_error_message(key: str) -> str:
    """Return safe error description from constant mapping."""
    return ERROR_MESSAGES.get(key, ERROR_MESSAGES["unexpected_error"])
