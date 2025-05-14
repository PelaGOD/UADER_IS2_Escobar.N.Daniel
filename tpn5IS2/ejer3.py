# Sujeto (Subject)
class EmisorID:
    def __init__(self):
        self.observers = []

    def suscribir(self, observer):
        self.observers.append(observer)

    def emitir(self, id_emitido):
        print(f"\n📢 Emisor emite ID: {id_emitido}")
        for observer in self.observers:
            observer.actualizar(id_emitido)


# Observador (Observer)
class ObservadorID:
    def __init__(self, id_personal):
        self.id_personal = id_personal

    def actualizar(self, id_emitido):
        if self.id_personal == id_emitido:
            print(f"✅ Observador con ID {self.id_personal} recibió coincidencia.")
