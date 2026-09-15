import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file with provided fallback defaults.
    """
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            # Update defaults with values from the file
            config.update(user_config)
    except (json.JSONDecodeError, IOError) as e:
        # Log error or handle as per project requirements
        print(f"Configuration loading error: {e}")

    return config

if __name__ == '__main__':
    # Example usage for demonstration
    default_settings = {"host": "localhost", "port": 8080, "debug": False}
    final_cfg = load_config('settings.json', default_settings)
    print(f"Final configuration: {final_cfg}")