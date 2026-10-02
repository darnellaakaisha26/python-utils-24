import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """A utility class to load, merge, and retrieve configuration settings with defaults."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._defaults = defaults or {}
        self._config = self._defaults.copy()

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        """Merges the provided dictionary configuration with the defaults."""
        self._config.update(data)

    def load_from_json(self, filepath: str) -> None:
        """Loads configuration from a JSON file and merges it with current values."""
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self.load_from_dict(data)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value.

        Supports nested keys separated by dots (e.g., 'database.host').
        """
        parts = key.split(".")
        current: Any = self._config

        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default

        return current

    @property
    def config(self) -> Dict[str, Any]:
        """Returns a copy of the active configuration."""
        return self._config.copy()
