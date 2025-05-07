from abc import ABC, abstractmethod

# Implementación: Interfaz del tren laminador
class TrenLaminador(ABC):
    @abstractmethod
    def laminar(self, lamina):
        pass

# Implementación concreta: tren de 5 metros
class Tren5m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Laminar lámina de {lamina.espesor}'' x {lamina.ancho}m x 5m de largo en Tren 5m.")

# Implementación concreta: tren de 10 metros
class Tren10m(TrenLaminador):
    def laminar(self, lamina):
        print(f"Laminar lámina de {lamina.espesor}'' x {lamina.ancho}m x 10m de largo en Tren 10m.")

# Abstracción: lámina de acero
class LaminaAcero:
    def __init__(self, espesor, ancho, tren_laminador: TrenLaminador):
        self.espesor = espesor
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        self.tren_laminador.laminar(self)

# --- Ejemplo de uso ---
if __name__ == "__main__":
    tren5 = Tren5m()
    tren10 = Tren10m()

    lamina1 = LaminaAcero(0.5, 1.5, tren5)
    lamina2 = LaminaAcero(0.5, 1.5, tren10)

    lamina1.producir()  # Produce con tren de 5m
    lamina2.producir()  # Produce con tren de 10m
