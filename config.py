import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Loads application configuration with fallback default settings."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._defaults = defaults or {}
        self._config = self._defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge a dictionary into the current configuration."""
        self._config.update(data)
        return self.get_all()

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Load configuration from a JSON file and merge with defaults."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.load_from_dict(data)
        return self.get_all()

    def load_from_env(self, prefix: str = "APP_") -> Dict[str, Any]:
        """Override configuration values using environment variables matching prefix."""
        for key in self._config.keys():
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                self._config[key] = os.environ[env_key]
        return self.get_all()

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key."""
        return self._config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """Return the complete merged configuration dictionary."""
        return self._config.copy()
