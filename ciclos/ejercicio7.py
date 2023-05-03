#.Solicitar 2 números al usuario e imprimir el cociente y el residuo del mayor en el menor sin utilizar la división ni el mod. 


# Solicitar los números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Determinar cuál es el mayor y cuál es el menor
if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

# Calcular el cociente y el residuo del mayor en el menor sin usar la división ni el mod
cociente = 0
while mayor >= menor:
    mayor -= menor
    cociente += 1
residuo = mayor

# Imprimir el resultado
print("El cociente de", mayor, "en", menor, "es", cociente)
print("El residuo de", mayor, "en", menor, "es", residuo)