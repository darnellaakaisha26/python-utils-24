"""Custom exception classes for the python-utils-24 library."""

from typing import Any, Dict, Optional


class BaseUtilError(Exception):
    """Base exception class for all errors raised by the utility package."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: Dict[str, Any] = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Return a structured dictionary representation of the exception."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(BaseUtilError):
    """Raised when data validation fails for an input value."""

    def __init__(
        self, message: str, invalid_value: Any = None, field_name: Optional[str] = None
    ) -> None:
        details: Dict[str, Any] = {}
        if invalid_value is not None:
            details["invalid_value"] = str(invalid_value)
        if field_name is not None:
            details["field_name"] = field_name
        super().__init__(message, details=details)


class ConfigurationError(BaseUtilError):
    """Raised when a configuration parameter is missing or invalid."""

    def __init__(self, config_key: str, message: str) -> None:
        details: Dict[str, Any] = {"config_key": config_key}
        full_msg: str = f"Configuration error for '{config_key}': {message}"
        super().__init__(full_msg, details=details)


class ResourceNotFoundError(BaseUtilError):
    """Raised when a requested resource or file cannot be located."""

    def __init__(self, resource_id: str, resource_type: str = "resource") -> None:
        details: Dict[str, Any] = {
            "resource_id": resource_id,
            "resource_type": resource_type,
        }
        super().__init__(
            f"{resource_type.capitalize()} '{resource_id}' was not found.",
            details=details,
        )
