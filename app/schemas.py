from pydantic import BaseModel, Field

class CalculatorInput(BaseModel):
    a: float = Field(..., description="Operando A")
    b: float = Field(..., description="Operando B")

class CalculatorResult(BaseModel):
    operation: str
    a: float
    b: float
    result: float
