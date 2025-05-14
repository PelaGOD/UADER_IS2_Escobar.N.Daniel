import time

class Scanner:
    def __init__(self):
        self.frecuencia_actual = None
        self.memorias = {
            "M1": ("AM", 810),
            "M2": ("FM", 101.1),
            "M3": ("FM", 95.5),
            "M4": ("AM", 1230)
        }

    def barrer_am(self):
        print("🔍 Barrido AM:")
        for f in range(530, 1710, 10):  # rango típico AM
            self.frecuencia_actual = f
            print(f"Sintonizando AM {f} kHz")
            time.sleep(0.1)  # simula el tiempo de escaneo

    def barrer_fm(self):
        print("🔍 Barrido FM:")
        f = 87.5
        while f <= 108.0:
            self.frecuencia_actual = round(f, 1)
            print(f"Sintonizando FM {self.frecuencia_actual} MHz")
            time.sleep(0.1)
            f += 0.2  # pasos típicos en FM

    def barrer_memorias(self):
        print("🎯 Sintonizando memorias:")
        for etiqueta, (tipo, frecuencia) in self.memorias.items():
            self.frecuencia_actual = frecuencia
            unidad = "kHz" if tipo == "AM" else "MHz"
            print(f"{etiqueta}: {tipo} {frecuencia} {unidad}")
            time.sleep(0.2)  # tiempo de sintonía en memorias

    def barrido_completo(self):
        print("\n=== Inicio de ciclo de barrido ===")
        self.barrer_am()
        self.barrer_fm()
        self.barrer_memorias()
        print("=== Fin de ciclo de barrido ===\n")


# Ejecución
scanner = Scanner()

# Simular 2 ciclos de barrido
for _ in range(2):
    scanner.barrido_completo()
