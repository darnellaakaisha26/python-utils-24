import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    """Custom exception for data processing failures."""
    pass

def process_data(data: Any) -> Optional[dict]:
    """Safely processes input data with robust error handling."""
    if data is None:
        logger.warning("Received null data for processing")
        return None

    try:
        if not isinstance(data, dict):
            raise ValueError(f"Expected dict, got {type(data).__name__}")
            
        # Simulation of core logic requiring key validation
        required_keys = {'id', 'payload'}
        if not required_keys.issubset(data.keys()):
            missing = required_keys - data.keys()
            raise KeyError(f"Missing keys: {missing}")
            
        return {
            "status": "success",
            "processed_id": data['id'],
            "result": str(data['payload']).strip()
        }

    except (ValueError, KeyError) as e:
        logger.error(f"Validation failed: {e}")
        return {"status": "error", "message": str(e)}
        
    except Exception as e:
        logger.critical(f"Unexpected processing failure: {e}", exc_info=True)
        raise ProcessingError("System encountered a critical failure") from e