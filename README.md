[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-24

`python-utils-24` is a lightweight, zero-dependency library designed to streamline daily Python development workflows. It provides optimized utility functions for common operations like safe dictionary traversal, robust datetime parsing, and cryptographically secure token generation.

## Features

* **Safe Nested Lookup**: Extract values from nested dictionaries using intuitive dot-notation paths without raising `KeyError`.
* **Smart Datetime Parsing**: Convert ambiguous timestamp strings into standard, timezone-aware UTC datetime objects automatically.
* **Cryptographic Helpers**: Generate secure, high-entropy tokens and keys suitable for APIs and session management.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install python-utils-24
```

## Usage

Here is how easily you can integrate these utilities into your script:

```python
from python_utils_24 import get_nested, to_utc, generate_token

# 1. Safely extract deep values
data = {"users": {"active": {"admin": "alice@example.com"}}}
email = get_nested(data, "users.active.admin", default="guest")
print(email)  # Output: alice@example.com

# 2. Convert raw strings to UTC datetime
timestamp = to_utc("2024-11-20 18:30:00 PST")
print(timestamp)  # Output: 2024-11-21 02:30:00+00:00

# 3. Generate a secure hexadecimal API token
token = generate_token(length=32)
print(token)  # Output: e.g., '9f4c3a2b7d8e0f1a9f4c3a2b7d8e0f1a'
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.