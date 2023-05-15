#comentarios de burbuja 1

#inicio del programa que mostrará un rango de 5 a 10 de números aleatorios
import random
lista=[] #se declara la variable lista 
tam=int(random.randint(5,10))# se declara el tamaño de números aleatorios 
#print(tam)#se imprime el tamaño de números aleatorios 
for i in range(tam): #se declara el rango del tamaño en i  num=int(random.randrange(100)) # se declara la variable números para almacenar 
 lista.append(num) # se agrega un elemento al final de la lista 
 num=0
 print(lista) #imprime la lista 
 for i in range(tam): # el ciclo se llama para darle u n rango a la variable número 
   for j in range(i+1,tam):# se agrega una variable en el ciclo y el tamaño 
     if lista[i]>lista[j]: #lista i es mayor que lista j
       aux=lista[i]  # se hace la modificación de la variable i en la lista 
 lista[i]=lista[j] # la variable i es igual a la j 
 lista[j]=aux # En  la lista j  se hace la modificación de la variable 
 print(lista) # se imprima la lista 
for i in range(tam): #se le agrega un rango al tamaño 
  for j in range(i+1,tam): #se le asigna un rango en la variable j 
    if lista[i]<lista[j]: # la lista i es menor o igual a la lista j
      aux=lista[i] # se hace la modificación de la variable i en la lista 
lista[i]=lista[j] #lista i es igual a lista j 
lista[j]=aux  #la lista es igual a la modificación de aux 
print(lista) #se imprime la lista }
x,y=10,20