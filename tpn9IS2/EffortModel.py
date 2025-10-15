
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel
#* Programa para procesar modelos lineales mediante correlación por cuadrados mínimos
#* 
#* UADER - FCyT
#* Ingeniería de Software II
#*
#* Dr. Pedro E. Colla
#* copyright (c) 2023,2024
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt
#*------------------------------------------------------------------------------------------------
#* Almacena dataset histórico
data = {
    'LOC': [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000],
    'Esfuerzo': [2,3,5,7,11,13,17,19,23,29]
}
df = pd.DataFrame(data)
------------------------------------------------------------------------------------------------
data = {
    'LOC': [794, 1336, 1572, 1572, 1126],
    'Esfuerzo': [1.07, 1.34, 2.27, 2.39, 0.93]
}

#*------------------------------------------------------------------------------------------------
#* Inicialización del programa
#*------------------------------------------------------------------------------------------------
version="7.0"
linear=False
exponential=False
os.system('clear')
#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version",required=False,help="version",action="store_true")
ap.add_argument("-x", "--exponential", required=False,help="Exponential model",action="store_true")
ap.add_argument("-l", "--linear", required=False,help="Linear model",action="store_true")
args = vars(ap.parse_args())

if args['version'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   sys.exit(0)

if args['linear'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Linear correlation model selected")
   linear=True

if args['exponential'] == True:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Exponential correlation model selected")
   exponential=True

if linear==False and exponential==False:
   print("Program %s version %s" % (sys.argv[0],version))
   print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

#*-----------------------------------------------------------------------------------------------
#* Definir dataset y procesar corrlación entre LOC (complejidad) y Esfuerzo (PM)
#*-----------------------------------------------------------------------------------------------
df = pd.DataFrame(data)
correlation = df['LOC'].corr(df['Esfuerzo'])

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal, usa numpy polyfit()
#*------------------------------------------------------------------------------------------------

if linear==True:

   a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
   R = np.corrcoef(df['LOC'], df['Esfuerzo'], 1)
   R2=R*R
   r_value=R2[1][0]

   print("Modelo lineal E=%.6f + %.6f*LOC)" % (b,a))
   print("El R-squared=%.4f (lineal)" % (r_value))

   lbl=("modelo lineal (R-Sq=%.2f)" % (r_value))
   plt.plot(df['LOC'], a*df['LOC']+b,label=lbl,color='red')

#*------------------------------------------------------------------------------------------------
#* procesa modelo exponencial utiliza OLS fit()
#*------------------------------------------------------------------------------------------------
if exponential==True:
   df['logEsfuerzo']=np.log(df['Esfuerzo'])
   df['logLOC']=np.log(df['LOC'])

   X = df['logLOC']
   Y = df['logEsfuerzo']
   X = sm.add_constant(X)  # Añadir una constante para el intercepto

   mx= sm.OLS(Y, X).fit()
   print(mx.summary())

   k=np.exp(mx.params['const'])
   b=mx.params['logLOC']

   print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k,b))
   print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

   lbl=("modelo exponencial (R-Sq=%.2f)" % (mx.rsquared))
   plt.plot(df['LOC'], k*(df['LOC']**b),label=lbl,color='green')

#*------------------------------------------------------------------------------------------------
#* Hace plot del dataset histórico
#*------------------------------------------------------------------------------------------------

#--- Modelo lineal
a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
pred_lin = a*df['LOC']+b
r2_lin = np.corrcoef(df['Esfuerzo'], pred_lin)[0,1]**2

print("Modelo lineal: E = %.6f*LOC + %.6f" % (a,b))
print("R² lineal= %.4f" % (r2_lin))

#--- Modelo exponencial (log-log)
df['logEsfuerzo'] = np.log(df['Esfuerzo'])
df['logLOC'] = np.log(df['LOC'])
X = sm.add_constant(df['logLOC'])
Y = df['logEsfuerzo']
mx = sm.OLS(Y, X).fit()
k = np.exp(mx.params['const'])
b_exp = mx.params['logLOC']
pred_exp = k * (df['LOC']**b_exp)
r2_exp = mx.rsquared

print("Modelo exponencial: E = %.6f * LOC^%.6f" % (k,b_exp))
print("R² exponencial= %.4f" % (r2_exp))

#--- Elegir mejor modelo
if r2_exp > r2_lin:
    mejor = "exponencial"
    modelo = lambda x: k * (x**b_exp)
else:
    mejor = "lineal"
    modelo = lambda x: a*x + b

print("\nEl mejor modelo es:", mejor)

#--- b) Estimar esfuerzo para LOC=9100
loc_9100 = 9100
esf_9100 = modelo(loc_9100)
print("\nEstimación para LOC=9100: Esfuerzo=%.2f PM" % esf_9100)

# Graficar
plt.scatter(df['LOC'], df['Esfuerzo'], label="Datos históricos", color="black")
plt.plot(df['LOC'], pred_lin, label=f"Lineal (R²={r2_lin:.2f})", color="red")
plt.plot(df['LOC'], pred_exp, label=f"Exponencial (R²={r2_exp:.2f})", color="green")
plt.scatter([loc_9100],[esf_9100], label=f"Estimación 9100 LOC ({esf_9100:.1f} PM)", color="blue", marker="x", s=100)
plt.xlabel("LOC")
plt.ylabel("Esfuerzo (PM)")
plt.legend()
plt.title("Comparación de modelos y estimación para LOC=9100")
plt.show()

#--- c) Estimar esfuerzo para LOC=200
loc_200 = 200
esf_200 = modelo(loc_200)
print("\nEstimación para LOC=200: Esfuerzo=%.2f PM" % esf_200)
print("⚠ Precaución: LOC=200 está fuera del rango de calibración (1000–10000).")
print("La estimación puede no ser confiable.")

# Graficar
plt.scatter(df['LOC'], df['Esfuerzo'], label="Datos históricos", color="black")
plt.plot(df['LOC'], pred_lin, label=f"Lineal (R²={r2_lin:.2f})", color="red")
plt.plot(df['LOC'], pred_exp, label=f"Exponencial (R²={r2_exp:.2f})", color="green")
plt.scatter([loc_200],[esf_200], label=f"Estimación 200 LOC ({esf_200:.1f} PM)", color="orange", marker="o", s=100)
plt.xlabel("LOC")
plt.ylabel("Esfuerzo (PM)")
plt.legend()
plt.title("Estimación para LOC=200 (fuera de rango)")
plt.show()

plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()

