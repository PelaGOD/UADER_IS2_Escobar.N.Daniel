class MemoriaEstados:
    def __init__(self):
        self.estado_actual = None
        self.historial = []  # Lista de los últimos 4 estados

    def set_estado(self, nuevo_estado):
        if self.estado_actual is not None:
            self.historial.insert(0, self.estado_actual)
            # Limitar a 4 estados pasados
            if len(self.historial) > 4:
                self.historial.pop()
        self.estado_actual = nuevo_estado
        print(f"🔄 Estado actual: {self.estado_actual}")

    def undo(self, n):
        if n < 0 or n >= len(self.historial):
            print(f"⚠️ No se puede deshacer {n} paso(s): historial insuficiente.")
            return

        # Guardar el actual como parte del historial
        self.historial.insert(0, self.estado_actual)
        if len(self.historial) > 4:
            self.historial.pop()

        self.estado_actual = self.historial.pop(n + 1)  # +1 porque el actual se insertó en la posición 0
        print(f"↩️ Estado recuperado ({n} pasos atrás): {self.estado_actual}")

    def mostrar_estado(self):
        print(f"📌 Estado actual: {self.estado_actual}")
