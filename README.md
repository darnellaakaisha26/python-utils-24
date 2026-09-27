# python-utils-24

`python-utils-24` is a collection of high-performance utility functions designed to streamline repetitive Python development tasks. It focuses on reducing boilerplate code for data serialization, file system manipulation, and asynchronous task management.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## Features

*   **File Streamliner**: Simplified context managers for efficient I/O operations and directory traversal.
*   **Data Sanitizers**: Robust decorators to enforce schema validation and type safety on function arguments.
*   **Async Dispatcher**: Lightweight wrappers to convert blocking I/O calls into non-blocking coroutines without overhead.
*   **Environment Manager**: Auto-loading functionality for `.env` files with strict type-casting capabilities.

## Installation

Install the package via pip:

```bash
pip install python-utils-24
```

For development mode and test dependencies:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -e .[dev]
```

## Basic Usage

Quickly handle file reading and environment variable management using the utility modules:

```python
from pyutils24.io import load_json
from pyutils24.env import get_env

# Load configurations securely
db_url = get_env("DATABASE_URL", default="localhost:5432")

# Robust JSON processing
data = load_json("config.json")

print(f"Connected to: {db_url}")
print(f"Data retrieved: {data['version']}")
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes before submitting a pull request. Ensure all new utilities include corresponding unit tests in the `/tests` directory.

## License

Distributed under the MIT License. See `LICENSE` for more information.