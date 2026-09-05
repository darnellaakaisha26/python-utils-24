import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility to load JSON configuration with default fallbacks."""

    def __init__(self, defaults: Dict[str, Any]):
        self.defaults = defaults

    def load(self, filepath: str) -> Dict[str, Any]:
        """Reads config file and merges with internal defaults."""
        config = self.defaults.copy()

        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

        return config

# Example usage:
# loader = ConfigLoader({"host": "localhost", "port": 8080})
# settings = loader.load("config.json")