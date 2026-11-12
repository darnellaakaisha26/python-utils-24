# python-utils-24

A curated collection of production-ready Python utility functions designed to streamline daily development tasks. This library focuses on performance, type safety, and minimizing boilerplate code for common data manipulation and system operations.

## Features

*   **Robust File Operations:** Simplified wrappers for recursive file searching, safe directory creation, and atomic file writes.
*   **Data Transformation:** Efficient helpers for flattening nested dictionaries and converting complex iterables into CSV-friendly formats.
*   **Performance Decorators:** Built-in tools for easy execution timing and lightweight memoization without external dependencies.
*   **Input Validation:** Concise validators for environment variables and configuration objects to ensure application stability.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-24
```

For local development or manual installation:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -e .
```

## Basic Usage

The following example demonstrates how to use the high-performance timing decorator and the dictionary flattener:

```python
from pyutils24.decorators import time_execution
from pyutils24.data import flatten_dict

@time_execution
def process_data(data):
    return flatten_dict(data)

nested = {"user": {"id": 1, "meta": {"login": "admin"}}}
result = process_data(nested)

print(result)
# Output: {'user_id': 1, 'user_meta_login': 'admin'}
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.