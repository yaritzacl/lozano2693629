#centarios de burbuja 2 

import random 
tam=random.randint(5,10)
#inicia el programa declarando la lista con ordenamiento de burbuja 
lista=[random.randrange(100) for i in range(tam)] 
print(lista)#se imprime la lista 
for i in range(len(lista)-1): #se le asigna el rango con el método len a la lista 
 if lista[i]<lista[i+1]: #se comprara si lista i es menor a lista i +1   lista[i],lista[i+1]=lista[i+1],lista[i] 
   print(lista) #se imprime en pantalla el resultado de lista 
#in - not in 
 # for i in range(len(lista)):
# print(lista[i]) 
for x in lista: #se declara lista en un ciclo 
  print(x) #se imprime la lista x 
if 10 not in lista: 
  print('no esta')# se prime que no esta   
else:
  print('si esta')# se imprime que si esta