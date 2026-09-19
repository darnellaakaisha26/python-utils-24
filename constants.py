import os

# System path configurations for file operations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Standard timeout values for network and I/O
DEFAULT_TIMEOUT_SEC = 30
SHORT_TIMEOUT_SEC = 5

# Common application settings
MAX_RETRIES = 3
CHUNK_SIZE = 1024 * 1024  # 1MB chunks

# Supported formats for file processing
SUPPORTED_EXTENSIONS = {'.json', '.csv', '.txt', '.yaml'}

# Environment defaults
ENV_PROD = 'production'
ENV_DEV = 'development'
CURRENT_ENV = os.getenv('APP_ENV', ENV_DEV)

def get_directory(name: str) -> str:
    """Helper to ensure consistent directory path resolution."""
    target_dir = os.path.join(BASE_DIR, name)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    return target_dir