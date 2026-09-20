import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with fallback defaults."""

    def __init__(self, default_config: Dict[str, Any] = None):
        self.defaults = default_config or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration file and merges with default values."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError):
            pass

        return config

def get_config(filepath: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Shortcut function to initialize and load config."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)