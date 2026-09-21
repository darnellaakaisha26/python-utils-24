import re
import math
from typing import Any, Union, Optional

def validate_email(email: Any) -> str:
    """
    Validates an email address against length, format, and edge cases.
    Raises ValueError or TypeError for invalid inputs.
    """
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    
    # Trim and handle empty string edge case
    cleaned_email = email.strip()
    if not cleaned_email:
        raise ValueError("Email cannot be empty or only whitespace")
    
    # Handle unreasonably long emails (RFC 5321 limit is 254 octets)
    if len(cleaned_email) > 254:
        raise ValueError("Email length exceeds maximum permitted limit of 254 characters")
    
    # Basic regex for email pattern, preventing catastrophic backtracking
    email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if not email_regex.match(cleaned_email):
        raise ValueError(f"Invalid email format: '{cleaned_email}'")
        
    # Prevent edge cases with consecutive dots or trailing dots
    if ".." in cleaned_email or cleaned_email.endswith("."):
        raise ValueError("Email domain cannot contain consecutive dots or end with a dot")
        
    return cleaned_email

def validate_numeric_range(
    value: Any, 
    min_val: Optional[Union[int, float]] = None, 
    max_val: Optional[Union[int, float]] = None
) -> Union[int, float]:
    """
    Validates that a numeric value is within a specified range, handling 
    NaN, infinity, non-numeric inputs, and logical range constraint errors.
    """
    if isinstance(value, bool):  # Python booleans are subclasses of int
        raise TypeError("Booleans are not accepted as numeric values")
        
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be a number, got {type(value).__name__}")
        
    # Handle NaN and Infinity edge cases
    if math.isnan(value):
        raise ValueError("Value cannot be NaN (Not a Number)")
    if math.isinf(value):
        raise ValueError("Value cannot be infinite")

    # Validate boundary logical constraints
    if min_val is not None and max_val is not None and min_val > max_val:
        raise ValueError(f"Invalid range: min_val ({min_val}) is greater than max_val ({max_val})")

    if min_val is not None and value < min_val:
        raise ValueError(f"Value {value} is below the minimum allowed limit of {min_val}")
        
    if max_val is not None and value > max_val:
        raise ValueError(f"Value {value} is above the maximum allowed limit of {max_val}")
        
    return value