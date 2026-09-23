import os
import shutil
from typing import List, Optional

def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def clean_temp_files(directory: str, extension: str = '.tmp') -> int:
    """Remove files with specific extension from directory."""
    count = 0
    if not os.path.exists(directory):
        return count

    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                count += 1
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")
    return count

def get_file_list(directory: str, pattern: Optional[str] = None) -> List[str]:
    """Retrieve list of files optionally matching pattern."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if pattern:
        return [f for f in files if pattern in f]
    return files

def safe_remove_tree(path: str) -> bool:
    """Recursively remove directory if exists."""
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            return True
        except OSError:
            return False
    return False