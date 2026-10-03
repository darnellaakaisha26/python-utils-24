import json
import os
from typing import Any, Dict, Optional


class ConfigManager:
    """Handles application configuration loading with robust edge-case handling."""

    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self._config: Dict[str, Any] = {}
        if config_path:
            self.load_from_file(config_path)

    def load_from_file(self, filepath: str) -> Dict[str, Any]:
        """Load configuration from a JSON file with validation and safe parsing."""
        if not isinstance(filepath, str) or not filepath.strip():
            raise ValueError("Configuration filepath must be a non-empty string")

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")

        if not os.path.access(filepath, os.R_OK):
            raise PermissionError(f"Configuration file is not readable: {filepath}")

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in '{filepath}': {e.msg} at line {e.lineno}") from e
        except Exception as e:
            raise RuntimeError(f"Failed to read configuration '{filepath}': {str(e)}") from e

        if not isinstance(data, dict):
            raise TypeError(f"Root config must be a JSON object, got {type(data).__name__}")

        self._config.update(data)
        return self._config

    def get(self, key: str, default: Any = None, expected_type: Optional[type] = None) -> Any:
        """Safely retrieve nested config values using dot notation with fallback type conversion."""
        if not key or not isinstance(key, str):
            return default

        current = self._config
        for part in key.split("."):
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default

        if expected_type is not None and not isinstance(current, expected_type):
            try:
                return expected_type(current)
            except (ValueError, TypeError):
                return default

        return current
