import os
import shutil
from typing import List, Optional

def clean_directory(path: str, extensions: Optional[List[str]] = None) -> int:
    """Removes files with specified extensions from a directory."""
    count = 0
    if not os.path.exists(path):
        return count

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            if extensions is None or filename.endswith(tuple(extensions)):
                os.remove(file_path)
                count += 1
    return count

def safe_move(src: str, dst: str) -> bool:
    """Moves file ensuring destination directory exists."""
    try:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        return True
    except (IOError, OSError):
        return False

def get_file_stats(path: str) -> dict:
    """Returns basic metadata for a given file path."""
    stat = os.stat(path)
    return {
        "size": stat.st_size,
        "created": stat.st_ctime,
        "modified": stat.st_mtime
    }