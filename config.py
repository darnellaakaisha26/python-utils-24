import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles configuration loading from environment variables."""

    def __init__(self, prefix: str = "APP_") -> None:
        self.prefix: str = prefix
        self._cache: Dict[str, str] = {}

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Retrieve a configuration value with an optional default."""
        env_key: str = f"{self.prefix}{key.upper()}"
        return os.environ.get(env_key, default)

    def get_int(self, key: str, default: int) -> int:
        """Retrieve an integer configuration value."""
        value: Optional[str] = self.get(key)
        try:
            return int(value) if value is not None else default
        except (ValueError, TypeError):
            return default

    def load_all(self) -> Dict[str, str]:
        """Return all configuration values matching the prefix."""
        if not self._cache:
            self._cache = {
                k[len(self.prefix):].lower(): v
                for k, v in os.environ.items()
                if k.startswith(self.prefix)
            }
        return self._cache