[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# python-utils-24

A lightweight, production-ready utility toolkit designed to streamline daily Python development. It provides highly optimized, zero-dependency helpers for dictionary manipulation, path operations, and transient failure handling.

## Features

* **Deep Dict Merging:** Recursively merge nested configurations and dictionaries with customizable conflict resolution.
* **Resilient Retries:** A configurable decorator to automatically retry flaky functions or API calls using exponential backoff.
* **Safe Path Resolver:** Bulletproof file system utility to locate, create, and validate cross-platform file paths securely.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-24
```

## Quick Start

Here is a quick look at how you can simplify your workflow with `python-utils-24`:

```python
from python_utils_24.dicts import deep_merge
from python_utils_24.decorators import retry

# 1. Safely merge nested configuration dicts
default_config = {"server": {"host": "localhost", "port": 8080}, "debug": True}
override_config = {"server": {"port": 9000}}

final_config = deep_merge(default_config, override_config)
print(final_config)
# Output: {'server': {'host': 'localhost', 'port': 9000}, 'debug': True}


# 2. Add automatic retry logic with backoff
@retry(exceptions=(ConnectionError,), tries=3, delay=2)
def fetch_unreliable_api():
    print("Attempting to connect to api...")
    raise ConnectionError("Network timeout")

# fetch_unreliable_api() will retry 3 times before raising the exception
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.