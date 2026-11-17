import json
import os
from typing import Any, Dict

class ConfigLoader:
    """Utility for loading JSON configurations with defaults."""
    
    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load(self, filepath: str) -> Dict[str, Any]:
        """Loads configuration from file and merges with defaults."""
        if not os.path.exists(filepath):
            return self.config

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                return {**self.config, **user_config}
        except (json.JSONDecodeError, IOError):
            return self.config

    def update(self, key: str, value: Any, filepath: str) -> None:
        """Persists a single key to the config file."""
        current = self.load(filepath)
        current[key] = value
        with open(filepath, 'w') as f:
            json.dump(current, f, indent=4)