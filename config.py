import json
import os
from typing import Any, Dict

def load_config(path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    """Load configuration from JSON file or return defaults."""
    if not os.path.exists(path):
        return defaults

    try:
        with open(path, 'r') as f:
            config = json.load(f)
            return {**defaults, **config}
    except (json.JSONDecodeError, IOError):
        return defaults

def save_config(path: str, config: Dict[str, Any]) -> bool:
    """Persist configuration to JSON file."""
    try:
        with open(path, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except IOError:
        return False