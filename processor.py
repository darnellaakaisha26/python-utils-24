from typing import Any, Dict, List, Tuple


def validate_item(item: Any) -> Tuple[bool, str]:
    """Validate individual input item structure and data types."""
    if not isinstance(item, dict):
        return False, f"Expected dict, got {type(item).__name__}"

    required_keys = {"id", "action", "payload"}
    missing = required_keys - set(item.keys())
    if missing:
        return False, f"Missing required keys: {', '.join(sorted(missing))}"

    if not isinstance(item["id"], (int, str)) or not str(item["id"]).strip():
        return False, "Invalid 'id': must be non-empty string or integer"

    if not isinstance(item["payload"], dict):
        return False, "Invalid 'payload': must be a dictionary"

    return True, ""


def process_batch(items: List[Any]) -> Dict[str, Any]:
    """Process a batch of input items, enforcing input validation in the main loop."""
    results: Dict[str, List[Dict[str, Any]]] = {"successful": [], "failed": []}

    if not isinstance(items, list):
        raise TypeError(f"Expected items to be a list, got {type(items).__name__}")

    for idx, item in enumerate(items):
        is_valid, error_msg = validate_item(item)

        if not is_valid:
            results["failed"].append({
                "index": idx,
                "item": item,
                "error": error_msg
            })
            continue

        # Process valid item
        item_id = str(item["id"]).strip()
        action = str(item["action"]).lower()
        payload = item["payload"]

        results["successful"].append({
            "id": item_id,
            "action": action,
            "processed_payload_size": len(payload),
            "status": "completed"
        })

    return results
