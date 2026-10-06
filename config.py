import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Loads JSON configuration with provided default fallback."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config
        
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            config.update(data)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Configuration load error: {e}. Using defaults.")
        
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Configuration save error: {e}")