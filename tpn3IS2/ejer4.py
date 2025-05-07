from abc import ABC, abstractmethod

# Clase base abstracta
class Factura(ABC):
    def __init__(self, importe: float):
        self.importe = importe

    @abstractmethod
    def mostrar_detalle(self):
        pass

# Factura para IVA Responsable
class FacturaResponsable(Factura):
    def mostrar_detalle(self):
        print(f"Factura A - IVA Responsable. Importe total: ${self.importe}")

# Factura para IVA No Inscripto
class FacturaNoInscripto(Factura):
    def mostrar_detalle(self):
        print(f"Factura B - IVA No Inscripto. Importe total: ${self.importe}")

# Factura para IVA Exento
class FacturaExento(Factura):
    def mostrar_detalle(self):
        print(f"Factura C - IVA Exento. Importe total: ${self.importe}")

