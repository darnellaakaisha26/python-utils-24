import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional, Union

DEFAULT_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_logger(
    name: str = "app",
    log_file: Optional[Union[str, Path]] = None,
    level: int = logging.INFO,
    max_bytes: int = 10_000_000,
    backup_count: int = 5,
    console: bool = True,
    fmt: str = DEFAULT_FORMAT,
) -> logging.Logger:
    """
    Configures and returns a logger instance with optional file rotation and console output.

    :param name: Name of the logger instance.
    :param log_file: Path to log file. If provided, enables rotating file handler.
    :param level: Minimum logging level to capture.
    :param max_bytes: Maximum file size in bytes before rotating.
    :param backup_count: Number of rotated log files to retain.
    :param console: Whether to output logs to standard stream.
    :param fmt: Format string for log messages.
    :return: Configured Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to prevent duplicate logging setup
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(fmt)

    if log_file:
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
