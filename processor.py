import math
from typing import Any, List, Union


class DataProcessor:
    """Utility class for safe data transformation and edge case handling."""

    @staticmethod
    def safe_divide(
        numerator: Union[int, float, str],
        denominator: Union[int, float, str],
        default: float = 0.0
    ) -> float:
        """Safely divide two numbers handling zero division, type mismatches, and invalid values."""
        try:
            if numerator is None or denominator is None:
                return default
            num = float(numerator)
            den = float(denominator)
            if den == 0.0 or math.isnan(num) or math.isnan(den):
                return default
            result = num / den
            return default if math.isinf(result) else result
        except (ValueError, TypeError, ZeroDivisionError):
            return default

    @staticmethod
    def extract_nested_key(
        data: Any,
        path: List[str],
        default: Any = None
    ) -> Any:
        """Safely extract nested dictionary values without raising KeyError or TypeError."""
        if not isinstance(data, dict) or not path:
            return default
        
        current = data
        for key in path:
            if not isinstance(current, dict):
                return default
            current = current.get(key)
            if current is None:
                return default
        return current

    @staticmethod
    def sanitize_numeric_list(items: List[Any]) -> List[float]:
        """Parse mixed inputs into floats, dropping non-numeric and special math values."""
        if not isinstance(items, (list, tuple)):
            return []
        
        cleaned = []
        for item in items:
            try:
                if item is None or isinstance(item, bool):
                    continue
                val = float(item)
                if not math.isnan(val) and not math.isinf(val):
                    cleaned.append(val)
            except (ValueError, TypeError):
                continue
        return cleaned
