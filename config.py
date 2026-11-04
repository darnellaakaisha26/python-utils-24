import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class ConfigLoader:
    """Utility to manage application configurations with fallback defaults."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._defaults: Dict[str, Any] = defaults or {}
        self._config: Dict[str, Any] = self._defaults.copy()

    def load_dict(self, config_data: Dict[str, Any]) -> None:
        """Merge custom dictionary into current configuration."""
        self._config.update(config_data)

    def load_json(self, filepath: Union[str, Path]) -> bool:
        """Load configuration options from a JSON file if it exists."""
        path = Path(filepath)
        if not path.is_file():
            return False
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    self._config.update(data)
                    return True
        except (json.JSONDecodeError, OSError):
            return False
        return False

    def load_env(self, prefix: str = "APP_") -> None:
        """Override matching values using environment variables."""
        for key in list(self._config.keys()):
            env_var = f"{prefix}{key.upper()}"
            if env_var in os.environ:
                val = os.environ[env_var]
                # Basic string type conversion for boolean and numeric values
                if val.lower() in ("true", "false"):
                    self._config[key] = val.lower() == "true"
                elif val.isdigit():
                    self._config[key] = int(val)
                else:
                    self._config[key] = val

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve value for a key with optional fallback default."""
        return self._config.get(key, default)

    def as_dict(self) -> Dict[str, Any]:
        """Return a copy of the active configuration dictionary."""
        return self._config.copy()
