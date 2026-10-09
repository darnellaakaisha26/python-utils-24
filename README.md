# python-utils-24

A curated collection of production-ready Python helper functions designed to streamline daily development tasks. This library focuses on minimizing boilerplate code for data manipulation, file system operations, and performance monitoring.

## Features

*   **File Streamliner:** Simplified context managers for robust JSON/CSV serialization and directory traversal.
*   **Performance Decorators:** Easy-to-use decorators for benchmarking function execution time and memory usage.
*   **Type-Safe Validators:** Utility functions for validating common data formats, including email addresses, URLs, and complex nested dictionaries.
*   **Logger Factory:** Pre-configured logging templates with rotating file support and colored terminal output.

## Installation

Install the package via pip:

```bash
pip install python-utils-24
```

Or add it to your `requirements.txt`:

```text
python-utils-24>=1.0.0
```

## Basic Usage

Quickly profile your functions and manage configuration files with minimal setup:

```python
from pyutils24.decorators import time_execution
from pyutils24.io import load_json

# Benchmark function performance
@time_execution
def process_data(data):
    return [d * 2 for d in data]

# Load and validate configuration
config = load_json("settings.json")

# Run utility
result = process_data([1, 2, 3])
print(f"Result: {result}")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.