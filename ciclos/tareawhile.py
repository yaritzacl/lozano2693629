#programa que de dos numeros que no sea uno mayor del otro
# Inicializar las variables con numeros que no uno sea mayor del otro 
numero1 = 0
numero2 = 0

#ingrese nuevamente otros numero  diferentes 
while num1 == num2:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
#Cual numero es mayor
if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

# Calcular el numero mayor del menor y  restar si es posible
resta  = mayor - menor

if mayor >= menor:
    print (" el numero mayor es:", mayor)
else:
    sobra = mayor % menor
    
    resta = resta

# Imprimir el resultado
print("el numero que sobra :", sobra )