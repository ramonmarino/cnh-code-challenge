from typing import List
from app.logs.setup_logger import LOGGER


class OperationService:
    def __init__(self):
        self.logger = LOGGER
    
       
    def service_challenge(self, request):
        operation = request.operation
        operands = request.operands

        if not operands or len(operands) < 2:
            self.logger.error("Operands list too short")
            raise ValueError("At least two operands are required.")

        self.logger.info(f"Executing operation {operation} with operands {operands}")

        match operation:
            case "sum":
                return self.sum(operands)
            case "subtract":
                return self.subtract(operands)
            case "multiply":
                return self.multiply(operands)
            case "divide":
                return self.divide(operands)
            case _:
                self.logger.error(f"Invalid operation: {operation}")
                raise ValueError("Invalid operation")
    @staticmethod
    def sum(operands: List[float]) -> float:
        return sum(operands)
    
    @staticmethod
    def subtract(operands: List[float]) -> float:
        result = operands[0]
        for op in operands[1:]:
            result -= op
        return result
    
    @staticmethod
    def multiply(operands: List[float]) -> float:
        result = 1
        for op in operands:
            result *= op
        return result
    
    @staticmethod
    def divide(operands: List[float]) -> float:
        result = operands[0]
        for op in operands[1:]:
            if op == 0:
                raise ValueError("Division by zero is not allowed. Please try a different number.")
            result /= op
        return result