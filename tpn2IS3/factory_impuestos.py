from ejer4 import CalculadoraImpuestos

class CalculadoraImpuestosFactory:
    @staticmethod
    def obtener_calculadora():
        return CalculadoraImpuestos()
