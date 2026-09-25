import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from JSON file with fallback to defaults."""
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Update default values with existing file values
            config.update(data)
    except (json.JSONDecodeError, IOError):
        # Return defaults if file is corrupted or unreadable
        pass
        
    return config

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persist configuration to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        raise RuntimeError(f"Unable to save config: {e}")