import os
import shutil
from typing import List, Optional

def cleanup_directory(path: str, extensions: Optional[List[str]] = None) -> int:
    """Removes files with specific extensions from the target directory."""
    count = 0
    if not os.path.exists(path):
        return count

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            if extensions is None or any(filename.endswith(ext) for ext in extensions):
                os.remove(file_path)
                count += 1
    return count

def ensure_directory(path: str) -> None:
    """Creates a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def purge_temp_files(base_path: str) -> bool:
    """Recursive removal of common temporary artifacts."""
    try:
        for root, dirs, files in os.walk(base_path):
            for name in dirs:
                if name in ('__pycache__', '.pytest_cache'):
                    shutil.rmtree(os.path.join(root, name))
        return True
    except OSError:
        return False

def get_file_metadata(path: str) -> dict:
    """Retrieves basic stats for a given file."""
    stat = os.stat(path)
    return {
        "size": stat.st_size,
        "created": stat.st_ctime,
        "modified": stat.st_mtime
    }