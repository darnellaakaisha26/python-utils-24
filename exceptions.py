"""Custom exception hierarchy for general utility operations."""

from typing import Any, Dict, Optional


class BaseUtilError(Exception):
    """Base exception class for all library utilities."""

    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.code: Optional[int] = code

    def to_dict(self) -> Dict[str, Any]:
        """Convert exception details into a structured dictionary."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
        }


class ValidationError(BaseUtilError):
    """Raised when input data validation fails."""

    def __init__(self, message: str, field_name: Optional[str] = None) -> None:
        super().__init__(message, code=400)
        self.field_name: Optional[str] = field_name

    def to_dict(self) -> Dict[str, Any]:
        """Include the problematic field name in the error payload."""
        payload: Dict[str, Any] = super().to_dict()
        if self.field_name:
            payload["field_name"] = self.field_name
        return payload


class ConfigurationError(BaseUtilError):
    """Raised when configuration settings are missing or malformed."""

    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        super().__init__(message, code=500)
        self.config_key: Optional[str] = config_key


class ResourceNotFoundError(BaseUtilError):
    """Raised when a requested resource cannot be located."""

    def __init__(self, message: str, resource_id: Optional[str] = None) -> None:
        super().__init__(message, code=404)
        self.resource_id: Optional[str] = resource_id
