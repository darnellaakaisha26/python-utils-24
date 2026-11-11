import enum
from typing import Dict, Any

class ErrorCodes(enum.IntEnum):
    SUCCESS = 0
    INVALID_INPUT = 1001
    TIMEOUT = 1002
    UNAUTHORIZED = 1003
    RESOURCE_NOT_FOUND = 1004
    INTERNAL_SERVER_ERROR = 5000

ERROR_MESSAGES: Dict[int, str] = {
    ErrorCodes.SUCCESS: "Operation successful",
    ErrorCodes.INVALID_INPUT: "The provided input parameters are invalid",
    ErrorCodes.TIMEOUT: "The operation timed out while waiting for a response",
    ErrorCodes.UNAUTHORIZED: "Authentication is required for this action",
    ErrorCodes.RESOURCE_NOT_FOUND: "The requested resource could not be located",
    ErrorCodes.INTERNAL_SERVER_ERROR: "An unexpected error occurred in the system"
}

def get_error_message(code: int) -> str:
    """Retrieve human-readable description for error code."""
    return ERROR_MESSAGES.get(code, ERROR_MESSAGES[ErrorCodes.INTERNAL_SERVER_ERROR])

# Configuration defaults for environment edge cases
DEFAULT_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
MAX_LOG_FILE_SIZE_MB = 10

# Validation boundaries
MIN_PROCESS_COUNT = 1
MAX_PROCESS_COUNT = 64

if __name__ == "__main__":
    # Verification of constant mapping
    assert get_error_message(ErrorCodes.TIMEOUT) == "The operation timed out while waiting for a response"