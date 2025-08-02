from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import List
from .services.service import OperationService

router = APIRouter()

class ChallengeRequest(BaseModel):
    operation: str
    operands: List[float]

@router.post(
    "/challenge",
    summary="Execute a processing challenge",
)

def challenge_entrypoint(request: ChallengeRequest):
    operator = request.operation
    list_numbers = request.operands
    
    if not list_numbers or len(list_numbers) < 2:
        raise HTTPException(status_code=400, detail= "At least two operands are required")
    
    if len(list_numbers) > 50:
        raise HTTPException(status_code=413, detail="Too many operands")
   
    try:
        match operator:
            case "sum":
                result = OperationService.sum(list_numbers)
            case "subtract":
                result = OperationService.subtract(list_numbers)
            case "multiply":
                result = OperationService.multiply(list_numbers)
            case "divide":
                result = OperationService.divide(list_numbers)
            case _:
                raise HTTPException(status_code=400, detail="Unsupported operation. Please use one of: sum, subtract, multiply, divide.")
    except ValueError as e:
        raise HTTPException(status_code=400, detail = "Division by zero is not allowed. Please try a different number.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"The result of the operation is": result}
