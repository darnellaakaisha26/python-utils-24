import os
from typing import Any, Dict, Optional


class ConfigManager:
    """A utility class for managing and parsing application configuration safely
    from environment variables or default dictionary fallbacks.
    """

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initializes the ConfigManager with optional default values.

        Args:
            defaults: A dictionary of fallback configuration options.
        """
        self._defaults: Dict[str, Any] = defaults or {}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a configuration value by key.

        Looks up the key in system environment variables first, then defaults.

        Args:
            key: The configuration key to lookup.
            default: A fallback value if the key is not found anywhere.

        Returns:
            The configuration value, or the fallback default.
        """
        env_key = key.upper()
        if env_key in os.environ:
            return os.environ[env_key]
        return self._defaults.get(key, default)

    def get_str(self, key: str, default: str = "") -> str:
        """Retrieves a configuration value cast to a string.

        Args:
            key: The configuration key.
            default: The fallback string if key is not found.

        Returns:
            The configuration value as a string.
        """
        value = self.get(key, default)
        return str(value) if value is not None else default

    def get_int(self, key: str, default: int = 0) -> int:
        """Retrieves a configuration value cast to an integer.

        Args:
            key: The configuration key.
            default: The fallback integer if key is not found or parsing fails.

        Returns:
            The parsed integer value.
        """
        value = self.get(key)
        if value is None:
            return default
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Retrieves a configuration value parsed as a boolean.

        Accepts standard truthy values like 'true', '1', 'yes', 'on' (case-insensitive).

        Args:
            key: The configuration key.
            default: The fallback boolean if key is not found.

        Returns:
            The parsed boolean representation.
        """
        value = self.get(key)
        if value is None:
            return default
        if isinstance(value, bool):
            return value
        return str(value).lower() in ("true", "1", "yes", "on")
