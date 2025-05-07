# Abstract Factory
class ComidaFactory:
    def crear_comida(self):
        pass

    def crear_bebida(self):
        pass


# Fábrica concreta 1
class ComboInfantilFactory(ComidaFactory):
    def crear_comida(self):
        return "Hamburguesa infantil"

    def crear_bebida(self):
        return "Jugo"


# Fábrica concreta 2
class ComboAdultoFactory(ComidaFactory):
    def crear_comida(self):
        return "Hamburguesa doble"

    def crear_bebida(self):
        return "Cerveza"


def preparar_combo(factory: ComidaFactory):
    comida = factory.crear_comida()
    bebida = factory.crear_bebida()
    print(f"Combo preparado: {comida} + {bebida}")


# Ejemplo de uso:
preparar_combo(ComboAdultoFactory())  # Combo preparado: Hamburguesa doble + Cerveza
