import logging
import sys
from pathlib import Path
from typing import Optional, Union


class CustomLogger:
    """Configurable logging wrapper supporting stdout and file outputs."""

    def __init__(
        self,
        name: str = "app",
        level: int = logging.INFO,
        log_file: Optional[Union[str, Path]] = None,
    ) -> None:
        """Initialize logger instance with custom formatting and handlers."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_file:
            file_path = Path(log_file)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(file_path, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """Return configured standard logging instance."""
        return self.logger


def setup_logger(
    name: str = "default",
    level: Union[int, str] = "INFO",
    log_file: Optional[str] = None,
) -> logging.Logger:
    """Utility function to quickly initialize and retrieve a logger."""
    if isinstance(level, str):
        numeric_level = getattr(logging, level.upper(), logging.INFO)
    else:
        numeric_level = level

    custom_logger = CustomLogger(name=name, level=numeric_level, log_file=log_file)
    return custom_logger.get_logger()
