from abc import ABC, abstractmethod

# Componente base
class NumeroComponente(ABC):
    @abstractmethod
    def mostrar(self):
        pass

# Clase base concreta
class Numero(NumeroComponente):
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Valor actual: {self.valor}")
        return self.valor

# Decorador base
class DecoradorNumero(NumeroComponente):
    def __init__(self, componente: NumeroComponente):
        self.componente = componente

# Decorador: suma 2
class DecoradorSuma(DecoradorNumero):
    def mostrar(self):
        valor = self.componente.mostrar()
        valor += 2
        print(f" +2 => {valor}")
        return valor

# Decorador: multiplica por 2
class DecoradorMultiplicacion(DecoradorNumero):
    def mostrar(self):
        valor = self.componente.mostrar()
        valor *= 2
        print(f" *2 => {valor}")
        return valor

# Decorador: divide por 3
class DecoradorDivision(DecoradorNumero):
    def mostrar(self):
        valor = self.componente.mostrar()
        valor /= 3
        print(f" /3 => {valor}")
        return valor

# --- Ejemplo de uso ---
if __name__ == "__main__":
    print("== Sin decoradores ==")
    numero_base = Numero(6)
    numero_base.mostrar()

    print("\n== Decorador: +2 ==")
    decorado1 = DecoradorSuma(numero_base)
    decorado1.mostrar()

    print("\n== Decorador: *2 después de +2 ==")
    decorado2 = DecoradorMultiplicacion(decorado1)
    decorado2.mostrar()

    print("\n== Decorador: /3 después de *2 después de +2 ==")
    decorado3 = DecoradorDivision(decorado2)
    decorado3.mostrar()

    print("\n== Decorador anidado en una sola línea ==")
    DecoradorDivision(
        DecoradorMultiplicacion(
            DecoradorSuma(
                Numero(6)
            )
        )
    ).mostrar()
