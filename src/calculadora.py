class Calculadora:
    def __init__(self, precision=2):
        self.precision = precision

    def _formatear_resultado(self, valor):
        return round(valor, self.precision)

    def sumar(self, a, b):
        return self._formatear_resultado(a + b)

    def restar(self, a, b):
        return self._formatear_resultado(a - b)

    def multiplicar(self, a, b):
        return self._formatear_resultado(a * b)

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return self._formatear_resultado(a / b)