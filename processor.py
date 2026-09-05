import logging
from typing import Any, Dict, List

logger = logging.getLogger(__name__)

def validate_payload(data: Any) -> Dict[str, Any]:
    """Validates the incoming processing payload to ensure data integrity."""
    if not isinstance(data, dict):
        raise ValueError("Payload must be a dictionary")
    
    transaction_id = data.get("transaction_id")
    if not transaction_id or not isinstance(transaction_id, str):
        raise ValueError("Missing or invalid transaction_id")
        
    amount = data.get("amount")
    if amount is None or not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number")
        
    return {
        "transaction_id": transaction_id,
        "amount": float(amount),
        "status": "pending"
    }

def process_batch(batch_data: List[Any]) -> Dict[str, List[Any]]:
    """Processes a batch of input payloads with strict validation error handling."""
    successful_jobs = []
    failed_jobs = []
    
    for index, item in enumerate(batch_data):
        try:
            validated_data = validate_payload(item)
            # Simulate processing step with validated input
            validated_data["status"] = "processed"
            successful_jobs.append(validated_data)
        except (ValueError, TypeError) as error:
            failed_jobs.append({
                "index": index,
                "raw_data": item,
                "error": str(error)
            })
            logger.warning(f"Validation failed for item at index {index}: {error}")
            
    return {
        "processed": successful_jobs,
        "failed": failed_jobs
    }