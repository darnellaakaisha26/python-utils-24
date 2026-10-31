"""Data processing utilities with comprehensive edge case error handling."""

import math
from typing import Any, List, Optional


class ProcessingError(Exception):
    """Raised when data transformation fails irrecoverably."""

    pass


def safe_cast_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    """Safely convert various input types to float, handling edge cases."""
    if value is None:
        return default

    if isinstance(value, (int, float)):
        if math.isnan(value) or math.isinf(value):
            return default
        return float(value)

    if isinstance(value, str):
        cleaned = value.strip().replace(",", "")
        if not cleaned:
            return default
        try:
            val = float(cleaned)
            return default if math.isnan(val) or math.isinf(val) else val
        except (ValueError, TypeError):
            return default

    return default


def process_numeric_batch(
    data: List[Any], scale_factor: float = 1.0, skip_invalid: bool = True
) -> List[float]:
    """Process a list of raw items into scaled floating-point values."""
    if not isinstance(data, list):
        raise TypeError(f"Expected list for data, got {type(data).__name__}")

    if scale_factor == 0 or math.isnan(scale_factor) or math.isinf(scale_factor):
        raise ValueError("scale_factor must be a non-zero finite number")

    results: List[float] = []

    for idx, item in enumerate(data):
        cast_val = safe_cast_float(item)

        if cast_val is None:
            if not skip_invalid:
                raise ProcessingError(f"Invalid numeric value at index {idx}: {item!r}")
            continue

        try:
            scaled = cast_val * scale_factor
            if math.isinf(scaled):
                if not skip_invalid:
                    raise ProcessingError(f"Numeric overflow at index {idx}")
                continue
            results.append(scaled)
        except Exception as err:
            if not skip_invalid:
                raise ProcessingError(f"Error processing index {idx}: {err}") from err

    return results