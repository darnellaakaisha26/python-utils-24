import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "app",
    log_file: str = "app.log",
    max_bytes: int = 1048576,  # 1MB
    backup_count: int = 5,
    level: int = logging.INFO,
) -> logging.Logger:
    """Configures and returns a logger with console and rotating file handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if the logger was already initialized
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Ensure directory path for log file exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Configure rotating file handler
    try:
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as err:
        # Fallback message to console if logging directory is not writable
        print(f"Warning: Logger failed to write to {log_file}: {err}")

    # Configure stdout console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
