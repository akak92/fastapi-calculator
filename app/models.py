from dataclasses import dataclass

@dataclass
class Calculator:
    """Modelo de dominio para operaciones básicas de calculadora."""

    def suma(self, a: float, b: float) -> float:
        return a + b

    def resta(self, a: float, b: float) -> float:
        return a - b

    def producto(self, a: float, b: float) -> float:
        return a * b

    def division(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
