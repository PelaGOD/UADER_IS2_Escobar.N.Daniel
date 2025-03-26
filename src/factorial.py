#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Validar si se pasó un argumento
if len(sys.argv) == 1:
    print("Debe informar un número!")
    sys.exit(1)

# Validar que el argumento sea numérico
try:
    num = int(sys.argv[1])
except ValueError:
    print("Debe ingresar un número entero válido.")
    sys.exit(1)

# Calcular y mostrar el factorial
resultado = factorial(num)
if resultado is not None:
    print(f"Factorial {num}! es {resultado}")


