from typing import Any, Dict, List, Generator, Iterable, Union
import itertools


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Recursively flatten a nested dictionary into key-value pairs with separated keys."""
    items: List[tuple] = []
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def clean_nulls(data: Union[Dict[str, Any], List[Any]]) -> Union[Dict[str, Any], List[Any]]:
    """Recursively remove None values from dictionaries and lists."""
    if isinstance(data, dict):
        return {
            k: clean_nulls(v) if isinstance(v, (dict, list)) else v
            for k, v in data.items()
            if v is not None
        }
    elif isinstance(data, list):
        return [
            clean_nulls(item) if isinstance(item, (dict, list)) else item
            for item in data
            if item is not None
        ]
    return data


def chunk_iterable(iterable: Iterable[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    """Yield successive n-sized chunks from an iterable collection."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be at least 1")
    iterator = iter(iterable)
    while chunk := list(itertools.islice(iterator, chunk_size)):
        yield chunk
