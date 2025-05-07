from abc import ABC, abstractmethod

# Componente base
class Componente(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

# Hoja: Pieza
class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")

# Compuesto: Subconjunto o producto
class SubConjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar(self, componente: Componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"+ SubConjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Crear producto principal
    producto_principal = SubConjunto("Producto Principal")

    # Crear 3 subconjuntos con 4 piezas cada uno
    for i in range(1, 4):
        subconjunto = SubConjunto(f"SubConjunto{i}")
        for j in range(1, 5):
            subconjunto.agregar(Pieza(f"Pieza{i}.{j}"))
        producto_principal.agregar(subconjunto)

    # Mostrar la jerarquía inicial
    print("== Producto inicial ==")
    producto_principal.mostrar()

    # Agregar subconjunto adicional opcional con 4 piezas
    subconjunto_extra = SubConjunto("SubConjuntoOpcional")
    for k in range(1, 5):
        subconjunto_extra.agregar(Pieza(f"PiezaExtra.{k}"))

    producto_principal.agregar(subconjunto_extra)

    # Mostrar jerarquía final
    print("\n== Producto con subconjunto adicional ==")
    producto_principal.mostrar()
