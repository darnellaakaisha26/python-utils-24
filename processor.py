from typing import List, Dict, Optional, Any

def clean_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sanitize a list of dictionaries by removing null values.

    Args:
        data: List of dictionaries to be processed.

    Returns:
        A cleaned list of dictionaries with null keys removed.
    """
    return [{k: v for k, v in entry.items() if v is not None} for entry in data]

def transform_keys(data: Dict[str, Any], mapping: Dict[str, str]) -> Dict[str, Any]:
    """
    Rename keys in a dictionary based on a mapping.

    Args:
        data: The input dictionary to modify.
        mapping: A map of {old_key: new_key}.

    Returns:
        A dictionary with transformed keys.
    """
    return {mapping.get(k, k): v for k, v in data.items()}

def batch_process(items: List[Any], func: callable, chunk_size: int = 10) -> List[Any]:
    """
    Process a large list in smaller batches.

    Args:
        items: List of elements to process.
        func: Callback function to apply to each item.
        chunk_size: Number of items per batch.

    Returns:
        A list of results from the function calls.
    """
    results = []
    for i in range(0, len(items), chunk_size):
        batch = items[i:i + chunk_size]
        results.extend([func(item) for item in batch])
    return results