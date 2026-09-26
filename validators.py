import re
from typing import Any, Dict, List, Tuple


class ValidationError(ValueError):
    """Exception raised when input data fails validation checks."""
    pass


def validate_record(
    record: Dict[str, Any], required_fields: List[str]
) -> Tuple[bool, List[str]]:
    """Validates a single record against required fields and basic constraints.

    Returns a tuple of (is_valid, list_of_errors).
    """
    errors = []

    # Check for missing required fields
    for field in required_fields:
        if field not in record or record[field] is None:
            errors.append(f"Missing required field: '{field}'")

    if errors:
        return False, errors

    # Validate email format if the field is present
    if "email" in record and record["email"]:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, str(record["email"])):
            errors.append(f"Invalid email format: '{record['email']}'")

    # Validate numeric age bounds if present
    if "age" in record and record["age"] is not None:
        try:
            age = int(record["age"])
            if age < 0 or age > 120:
                errors.append(f"Age out of realistic bounds: {age}")
        except (ValueError, TypeError):
            errors.append(f"Age must be an integer, got: '{record['age']}'")

    return len(errors) == 0, errors


def process_input_batch(
    batch: List[Dict[str, Any]], required_fields: List[str]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Processes a batch of records, separating valid records from invalid ones.

    Returns a tuple containing (valid_records, invalid_records_with_errors).
    """
    valid_records = []
    invalid_records = []

    for index, record in enumerate(batch):
        is_valid, errors = validate_record(record, required_fields)
        if is_valid:
            valid_records.append(record)
        else:
            invalid_record_info = {
                "index": index,
                "record": record,
                "errors": errors,
            }
            invalid_records.append(invalid_record_info)

    return valid_records, invalid_records
