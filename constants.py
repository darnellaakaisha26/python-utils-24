import sys
from typing import Final, Dict, Any

# global constant registry with caching
# using __slots__ or frozen classes for memory efficiency

class CoreConstants:
    """Immutable registry for application-wide constants."""
    __slots__ = ('_data',)

    def __init__(self, data: Dict[str, Any]):
        self._data = data

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

# optimized cache for core lookups
DEFAULT_TIMEOUT: Final[int] = 30
BUFFER_SIZE: Final[int] = 4096

# performance optimized constant dictionary
CACHE_CONFIG: Final[Dict[str, Any]] = {
    "max_size": 1024,
    "ttl": 3600,
    "strategy": "lru"
}

def get_system_defaults() -> Dict[str, Any]:
    """Returns optimized default configuration mapping."""
    return {
        "timeout": DEFAULT_TIMEOUT,
        "buffer": BUFFER_SIZE,
        "platform": sys.platform
    }