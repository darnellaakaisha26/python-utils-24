# python-utils-24

A curated collection of production-ready Python utility functions designed to streamline boilerplate code in data processing and automation tasks. This library focuses on performance, type safety, and minimizing dependencies for cleaner project integration.

## Features

*   **Robust File Operations:** Advanced wrappers for path handling, directory recursive creation, and atomic file writes.
*   **Performance Decorators:** Built-in caching mechanisms, retry logic with exponential backoff, and execution time logging.
*   **String Sanitization:** Comprehensive cleaning tools for normalizing filenames, email formats, and Unicode stripping.
*   **Lightweight Core:** Zero-dependency architecture ensuring compatibility across Python 3.8+ environments.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-24
```

To include it in your `requirements.txt` file:

```text
python-utils-24>=1.0.0
```

## Basic Usage

The library is designed for quick imports to solve common architectural hurdles. Below is an example of the retry decorator and atomic file writing:

```python
from pyutils import retry, atomic_write

# Automatically retry a network call up to 3 times
@retry(attempts=3, delay=2)
def fetch_data():
    # Simulated fragile operation
    pass

# Write data safely to disk without file corruption
data = "System state saved."
atomic_write("config.txt", data)
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.