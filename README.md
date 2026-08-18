# python-utils-24

A collection of utility functions and classes designed to make common Python tasks easier and more efficient. Whether you're working on data manipulation, string processing, or file handling, python-utils-24 provides a reliable toolkit to boost your productivity.

## Features
- **Data Manipulation**: Streamlined functions for transforming lists and dictionaries, including filtering, sorting, and custom transformations.
- **String Utilities**: Advanced string handling features like smart casing, slugify, and substring extraction to simplify your text processing tasks.
- **File Operations**: Easy-to-use methods for reading and writing files, including CSV and JSON formats, with built-in error handling.
- **Time Management**: Helper functions for date and time manipulation, such as formatting, parsing, and calculating differences.

## Installation

To install python-utils-24, you can use pip. Run the following command in your terminal:

```bash
pip install python-utils-24
```

## Basic Usage Example

Here’s a quick example to get you started with some of the utility features provided by the library:

```python
from python_utils24 import StringUtils, FileUtils

# Using StringUtils to slugify text
slug = StringUtils.slugify("Hello World! Welcome to python-utils-24")
print(slug)  # Output: hello-world-welcome-to-python-utils-24

# Using FileUtils to read data from a JSON file
data = FileUtils.read_json('data.json')
print(data)
```

## License

![MIT License](https://img.shields.io/badge/License-MIT-green)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.