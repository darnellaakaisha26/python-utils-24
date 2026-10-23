import logging
import sys
from typing import Optional

class CustomLogger:
    """Utility class for application logging with safety checks."""
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stderr)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def safe_log(self, level: int, message: Optional[str]) -> None:
        """Logs a message while handling potential null inputs."""
        try:
            if message is None:
                self.logger.warning("Attempted to log a null message")
                return
            
            if not isinstance(message, str):
                message = str(message)
                
            self.logger.log(level, message)
        except Exception as e:
            # Fallback to standard error to prevent log-induced crashes
            print(f"Critical logging failure: {e}", file=sys.stderr)

    def log_error(self, message: str, exc_info: bool = True) -> None:
        """Specialized error logging wrapper."""
        try:
            self.logger.error(message, exc_info=exc_info)
        except Exception:
            self.safe_log(logging.ERROR, message)