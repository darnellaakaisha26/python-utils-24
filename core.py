import json
import os

class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config_data = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"Config file not found: {self.file_path}")
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config_data.get(key, default)

class Logger:
    def __init__(self, filename='app.log'):
        self.filename = filename

    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(f"{message}\n")

def perform_operation(config_file):
    config = Config(config_file)
    logger = Logger()
    try:
        operation_mode = config.get('mode', 'default')
        logger.log(f'Operation mode: {operation_mode}')
        # Simulate operation
        logger.log('Operation completed successfully')
    except Exception as e:
        logger.log(f'Error: {e}')

if __name__ == '__main__':
    perform_operation('config.json')