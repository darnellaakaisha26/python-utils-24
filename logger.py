import logging
import os
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: str = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    log_to_console: bool = True,
) -> logging.Logger:
    """Configures and returns a logger with rotating file and optional console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent adding duplicate handlers if logger is configured multiple times
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
    )

    # Ensure directory exists for log file
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Set up rotating file handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Optionally set up console handler
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger
