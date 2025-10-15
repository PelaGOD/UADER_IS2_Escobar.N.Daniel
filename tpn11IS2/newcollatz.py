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
    i = int(input("Ingrese un número entero positivo menor o igual a 1999: "))
    if i <= 0 or i > 1999:
        print("Error: ingrese un número positivo y menor o igual a 1999.")
    else:
        print("El número de iteraciones para %d es %d" % (i, collatz(i)))
except ValueError:
    print("Error: debe ingresar un número entero.")
