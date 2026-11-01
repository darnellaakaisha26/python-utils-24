import sys

def validate_input(data):
    """Ensures input is a non-empty string for processing."""
    if not isinstance(data, str) or not data.strip():
        raise ValueError("Invalid input: expected non-empty string")
    return data.strip()

def process_payloads(items):
    """Main loop for secure data ingestion."""
    results = []
    for item in items:
        try:
            clean_data = validate_input(item)
            # Mock transformation logic
            processed = clean_data.upper()
            results.append(processed)
        except (ValueError, TypeError) as e:
            print(f"Skipping invalid entry: {e}", file=sys.stderr)
            continue
    return results

if __name__ == "__main__":
    raw_data = ["alpha", "  ", 123, "beta"]
    final_output = process_payloads(raw_data)
    print(f"Processing complete: {final_output}")