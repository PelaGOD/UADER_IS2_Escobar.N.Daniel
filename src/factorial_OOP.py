class Factorial:
    def __init__(self):
        pass

    def run(self, min_val, max_val):
        import math
        for i in range(min_val, max_val + 1):
            print(f"Factorial de {i}: {math.factorial(i)}")

if __name__ == "__main__":
    fact = Factorial()
    fact.run(4, 8)  # Ejemplo de ejecución
