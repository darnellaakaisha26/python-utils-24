 """Batch data processor with built-in input validation."""

from typing import Any, Dict, List, Tuple


def validate_item(item: Any) -> Tuple[bool, str]:
    """Validate an individual data record prior to processing."""
    if not isinstance(item, dict):
        return False, "Record must be a dictionary"

    if "id" not in item or not isinstance(item["id"], (int, str)):
        return False, "Missing or invalid required field 'id'"

    if "value" not in item or not isinstance(item["value"], (int, float)):
        return False, "Missing or non-numeric field 'value'"

    if item["value"] < 0:
        return False, "Field 'value' must be non-negative"

    return True, ""


def process_batch(items: List[Any]) -> Dict[str, List[Any]]:
    """Main processing loop that validates and transforms input items."""
    successful_records = []
    failed_records = []

    # Main processing loop with explicit input validation
    for index, item in enumerate(items):
        is_valid, error_message = validate_item(item)

        if not is_valid:
            failed_records.append({
                "index": index,
                "item": item,
                "reason": error_message
            })
            continue

        # Process valid item data
        transformed_val = round(float(item["value"]) * 1.15, 2)
        successful_records.append({
            "id": item["id"],
            "processed_value": transformed_val
        })

    return {"successful": successful_records, "failed": failed_records}


if __name__ == "__main__":
    sample_data = [
        {"id": 101, "value": 50.0},
        {"id": 102, "value": -5.0},
        {"id": "103", "value": 22.5},
        {"value": 10.0},
        "invalid_record_structure"
    ]
    results = process_batch(sample_data)
    print(f"Processed {len(results['successful'])} valid items.")
    print(f"Rejected {len(results['failed'])} invalid items.")