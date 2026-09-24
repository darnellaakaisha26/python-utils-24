"""Custom exceptions module for package error handling."""

from typing import Optional


class UtilsError(Exception):
    """Base exception class for all library-specific errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class ValidationError(UtilsError):
    """Exception raised when value validation checks fail."""

    def __init__(self, message: str, field: Optional[str] = None) -> None:
        detailed_message = f"Validation failed for '{field}': {message}" if field else message
        super().__init__(detailed_message)
        self.field = field


class ConfigurationError(UtilsError):
    """Exception raised for missing or incorrect configurations."""


class ProcessingError(UtilsError):
    """Exception raised when an operation fails during execution."""

    def __init__(self, message: str, cause: Optional[Exception] = None) -> None:
        super().__init__(message)
        if cause:
            self.__cause__ = cause
