import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a rotating file logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Rotate files at 5MB, keep 3 backups
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Example usage for python-utils-24
if __name__ == '__main__':
    app_logger = setup_logger('app', 'logs/app.log')
    app_logger.info('Logger initialized successfully')