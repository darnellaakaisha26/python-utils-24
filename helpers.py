import os
import shutil
from typing import List, Optional

def clean_temp_directories(paths: List[str]) -> int:
    """Removes temporary directories and returns count of removed items."""
    count = 0
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            try:
                shutil.rmtree(path)
                count += 1
            except OSError:
                continue
    return count

def validate_path_exists(path: Optional[str]) -> bool:
    """Checks if a given string is a valid existing path."""
    return path is not None and os.path.exists(path)

def format_byte_size(size_bytes: int) -> str:
    """Converts integer bytes into human-readable string format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

class PathManager:
    """Utility class for managing filesystem paths."""
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def get_full_path(self, relative_path: str) -> str:
        return os.path.join(self.base_dir, relative_path)