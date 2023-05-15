#Ejercicio 11 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Lista de números entre 2 y 15
numeros = list(range(2, 16))

# Lista para almacenar los factoriales
factoriales = []

# Calcular el factorial de cada número y agregarlo a la lista correspondiente
for numero in numeros:
    fact = factorial(numero)
    factoriales.append(fact)

# Imprimir la lista de factoriales
print(factoriales)