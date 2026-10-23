class UtilityError(Exception):
    """Base exception for python-utils-24 operations."""

class ConfigurationError(UtilityError):
    """Raised when configuration constraints are violated."""

class ProcessingError(UtilityError):
    """Raised when data processing fails."""

def handle_exceptions(func):
    """Decorator to wrap functions with standard error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            raise ProcessingError(f"Processing failed: {str(e)}") from e
        except Exception as e:
            # Log unexpected errors before re-raising
            print(f"Critical failure in {func.__name__}: {e}")
            raise UtilityError("An unexpected utility error occurred") from e
    return wrapper

def validate_input(value, expected_type):
    """Utility for enforcing type safety on edge inputs."""
    if value is None:
        raise ConfigurationError("Input value cannot be None")
    if not isinstance(value, expected_type):
        raise ProcessingError(f"Expected {expected_type}, got {type(value)}")
    return True