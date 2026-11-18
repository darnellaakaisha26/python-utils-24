from typing import Optional, Any

class BaseUtilsError(Exception):
    """Base exception for the python-utils-24 package."""
    pass

class ConfigurationError(BaseUtilsError):
    """Raised when the provided configuration is invalid."""
    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.details = details

class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""
    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"Validation failed for {field}: {reason}")
        self.field = field
        self.reason = reason

class ProcessingError(BaseUtilsError):
    """Raised during data transformation or processing cycles."""
    def __init__(self, message: str, source: Optional[str] = None) -> None:
        super().__init__(message)
        self.source = source

def raise_if_none(value: Optional[Any], name: str) -> None:
    """Raises ValidationError if the provided value is None."""
    if value is None:
        raise ValidationError(name, "value cannot be None")