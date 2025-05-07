import copy

class Prototipo:
    def __init__(self, valor):
        self.valor = valor

    def clonar(self):
        return copy.deepcopy(self)


# Ejemplo de uso:
obj1 = Prototipo(10)
obj2 = obj1.clonar()
obj3 = obj2.clonar()

print(obj1.valor, obj2.valor, obj3.valor)  # 10 10 10
