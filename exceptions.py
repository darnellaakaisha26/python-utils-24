"""Custom exception classes and formatting utilities for general operations."""

import traceback
from typing import Optional, Type


class UtilError(Exception):
    """Base exception class for all library-specific errors."""

    def __init__(self, message: str, original_exception: Optional[Exception] = None) -> None:
        super().__init__(message)
        self.original_exception = original_exception


class ValidationError(UtilError):
    """Raised when a validation check fails on input data."""


class ConfigurationError(UtilError):
    """Raised when configuration properties are missing or malformed."""


class OperationTimeoutError(UtilError):
    """Raised when a timed operation exceeds its allocated duration."""


def format_exception_info(exc: Exception, include_traceback: bool = False) -> str:
    """Format an exception into a structured and readable string.

    Args:
        exc: The exception instance to format.
        include_traceback: If True, appends the traceback block.
    """
    exc_type: Type[BaseException] = type(exc)
    msg = f"{exc_type.__name__}: {str(exc)}"

    if include_traceback and exc.__traceback__:
        tb = traceback.format_exception(exc_type, exc, exc.__traceback__)
        msg += "\nTraceback (most recent call last):\n" + "".join(tb)

    return msg
