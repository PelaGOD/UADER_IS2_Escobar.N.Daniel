class FactorialSingleton:
    _instancia = None  # atributo de clase que guarda la instancia

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(FactorialSingleton, cls).__new__(cls)
        return cls._instancia

    def calcular_factorial(self, numero: int) -> int:
        if numero < 0:
            raise ValueError("El número debe ser no negativo")

        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
