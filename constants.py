import sys
from functools import lru_cache

# Global constants for library performance optimization
# Using slots and lru_cache to reduce memory footprint

CACHE_SIZE = 1024

@lru_cache(maxsize=CACHE_SIZE)
def get_system_platform():
    """Cached retrieval of platform information."""
    return sys.platform

class OptimizationConfig:
    """Config container using slots to prevent __dict__ overhead."""
    __slots__ = ('buffer_size', 'timeout', 'retry_limit')

    def __init__(self, buffer_size: int = 4096, timeout: float = 30.0, retry_limit: int = 3):
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.retry_limit = retry_limit

# Pre-computed defaults for high-frequency operations
DEFAULT_CONFIG = OptimizationConfig()

def get_optimized_buffer_size() -> int:
    """Return the base buffer size for core operations."""
    return DEFAULT_CONFIG.buffer_size

# Ensure clean constant access patterns across the package
PLATFORM = get_system_platform()