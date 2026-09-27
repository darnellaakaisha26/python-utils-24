import functools
import threading
from typing import Any, Callable, Dict

class ConfigRegistry:
    """Thread-safe singleton registry for application configurations."""
    _instance = None
    _lock = threading.Lock()
    _cache: Dict[str, Any] = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ConfigRegistry, cls).__new__(cls)
            return cls._instance

    @functools.lru_cache(maxsize=128)
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Retrieve setting with memoization for performance."""
        return self._cache.get(key, default)

    def set_setting(self, key: str, value: Any) -> None:
        """Update registry and clear cache to ensure consistency."""
        with self._lock:
            self._cache[key] = value
            self.get_setting.cache_clear()

registry = ConfigRegistry()