# python-utils-24

A comprehensive collection of production-ready Python utility functions designed to streamline daily development tasks. This library focuses on performance, type-safety, and reducing boilerplate code in data processing and system operations.

## Features

*   **Robust File Operations:** Simplified wrappers for recursive directory traversal and high-speed JSON/YAML configuration parsing.
*   **Performance Decorators:** Built-in tools for function execution timing, thread-safe memoization, and automatic retry logic with exponential backoff.
*   **Data Validation:** Lightweight schema validation helpers for dictionaries and complex object structures.
*   **String Manipulation:** Advanced sanitization and pattern matching utilities for log parsing and input normalization.

## Installation

Install the latest version directly from PyPI:

```bash
pip install python-utils-24
```

Alternatively, install from source:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install .
```

## Usage

Leverage the decorator-based utility suite to improve code maintainability and execution tracking:

```python
from pyutils24.decorators import time_execution
from pyutils24.io import load_json

@time_execution
def process_data(file_path):
    data = load_json(file_path)
    # Perform complex logic
    return data

result = process_data("config.json")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.