import json
import os
from typing import Any, Dict

def load_config(filepath: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """
    Loads JSON configuration from a file, merging with provided defaults.
    """
    config = defaults.copy()
    
    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                config.update(data)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

if __name__ == '__main__':
    # Example usage for demonstration
    default_settings = {'host': 'localhost', 'port': 8080}
    settings = load_config('config.json', default_settings)
    print(f'Loaded configuration: {settings}')