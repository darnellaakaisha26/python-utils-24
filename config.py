import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application configuration loading and access."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config = defaults or {}

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Loads configuration values from environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Sets a configuration value."""
        self._config[key] = value

    def update(self, new_config: Dict[str, Any]) -> None:
        """Updates the internal configuration dictionary."""
        self._config.update(new_config)

    def reset(self) -> None:
        """Clears all configuration settings."""
        self._config.clear()

config = ConfigManager()