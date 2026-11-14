import os
import json
from typing import Any, Dict, Optional


def _deep_update(base: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively update nested dictionary defaults with overrides."""
    for key, value in overrides.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            _deep_update(base[key], value)
        else:
            base[key] = value
    return base


class ConfigLoader:
    """Utility class to load and manage configuration with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Merge a configuration dictionary into current settings."""
        self._config = _deep_update(self._config, config_dict)
        return self._config

    def load_json(self, filepath: str, ignore_missing: bool = True) -> Dict[str, Any]:
        """Load configuration from a JSON file."""
        if not os.path.exists(filepath):
            if ignore_missing:
                return self._config
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            return self.load_from_dict(data)

    def load_env(self, prefix: str = "") -> Dict[str, Any]:
        """Override configuration options from environment variables."""
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            clean_key = key[len(prefix):].lower() if prefix else key.lower()
            try:
                parsed_value = json.loads(value)
            except (json.JSONDecodeError, TypeError):
                parsed_value = value
            self._config[clean_key] = parsed_value
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration option by key with optional fallback."""
        return self._config.get(key, default)

    @property
    def config(self) -> Dict[str, Any]:
        """Get copy of current configuration dictionary."""
        return self._config.copy()
