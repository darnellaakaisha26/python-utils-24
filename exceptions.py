"""Custom exception hierarchy for utility operations."""

from typing import Any, Dict, Optional


class BaseUtilError(Exception):
    """Base exception class for all library errors."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        """Return exception information as a structured dictionary."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (details: {self.details})"
        return self.message


class ValidationError(BaseUtilError):
    """Raised when data validation fails."""

    pass


class ConfigurationError(BaseUtilError):
    """Raised when invalid configuration parameters are provided."""

    pass


class ProcessingError(BaseUtilError):
    """Raised when a core processing step encounters an error."""

    pass


class ResourceNotFoundError(BaseUtilError):
    """Raised when a requested resource cannot be located."""

    def __init__(self, resource_name: str, resource_id: Any) -> None:
        message = f"Resource '{resource_name}' with identifier '{resource_id}' was not found."
        super().__init__(
            message,
            details={"resource_name": resource_name, "resource_id": resource_id},
        )
