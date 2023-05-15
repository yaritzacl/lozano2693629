def calcular_suma(x):
    suma = 0
    for elem in x:
        suma += elem
    return suma

numeros=[5,4,6,7]

resultado = calcular_suma(numeros)
print("La suma de los números es:", resultado)