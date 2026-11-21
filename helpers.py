import typing as t
from collections.abc import Iterable

def deep_flatten(items: Iterable[t.Any]) -> t.Generator[t.Any, None, None]:
    """Recursively flatten nested iterables into a single generator."""
    for item in items:
        if isinstance(item, (list, tuple, set)) and not isinstance(item, (str, bytes)):
            yield from deep_flatten(item)
        else:
            yield item

def batch_process(data: t.Sequence[t.Any], size: int) -> t.Generator[t.Sequence[t.Any], None, None]:
    """Chunk a sequence into batches of specified size."""
    if size <= 0:
        raise ValueError("batch size must be positive")
    for i in range(0, len(data), size):
        yield data[i:i + size]

def sanitize_dict(data: dict[str, t.Any], keys_to_remove: t.Iterable[str]) -> dict[str, t.Any]:
    """Return new dictionary excluding specified keys."""
    return {k: v for k, v in data.items() if k not in keys_to_remove}

def get_nested(data: dict[str, t.Any], path: str, default: t.Any = None) -> t.Any:
    """Retrieve nested value from dict using dot notation path."""
    keys = path.split('.')
    current = data
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError):
        return default