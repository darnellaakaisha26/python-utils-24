from typing import Optional, Any

class UtilsError(Exception):
    """Base exception for the python-utils-24 package."""
    pass

class ConfigurationError(UtilsError):
    """Raised when configuration validation fails."""
    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        self.config_key = config_key
        super().__init__(f"{message} (key: {config_key})" if config_key else message)

class ProcessingError(UtilsError):
    """Raised when a data processor encounters invalid input."""
    def __init__(self, message: str, payload: Any = None) -> None:
        self.payload = payload
        super().__init__(message)

class ValidationError(UtilsError):
    """Raised during schema or data validation failure."""
    def __init__(self, message: str, errors: Optional[list[str]] = None) -> None:
        self.errors = errors or []
        super().__init__(f"{message}: {', '.join(self.errors)}" if self.errors else message)

class TimeoutError(UtilsError):
    """Raised when an operation exceeds defined limits."""
    def __init__(self, message: str, duration: float) -> None:
        self.duration = duration
        super().__init__(f"{message} after {duration}s")