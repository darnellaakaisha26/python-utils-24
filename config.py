import os
from typing import Any, Dict

class Config:
    """Centralized configuration management for python-utils-24"""

    def __init__(self, env_prefix: str = "UTILS_"):
        self._prefix = env_prefix
        self._settings: Dict[str, Any] = {}
        self._load_defaults()

    def _load_defaults(self) -> None:
        """Initialize base configuration from environment variables"""
        self._settings = {
            "LOG_LEVEL": os.getenv(f"{self._prefix}LOG_LEVEL", "INFO"),
            "MAX_RETRIES": int(os.getenv(f"{self._prefix}MAX_RETRIES", "3")),
            "TIMEOUT": float(os.getenv(f"{self._prefix}TIMEOUT", "30.0")),
        }

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a configuration value by key"""
        return self._settings.get(key, default)

    def update(self, new_settings: Dict[str, Any]) -> None:
        """Update existing configuration with provided dictionary"""
        self._settings.update(new_settings)

def get_config() -> Config:
    """Factory function to retrieve global configuration"""
    if not hasattr(get_config, "_instance"):
        get_config._instance = Config()
    return get_config._instance