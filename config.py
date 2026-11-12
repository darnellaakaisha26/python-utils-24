import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and merging of application configurations."""

    def __init__(self, env_prefix: str = "APP_"):
        self.env_prefix = env_prefix

    def load_from_env(self) -> Dict[str, str]:
        """Extracts environment variables matching the prefix."""
        return {
            key[len(self.env_prefix):].lower(): value
            for key, value in os.environ.items()
            if key.startswith(self.env_prefix)
        }

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves configuration with fallback to environment."""
        config = self.load_from_env()
        return config.get(key.lower(), default)

class AppConfig:
    """Global application configuration storage."""
    _settings: Dict[str, Any] = {"debug": False, "version": "24.0.0"}

    @classmethod
    def update(cls, new_settings: Dict[str, Any]) -> None:
        """Updates global settings with new dictionary."""
        cls._settings.update(new_settings)

    @classmethod
    def get(cls, key: str) -> Any:
        """Returns value for given configuration key."""
        return cls._settings.get(key)