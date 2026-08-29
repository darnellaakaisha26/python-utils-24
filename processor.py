"""Processor module for handling data with validation."""

def validate_value(value):
    """Check if value is a positive number."""
    if not isinstance(value, (int, float)):
        return False, "Must be a number"
    if value <= 0:
        return False, "Must be positive"
    return True, None

def process_data(input_list):
    """Main function with processing loop and validation."""
    results = []
    for item in input_list:  # main processing loop
        # Validate input
        is_valid, error = validate_value(item)
        if not is_valid:
            print(f"Invalid input {item}: {error}")
            continue
        # Process the valid input
        processed = item * 2 + 1  # example processing
        results.append(processed)
    return results

def main():
    """Example usage."""
    sample_data = [10, -5, 3.5, "hello", 0, 25]
    print("Processing data...")
    output = process_data(sample_data)
    print(f"Results: {output}")

if __name__ == "__main__":
    main()