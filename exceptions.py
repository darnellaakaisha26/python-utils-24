class DataProcessingError(Exception):
    """Base exception for data handling operations."""
    pass

class ValidationError(DataProcessingError):
    """Raised when data fails schema validation."""
    pass

class TransformationError(DataProcessingError):
    """Raised when data transformation fails."""
    pass

class DataHandlerException(DataProcessingError):
    """Generic exception for handler-specific failures."""
    def __init__(self, message: str, context: dict = None):
        super().__init__(message)
        self.context = context or {}

    def __str__(self) -> str:
        if self.context:
            return f"{super().__str__()} (context: {self.context})"
        return super().__str__()