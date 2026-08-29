import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """A simple configuration loader that supports defaults, JSON file, and environment overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None, config_file: Optional[str] = None) -> None:
        self.defaults = defaults or {}
        self.config_file = config_file or os.getenv("CONFIG_FILE", "config.json")
        self._config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load config by merging defaults, file contents, and env vars."""
        config = self.defaults.copy()
        if os.path.isfile(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    file_data = json.load(f)
                    if isinstance(file_data, dict):
                        config.update(file_data)
            except (IOError, json.JSONDecodeError):
                pass

        for key, value in list(config.items()):
            env_key = key.upper().replace(".", "_")
            if env_key in os.environ:
                env_value = os.environ[env_key]
                config[key] = self._parse_env_value(env_value)
        return config

    def _parse_env_value(self, value: str) -> Any:
        """Parse environment value to appropriate type."""
        if value.lower() == "true":
            return True
        if value.lower() == "false":
            return False
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value."""
        return self._config.get(key, default)

    def get_all(self) -> Dict[str, Any]:
        """Return a copy of the entire configuration."""
        return self._config.copy()

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value (in memory)."""
        self._config[key] = value

    def save(self, path: Optional[str] = None) -> None:
        """Save current config to a JSON file."""
        save_path = path or self.config_file
        try:
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(self._config, f, indent=2)
        except IOError:
            pass

def load_config(defaults: Optional[Dict[str, Any]] = None, config_file: Optional[str] = None) -> ConfigLoader:
    """Convenience function to load configuration."""
    return ConfigLoader(defaults, config_file)
