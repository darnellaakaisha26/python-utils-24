import os
import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict[str, Any]:
    """Loads and parses JSON configuration file with error handling."""
    if not os.path.exists(file_path):
        logger.error(f"config file not found: {file_path}")
        return {}

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("invalid config format: expected object")
            return data
    except json.JSONDecodeError as e:
        logger.error(f"malformed json in {file_path}: {e}")
    except PermissionError:
        logger.error(f"insufficient permissions to read {file_path}")
    except Exception as e:
        logger.error(f"unexpected error reading config {file_path}: {e}")
    
    return {}

def get_setting(config: Dict[str, Any], key: str, default: Any = None) -> Any:
    """Safely retrieves a nested setting with a default fallback."""
    try:
        return config.get(key, default)
    except AttributeError:
        logger.warning(f"invalid config type provided: {type(config)}")
        return default