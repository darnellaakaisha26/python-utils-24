import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self.defaults = default_config

    def load(self, path: str) -> Dict[str, Any]:
        """Loads configuration from a file or returns defaults."""
        if not os.path.exists(path):
            return self.defaults

        try:
            with open(path, 'r', encoding='utf-8') as f:
                user_config = json.load(f)
                return {**self.defaults, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.defaults

    @staticmethod
    def save(path: str, config: Dict[str, Any]) -> None:
        """Persists configuration dictionary to a JSON file."""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)