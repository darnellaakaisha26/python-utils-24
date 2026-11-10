import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    """Utility class to load configurations with default values and env overrides."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self.defaults = defaults or {}

    def load_from_dict(self, config_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Merge provided dictionary config into default settings."""
        merged = self.defaults.copy()
        merged.update(config_dict)
        return merged

    def load_from_json(self, filepath: str) -> Dict[str, Any]:
        """Load configuration from a JSON file and apply defaults."""
        if not os.path.exists(filepath):
            return self.defaults.copy()

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        return self.load_from_dict(data)

    def apply_env_overrides(
        self, config: Dict[str, Any], prefix: str = "APP_"
    ) -> Dict[str, Any]:
        """Override configuration values using environment variables."""
        updated = config.copy()
        for key, default_val in updated.items():
            env_var = f"{prefix}{key.upper()}"
            if env_var in os.environ:
                raw_val = os.environ[env_var]
                # Cast environment variable string to match existing type
                if isinstance(default_val, bool):
                    updated[key] = raw_val.lower() in ("true", "1", "yes")
                elif isinstance(default_val, int):
                    updated[key] = int(raw_val)
                elif isinstance(default_val, float):
                    updated[key] = float(raw_val)
                else:
                    updated[key] = raw_val
        return updated
