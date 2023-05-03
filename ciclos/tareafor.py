# Solicitar al usuario inicio, fin y cantidad de incremento/decremento

inicio = int(input("Ingrese el número de inicio: "))
fin = int(input("Ingrese el número final: "))
inc = int(input("Ingrese la cantidad a incrementar o decrementar: "))

# Validamos si se debe incrementar o decrementar el numero 
if inc > 0:
    # Incrementar numero 
    for i in range(inicio, fin+1, inc):
     print(i, fin='')

else:
    # Decrementar numero 
    for i in range(inicio, fin-1, inc):
        print(i, end=' ')

Print ("el numero decrementado o incremetado es :", )
# inicio del programa 
# ingrese por pantalla un numero positivo 
#ingrese el valor de multiplos de n 
num= int(input("Ingrese un número positivo  : "))
n= int(input("Ingrese  n : "))
multiplos = 0
for i in range(serie+ 1):
    if i % n == 0:
        multiplos += 1

print(f"La cantidad de múltiplos de n en la serie : ",multiplos)