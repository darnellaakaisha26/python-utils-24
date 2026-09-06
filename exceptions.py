class UtilsError(Exception):
    """Base exception class for all python-utils-24 errors."""

    def __init__(self, message: str = 'An error occurred in python-utils', *args):
        super().__init__(message, *args)


class ValidationError(UtilsError):
    """Raised when a validation check fails."""

    def __init__(self, message: str = 'Validation failed', field: str = None):
        self.field = field
        full_message = f'{message} (field: {field})' if field else message
        super().__init__(full_message)


class ConfigurationError(UtilsError):
    """Raised when configuration is missing or invalid."""
    pass


class ProcessTimeoutError(UtilsError):
    """Raised when a monitored process exceeds its time limit."""

    def __init__(self, timeout: float, message: str = 'Process timed out'):
        self.timeout = timeout
        full_message = f'{message} after {timeout} seconds'
        super().__init__(full_message)


class ResourceUnavailableError(UtilsError):
    """Raised when a requested resource cannot be accessed."""

    def __init__(self, resource: str, message: str = 'Resource unavailable'):
        self.resource = resource
        full_message = f'{message}: {resource}'
        super().__init__(full_message)
