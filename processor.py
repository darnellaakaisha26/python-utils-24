from typing import Any, Callable, Generator, Iterable, List, Sequence, TypeVar

T = TypeVar("T")


def chunk_iterable(iterable: Sequence[T], chunk_size: int) -> Generator[List[T], None, None]:
    """Split a sequence into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")
    for i in range(0, len(iterable), chunk_size):
        yield list(iterable[i : i + chunk_size])


def flatten(nested_iterable: Iterable[Any]) -> List[Any]:
    """Recursively flatten arbitrarily nested lists or tuples."""
    flat_list = []
    for item in nested_iterable:
        if isinstance(item, (list, tuple)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def deep_get(dictionary: dict, key_path: str, default: Any = None, delimiter: str = ".") -> Any:
    """Safely retrieve nested values from a dictionary using a delimited key path."""
    current = dictionary
    for key in key_path.split(delimiter):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def process_in_batches(
    items: Sequence[T], batch_size: int, transform_func: Callable[[List[T]], List[Any]]
) -> List[Any]:
    """Apply a transformation function to items in fixed-size batches."""
    results = []
    for batch in chunk_iterable(items, batch_size):
        processed_batch = transform_func(batch)
        results.extend(processed_batch)
    return results
