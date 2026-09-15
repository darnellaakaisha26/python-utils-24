import functools
from typing import Callable, Any, Dict

_memoization_cache: Dict[tuple, Any] = {}

def memoize_validator(func: Callable) -> Callable:
    """Performance optimization for repeated validation checks."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key not in _memoization_cache:
            _memoization_cache[key] = func(*args, **kwargs)
        return _memoization_cache[key]
    return wrapper

@memoize_validator
def validate_schema_structure(data: dict) -> bool:
    """Checks basic dictionary schema constraints efficiently."""
    if not isinstance(data, dict):
        return False
    return len(data) > 0 and all(isinstance(k, str) for k in data.keys())

def clear_validation_cache() -> None:
    """Resets cache to manage memory footprint."""
    _memoization_cache.clear()

class ValidationRegistry:
    """Thread-safe registry for validator management."""
    def __init__(self):
        self._validators = {}

    def register(self, name: str, func: Callable):
        self._validators[name] = func

    def run(self, name: str, *args, **kwargs) -> Any:
        validator = self._validators.get(name)
        if validator:
            return validator(*args, **kwargs)
        raise ValueError(f"Validator {name} not found")