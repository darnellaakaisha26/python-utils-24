import json
import os
from typing import Any, Dict

class ConfigLoader:
    '''Utility to load configuration settings with fallback defaults.'''
    def __init__(self, defaults: Dict[str, Any] = None):
        self._defaults = defaults or {}
        self._config = self._defaults.copy()

    def load_from_json(self, filepath: str) -> None:
        '''Loads JSON config and merges with current state.'''
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._config.update(data)

    def load_from_env(self, prefix: str = 'APP_') -> None:
        '''Overrides configuration using environment variables.'''
        for key in self._defaults.keys():
            env_key = f'{prefix}{key.upper()}'
            if env_key in os.environ:
                env_val = os.environ[env_key]
                default_val = self._defaults[key]
                if isinstance(default_val, bool):
                    self._config[key] = env_val.lower() in ('true', '1', 'yes')
                elif isinstance(default_val, int):
                    self._config[key] = int(env_val)
                elif isinstance(default_val, float):
                    self._config[key] = float(env_val)
                else:
                    self._config[key] = env_val

    def get(self, key: str, default: Any = None) -> Any:
        '''Retrieves configuration value by key with optional fallback.'''
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        '''Returns copy of configuration.'''
        return self._config.copy()