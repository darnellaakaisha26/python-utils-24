class BaseUtilError(Exception):
    """Base exception for the python-utils-24 package."""
    pass

class ConfigurationError(BaseUtilError):
    """Raised when config validation fails."""
    pass

class ValidationError(BaseUtilError):
    """Raised when input validation fails."""
    pass

class ProcessingError(BaseUtilError):
    """Raised during data transformation failures."""
    pass

def raise_if_none(value, message="Value cannot be None"):
    """Helper to enforce non-null requirements."""
    if value is None:
        raise ValidationError(message)
    return value

def wrap_exception(func):
    """Decorator to catch errors and re-raise as BaseUtilError."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, BaseUtilError):
                raise
            raise BaseUtilError(f"Operation failed: {str(e)}") from e
    return wrapper