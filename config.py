import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application configuration settings."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update a configuration value."""
        self._config[key] = value

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Load configuration from environment variables with a prefix."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value

    def __repr__(self) -> str:
        return f"ConfigManager(keys={list(self._config.keys())})"