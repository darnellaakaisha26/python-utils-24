import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Handles loading and merging of configuration files."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads json config and merges with defaults."""
        config = self._defaults.copy()
        
        if not os.path.exists(filepath):
            return config

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

def get_config(filepath: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Utility function to simplify config retrieval."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)