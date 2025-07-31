from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from typing import List


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
        raise HTTPException(status_code=400, detail= "Precisa de Dois Números")

    if operator == "sum":
        result = sum(list_numbers)
    elif operator == "subtract":
        result = list_numbers[0] - sum(list_numbers[1:])
    elif operator == "multiply":
        result = 1
        for n in list_numbers:
            result *= n
    elif operator == "divide":
        result = list_numbers[0]
        for n in list_numbers[1:]:
            if n == 0:
                raise HTTPException(status_code=400, detail="Não existe divisão por zero")
            result /= n
    else:
        raise HTTPException(status_code=400, detail="Operação Inválida")

    return {"result": result}
    
