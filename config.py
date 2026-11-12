import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application configuration loading and access."""
    
    def __init__(self, default_path: str = ".env"):
        self._config: Dict[str, Any] = {}
        self.default_path = default_path

    def load_from_env(self) -> None:
        """Loads environment variables into memory."""
        self._config = {key: value for key, value in os.environ.items()}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves config value with fallback."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Updates config value."""
        self._config[key] = value

def get_default_config() -> ConfigManager:
    """Factory for config manager instance."""
    manager = ConfigManager()
    manager.load_from_env()
    return manager