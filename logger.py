import logging
import sys
from typing import Optional

class AppLogger:
    def __init__(self, name: str = 'python-utils-24', level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def get_default_logger(name: Optional[str] = None) -> logging.Logger:
    instance = AppLogger(name or 'python-utils-24')
    return instance.get_logger()