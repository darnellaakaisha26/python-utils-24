from typing import Any, Dict, Generator, Iterable, List

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary into a single-level dictionary.
    
    Args:
        data: The nested dictionary to flatten.
        parent_key: The prefix key string (used internally for recursion).
        sep: Separator between nested keys.
    """
    items: List[tuple] = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def chunk_iterable(iterable: Iterable[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """
    Yields successive chunks of a given size from an iterable.
    
    Args:
        iterable: The collection or stream of data.
        chunk_size: Maximum size of each yielded chunk.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    
    chunk: List[Any] = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk