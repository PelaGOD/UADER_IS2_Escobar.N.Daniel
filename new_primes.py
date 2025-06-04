import os
import sys

# Limpiar pantalla según sistema operativo
os.system('clear' if os.name == 'posix' else 'cls')

args = sys.argv[1:]

# Validar que haya al menos un argumento
if len(args) == 0:
    print("⚠️ Error: No se proporcionaron argumentos.")
    print("👉 Uso: python new_primes.py [upper] o [lower upper]")
    sys.exit(1)

# Limitar a los dos primeros argumentos
args = args[:2]

# Intentar convertir a enteros
try:
    if len(args) == 1:
        lower = 1
        upper = int(args[0])
    else:
        lower = int(args[0])
        upper = int(args[1])
except ValueError:
    print("⚠️ Error: Los argumentos deben ser números enteros válidos.")
    sys.exit(1)

# Validar rango lógico
if lower > upper:
    print("⚠️ Error: El primer número debe ser menor o igual al segundo.")
    sys.exit(1)

# Mostrar los primos en el rango
print(f'✅ Números primos entre {lower} y {upper} son:\n')

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
