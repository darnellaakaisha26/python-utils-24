import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, merging with provided defaults.
    """
    config = defaults.copy()
    
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                file_data = json.load(f)
                if isinstance(file_data, dict):
                    config.update(file_data)
        except (json.JSONDecodeError, IOError):
            # Fallback to defaults on file access or parsing errors
            pass
            
    return config

def get_env_config(prefix: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Overwrites config values with matching environment variables.
    """
    config = defaults.copy()
    for key in config:
        env_key = f"{prefix}_{key.upper()}"
        if env_key in os.environ:
            val = os.environ[env_key]
            # Attempt basic type preservation
            if isinstance(config[key], bool):
                config[key] = val.lower() in ('true', '1', 'yes')
            elif isinstance(config[key], int):
                config[key] = int(val)
            else:
                config[key] = val
    return config