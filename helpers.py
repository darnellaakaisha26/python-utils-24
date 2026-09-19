from typing import Dict, Any, List, Generator

def deep_merge(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    '''
    Recursively merges dict2 into dict1.
    '''
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def chunk_list(lst: List[Any], size: int) -> Generator[List[Any], None, None]:
    '''
    Yield successive n-sized chunks from a list.
    '''
    if size <= 0:
        raise ValueError('Chunk size must be greater than zero.')
    for i in range(0, len(lst), size):
        yield lst[i : i + size]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    '''
    Flattens a nested dictionary using a separator.
    '''
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
