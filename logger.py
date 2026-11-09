import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Initialize and return a configured logger instance.

    Args:
        name: The name of the logger instance.
        level: The logging threshold level.

    Returns:
        A configured logging.Logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """
    Route message to the appropriate logger method.

    Args:
        logger: The logger instance to use.
        message: The text string to log.
        level: The severity level string.
    """
    levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)