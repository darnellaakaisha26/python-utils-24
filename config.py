import json
import os
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility for loading and managing configuration settings with default fallbacks."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Update current configuration with dictionary values."""
        self._config.update(data)

    def load_from_file(self, filepath: str) -> None:
        """Load configuration settings from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self.load_from_dict(data)
            else:
                raise ValueError("JSON content must be a top-level object")

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Override configuration values using environment variables."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix) :].lower()
                self._config[config_key] = self._parse_env_value(value)

    @staticmethod
    def _parse_env_value(val: str) -> Union[int, float, bool, str]:
        if val.lower() in ("true", "yes", "1"):
            return True
        if val.lower() in ("false", "no", "0"):
            return False
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            pass
        return val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration parameter."""
        return self._config.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration."""
        return self._config.copy()
