from fastapi import APIRouter, HTTPException
from app.models import Calculator
from app.schemas import CalculatorInput, CalculatorResult

router = APIRouter()
calc = Calculator()

@router.post("/suma", response_model=CalculatorResult)
def suma(payload: CalculatorInput):
    result = calc.suma(payload.a, payload.b)
    return CalculatorResult(operation="suma", a=payload.a, b=payload.b, result=result)

@router.post("/resta", response_model=CalculatorResult)
def resta(payload: CalculatorInput):
    result = calc.resta(payload.a, payload.b)
    return CalculatorResult(operation="resta", a=payload.a, b=payload.b, result=result)

@router.post("/producto", response_model=CalculatorResult)
def producto(payload: CalculatorInput):
    result = calc.producto(payload.a, payload.b)
    return CalculatorResult(operation="producto", a=payload.a, b=payload.b, result=result)

@router.post("/division", response_model=CalculatorResult)
def division(payload: CalculatorInput):
    try:
        result = calc.division(payload.a, payload.b)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return CalculatorResult(operation="division", a=payload.a, b=payload.b, result=result)
