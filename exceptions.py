from typing import Optional, Any

class UtilsError(Exception):
    """Base exception class for python-utils-24."""
    def __init__(self, message: str, context: Optional[Any] = None) -> None:
        super().__init__(message)
        self.context = context

class ValidationError(UtilsError):
    """Raised when validation logic fails."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration settings are invalid."""
    pass

class ProcessingError(UtilsError):
    """Raised during unexpected processing failures."""
    pass

def raise_error(error_type: type[UtilsError], message: str, context: Any = None) -> None:
    """Helper to raise typed exceptions with optional context."""
    raise error_type(message, context=context)

__all__ = ['UtilsError', 'ValidationError', 'ConfigurationError', 'ProcessingError', 'raise_error']