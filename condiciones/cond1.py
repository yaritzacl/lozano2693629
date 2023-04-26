# este programa mostrar el resultado de dos numeros, mostrara si son iguales, ascendente o desensente
x=input('ingrese numero')
y=input('ingrese numero')
# si el resultado de los dos numeros es igual  se muestra iguales  
if x==y:
    print('son iguales')
    # si el resultado de uno de los numeros es mayor del otro mostrar que es descendente
elif x>y:
    print('descendente')
    # si el resultado de uno de los numeros es menor del otro mostrar que es asendente

else:
    print('ascendente')