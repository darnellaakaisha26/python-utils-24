from typing import Any, Dict, List, Optional, Callable

class DataHandler:
    """Handles transformation of dictionary datasets."""

    def __init__(self, processors: Optional[List[Callable[[Any], Any]]] = None) -> None:
        self.processors = processors or []

    def process_payload(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply sequence of processors to data values.
        
        Args:
            data: Dictionary containing key-value pairs.
            
        Returns:
            Processed dictionary with modified values.
        """
        result: Dict[str, Any] = {}
        for key, value in data.items():
            processed_value = value
            for func in self.processors:
                processed_value = func(processed_value)
            result[key] = processed_value
        return result

    def validate_keys(self, data: Dict[str, Any], required: List[str]) -> bool:
        """
        Ensure all required keys are present.
        
        Args:
            data: Dictionary to inspect.
            required: List of mandatory keys.
            
        Returns:
            Boolean indicating presence of all keys.
        """
        return all(key in data for key in required)