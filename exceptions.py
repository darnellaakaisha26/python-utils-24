class UtilsError(Exception):
    """Base exception for python-utils-24 package."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration validation fails."""
    pass

class ProcessingError(UtilsError):
    """Raised when data transformation fails."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Helper to enforce non-null constraints."""
    if value is None:
        raise ValueError(message)

def handle_exception(e, logger=None):
    """Standardized exception formatting and logging."""
    error_msg = f"{type(e).__name__}: {str(e)}"
    if logger:
        logger.error(error_msg)
    return error_msg

class Result:
    """Container for operation results with error handling."""
    def __init__(self, data=None, error=None):
        self.data = data
        self.error = error

    @property
    def success(self):
        return self.error is None