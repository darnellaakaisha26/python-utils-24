import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and retrieval of application configurations."""

    def __init__(self, env_prefix: str = "APP_") -> None:
        self.env_prefix: str = env_prefix
        self._cache: Dict[str, Any] = {}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        Retrieve a configuration value from environment variables or cache.

        Args:
            key: The configuration setting name.
            default: Fallback value if key is not found.

        Returns:
            The configuration value or the provided default.
        """
        if key in self._cache:
            return self._cache[key]

        env_key: str = f"{self.env_prefix}{key.upper()}"
        value: Any = os.getenv(env_key, default)
        self._cache[key] = value
        return value

    def update(self, key: str, value: Any) -> None:
        """
        Manually override a configuration value.

        Args:
            key: Configuration key name.
            value: New configuration value to store.
        """
        self._cache[key] = value

def load_config() -> ConfigLoader:
    """Factory function for creating a standard config loader."""
    return ConfigLoader()