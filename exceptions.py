"""Custom exception classes for python-utils-24.

Provides a structured exception hierarchy to handle validation, configuration,
and operational failures gracefully.
"""

from typing import Any, Dict, Optional


class UtilsError(Exception):
    """Base exception for all errors raised by the utility library."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def __str__(self) -> str:
        if self.details:
            return f"{self.message} (details: {self.details})"
        return self.message


class ValidationError(UtilsError):
    """Raised when data validation checks fail."""

    def __init__(
        self, message: str, field: Optional[str] = None, value: Any = None
    ) -> None:
        details = {}
        if field is not None:
            details["field"] = field
        if value is not None:
            details["value"] = value
        super().__init__(message, details=details if details else None)


class ConfigError(UtilsError):
    """Raised when a configuration key or format is invalid."""

    pass


class ProcessError(UtilsError):
    """Raised when a background process or system command fails."""

    def __init__(
        self, 
        message: str, 
        exit_code: Optional[int] = None, 
        stderr: Optional[str] = None
    ) -> None:
        details = {}
        if exit_code is not None:
            details["exit_code"] = exit_code
        if stderr is not None:
            details["stderr"] = stderr
        super().__init__(message, details=details if details else None)
