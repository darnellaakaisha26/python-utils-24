import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'app.log', level=logging.INFO):
    """
    Configures a logger with file rotation settings.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Rotate after 5MB, keep 3 backups
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

        # Optional: add console output
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger

# Example usage:
if __name__ == '__main__':
    app_logger = setup_logger('dev_logger')
    app_logger.info('Logger setup complete with rotation')