# solicite ingresar por teclado un programa en el que muestre el numero de veces de los numeros digitados
#muestre el resultado de la suma de los numeros escritos al igual que es promedio, el numero mayor y el numero menor 
num=1
cont=0
suma=0 
prom=0
men=0
may=0
menor=100000
while num!=0:# muestre el numero mayor o igual a 0
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1 #se muestrar el numero de veces del contador de 1 en 1 
    suma += num # se muestrar la ejecucion de la suma y los numeros
    prom=cont/suma # se muestra la ejecucuin del promedio 
    if num>may: # ejecucion del numero mayor de los numeros 
        may=num
    if num<menor and num!=0: # ejecucion del numero menor de los numeros
        men=num    
        # se muestra los resultados de los numeros, suma, promedio, mayor y menor 
print(f'El usuario ingreso {cont-1} numeros')
#print('El usuario ingreso', cont, 'numeros')
print('la suma de los num: ',suma)
print('el promedio de la suma de los numeros es:',prom)
print('el men de los numeros es:',menor)
print('el may de los numeros es:',may)