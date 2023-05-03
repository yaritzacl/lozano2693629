#este programa mostrar que un numero sea mayor que el otro si ni es el caaso pidalos de nuevo 
#reste el menor del mayor y si el resultado lo permite reste nuevamente y diga cuantos sobra
num1=1
num2=2
may=0
men=0
while num!=0:#digite un numero
     num1=int(input('ingrese numero'))
     num2=int(input('ingrese numero'))
if num>may: # ejecucion del numero mayor de los numeros 
    may=num
if num<menor and num!=0: # ejecucion del numero menor de los numeros
    men=num
print ('')