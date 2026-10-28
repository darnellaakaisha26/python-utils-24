"""Custom exception hierarchy for utility operations."""

from typing import Any, Dict, Optional


class BaseUtilError(Exception):
    """Base exception class for all errors in python-utils-24."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message: str = message
        self.details: Dict[str, Any] = details if details is not None else {}

    def to_dict(self) -> Dict[str, Any]:
        """Serialize error details into a standard dictionary format."""
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class ValidationError(BaseUtilError):
    """Raised when data or argument validation fails."""

    def __init__(
        self,
        message: str,
        invalid_field: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None,
    ) -> None:
        details_map = details.copy() if details else {}
        if invalid_field:
            details_map["invalid_field"] = invalid_field
        super().__init__(message, details=details_map)


class ConfigurationError(BaseUtilError):
    """Raised when a configuration value is missing or invalid."""

    def __init__(self, message: str, config_key: Optional[str] = None) -> None:
        details = {"config_key": config_key} if config_key else None
        super().__init__(message, details=details)


class ResourceNotFoundError(BaseUtilError):
    """Raised when a requested resource cannot be located."""

    def __init__(self, resource_type: str, resource_id: str) -> None:
        message = f"{resource_type} with ID '{resource_id}' was not found."
        super().__init__(
            message, details={"resource_type": resource_type, "resource_id": resource_id}
        )
