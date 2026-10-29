import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading and merging configuration files with defaults."""

    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads json config and merges with instance defaults."""
        config = self.defaults.copy()
        
        if not os.path.exists(filepath):
            return config
            
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    config.update(data)
        except (json.JSONDecodeError, IOError):
            pass
            
        return config

def get_config(filepath: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    """Helper function for quick config access."""
    loader = ConfigLoader(defaults)
    return loader.load(filepath)