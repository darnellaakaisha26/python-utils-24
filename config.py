import json
import os
from typing import Any, Dict, Optional

class ConfigLoader:
    """Handles loading and merging of configuration files with defaults."""

    def __init__(self, default_config: Dict[str, Any]):
        self.config = default_config

    def load_from_file(self, filepath: str) -> None:
        """Loads json configuration and performs shallow merge with defaults."""
        if not os.path.exists(filepath):
            return

        try:
            with open(filepath, 'r') as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self.config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves value from config or returns a fallback."""
        return self.config.get(key, default)

def load_config(path: str, defaults: Dict[str, Any]) -> ConfigLoader:
    """Factory function to return initialized loader."""
    loader = ConfigLoader(defaults)
    loader.load_from_file(path)
    return loader