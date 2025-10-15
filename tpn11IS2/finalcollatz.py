def collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

try:
    entrada = input("Ingrese un número entero positivo menor o igual a 1999: ").strip()
    if not entrada:
        print("Error: no se ingresó ningún valor.")
    else:
        i = int(entrada)
        if i <= 0 or i > 1999:
            print("Error: ingrese un número positivo y menor o igual a 1999.")
        else:
            if i == 1:
                print("El número ya cumple la condición de la conjetura (1).")
            else:
                print(f"El número de iteraciones para {i} es {collatz(i)}")
except ValueError:
    print("Error: debe ingresar un número entero válido.")
