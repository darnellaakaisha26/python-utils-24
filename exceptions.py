"""
Custom exceptions for python-utils-24 library.
Provides structured error handling for common edge cases.
"""

class UtilsError(Exception):
    """Base exception for all errors raised by the utility library."""
    pass

class ValidationError(UtilsError):
    """Raised when data validation fails during runtime checks."""
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value

class ConfigurationError(UtilsError):
    """Raised when a required configuration value is missing or invalid."""
    pass

class TimeoutError(UtilsError):
    """Raised when an operation exceeds its designated execution time limit."""
    def __init__(self, message, elapsed_time=None):
        super().__init__(message)
        self.elapsed_time = elapsed_time

class NetworkRetryError(UtilsError):
    """Raised when a network operation fails persistently after retrying."""
    def __init__(self, message, attempt_count=0):
        super().__init__(message)
        self.attempt_count = attempt_count
