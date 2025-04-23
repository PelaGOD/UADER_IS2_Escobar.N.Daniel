class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con:")
        for parte in self.partes:
            print(f"- {parte}")


class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def construir_body(self):
        self.avion.agregar_parte("Body")

    def construir_turbinas(self):
        self.avion.agregar_parte("Turbina izquierda")
        self.avion.agregar_parte("Turbina derecha")

    def construir_alas(self):
        self.avion.agregar_parte("Ala izquierda")
        self.avion.agregar_parte("Ala derecha")

    def construir_tren_aterrizaje(self):
        self.avion.agregar_parte("Tren de aterrizaje")

    def obtener_avion(self):
        return self.avion


# Ejemplo de uso:
builder = AvionBuilder()
builder.construir_body()
builder.construir_turbinas()
builder.construir_alas()
builder.construir_tren_aterrizaje()
avion = builder.obtener_avion()
avion.mostrar()
