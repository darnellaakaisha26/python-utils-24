class UtilsError(Exception):
    """Base exception for python-utils-24 operations."""

class ConfigurationError(UtilsError):
    """Raised when configuration loading or parsing fails."""

class ValidationError(UtilsError):
    """Raised when data fails a validation check."""

class ProcessingError(UtilsError):
    """Raised when a data processor encounters an issue."""

def handle_exception(exc: Exception) -> None:
    """Centralized exception reporting helper."""
    import sys
    import logging

    logger = logging.getLogger('python-utils-24')
    if isinstance(exc, UtilsError):
        logger.error(f"Utility operation failed: {exc}")
    else:
        logger.exception("Unexpected system error occurred")

def raise_if_none(value, name: str):
    """Ensures value is not None to avoid downstream errors."""
    if value is None:
        raise ValidationError(f"Required parameter '{name}' cannot be None")
    return value