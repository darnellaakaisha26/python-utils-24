import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads JSON configuration with system defaults fallback."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {filepath}: {e}")
            
    return config

def get_env_override(key: str, default: Any) -> Any:
    """Fetches value from environment variables if present."""
    return os.environ.get(key.upper(), default)

if __name__ == "__main__":
    # Example usage
    current_config = load_config()
    current_config["port"] = get_env_override("PORT", current_config["port"])
    print(f"Loaded configuration: {current_config}")