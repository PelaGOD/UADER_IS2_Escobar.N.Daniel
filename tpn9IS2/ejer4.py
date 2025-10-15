import numpy as np
import matplotlib.pyplot as plt

# --- Definición de las funciones ---
# Asumiendo las relaciones dadas en el TP
# E = 8 * S^0.95
# td = 2.4 * E^0.33

def calcular_esfuerzo(S):
  """Calcula el esfuerzo (E) dado el tamaño del proyecto (S)."""
  return 8 * (S**0.95)

def calcular_tiempo(E):
  """Calcula el tiempo de desarrollo (td) dado el esfuerzo (E)."""
  return 2.4 * (E**0.33)

# --- Datos para las gráficas ---
# Intervalo de tamaños S de 0 a 10000
sizes = np.linspace(1, 10000, 400) # Empezamos en 1 para evitar S^0
esfuerzos_calculados = calcular_esfuerzo(sizes)

# Intervalo de esfuerzos E de 1 a 500
esfuerzos_base = np.linspace(1, 500, 400)
tiempos_calculados = calcular_tiempo(esfuerzos_base)


# --- Creación de las gráficas ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfica 1: Esfuerzo vs. Tamaño
ax1.plot(sizes, esfuerzos_calculados, color='blue')
ax1.set_title('Esfuerzo (E) vs. Tamaño del Proyecto (S)')
ax1.set_xlabel('Tamaño del Proyecto (S)')
ax1.set_ylabel('Esfuerzo (E)')
ax1.grid(True)

# Gráfica 2: Tiempo vs. Esfuerzo
ax2.plot(esfuerzos_base, tiempos_calculados, color='red')
ax2.set_title('Tiempo de Desarrollo (td) vs. Esfuerzo (E)')
ax2.set_xlabel('Esfuerzo (E)')
ax2.set_ylabel('Tiempo de Desarrollo (td)')
ax2.grid(True)

plt.tight_layout()
plt.show()