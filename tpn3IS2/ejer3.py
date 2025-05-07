from abc import ABC, abstractmethod

# Clase abstracta para la hamburguesa
class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Entrega por mostrador
class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        print("Hamburguesa entregada en mostrador.")

# Retiro por el cliente
class HamburguesaRetiro(Hamburguesa):
    def entregar(self):
        print("Hamburguesa retirada por el cliente.")

# Delivery
class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        print("Hamburguesa enviada por delivery.")
