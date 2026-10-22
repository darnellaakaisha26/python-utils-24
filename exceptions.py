from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception class for python-utils-24 package."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class ConfigurationError(BaseUtilsError):
    """Raised when configuration settings are invalid or missing."""
    pass

class ValidationError(BaseUtilsError):
    """Raised when input data fails validation requirements."""
    def __init__(self, message: str, field: Optional[str] = None) -> None:
        super().__init__(message)
        self.field = field

class ProcessingError(BaseUtilsError):
    """Raised during internal processing logic failures."""
    def __init__(self, message: str, context: Optional[Any] = None) -> None:
        super().__init__(message)
        self.context = context

def raise_error(error_type: type[BaseUtilsError], message: str, **kwargs: Any) -> None:
    """Helper function to instantiate and raise custom package exceptions."""
    raise error_type(message, **kwargs)