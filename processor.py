from typing import List, Optional, Any, Callable

class DataProcessor:
    """Handles transformation logic for structured datasets."""

    def __init__(self, transform_func: Optional[Callable[[Any], Any]] = None) -> None:
        """Initialize with an optional transformation strategy."""
        self.transform_func = transform_func

    def process_batch(self, items: List[Any]) -> List[Any]:
        """
        Apply transformation to each item in the provided list.

        Args:
            items: A list of arbitrary elements to process.

        Returns:
            A list of transformed elements.
        """
        if not self.transform_func:
            return items
        return [self.transform_func(item) for item in items]

    def filter_nulls(self, items: List[Optional[Any]]) -> List[Any]:
        """
        Remove None values from the input list.

        Args:
            items: A list potentially containing None values.

        Returns:
            A filtered list containing only non-null values.
        """
        return [item for item in items if item is not None]

    def summarize(self, items: List[int]) -> float:
        """
        Calculate the average of a list of integers.

        Args:
            items: A list of numeric values.

        Returns:
            The mean value of the list.
        """
        if not items:
            return 0.0
        return sum(items) / len(items)