import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Load configuration from file with fallback defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as f:
                file_data = json.load(f)
                config.update(file_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: failed to load {filepath}: {e}")
            
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Fetch specific configuration setting."""
    config = load_config()
    return config.get(key, default)

if __name__ == "__main__":
    # Example usage demonstration
    current_config = load_config()
    print(f"Active configuration: {current_config}")