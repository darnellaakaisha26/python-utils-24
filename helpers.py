import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided fallback defaults."""
    config = defaults.copy()

    if not os.path.exists(path):
        return config

    try:
        with open(path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(path: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a JSON file."""
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    # Example usage for python-utils-24
    default_settings = {"host": "localhost", "port": 8080}
    app_config = load_config("config.json", default_settings)
    print(f"Loaded configuration: {app_config}")