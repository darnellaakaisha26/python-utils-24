import os
import logging
from typing import Any, List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-24')

def clean_temp_files(directory: str, pattern: str = '.tmp') -> int:
    """Removes files with specific suffix in target directory."""
    count = 0
    if not os.path.exists(directory):
        return 0

    for filename in os.listdir(directory):
        if filename.endswith(pattern):
            try:
                os.remove(os.path.join(directory, filename))
                count += 1
            except OSError as e:
                logger.error(f"failed to remove {filename}: {e}")
    
    return count

def batch_process(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """Reorganizes items into equal chunks for processing."""
    if chunk_size <= 0:
        return [items]
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]

def get_env_var(key: str, default: Optional[str] = None) -> str:
    """Safe access to environment configuration variables."""
    return os.environ.get(key, default or '')

if __name__ == '__main__':
    logger.info("utils initialized successfully")