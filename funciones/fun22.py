#inicio de funciones en el cual mostrara diferentes proceso con la lista
import random
from subprocess import list2cmdline
def llenarLista(tam,rango): #se le asigna un nombre a la funcion y se le da unos parametros 
    lista=[random.randrange(rango) for i in range(tam)]  #a la lista se le asigna un rango y tamaño con el metodo ramdon   
    return lista    
def llenarLista2(tam,rango): #se le asigna un nombre a la funcion y se le da unos parametros 
    lista2=[random.randrange(rango) for i in range(tam)]  #a la lista se le asigna un rango y tamaño con el metodo ramdon   
    return lista2    

    
l1=llenarLista(10,30)
print(l1)
l2=llenarLista2(10,20)
print(l2)
    
def sumaLista(lista):
    sum=0 
    for x in lista: 
        sum+=x
    return sum  
sum1=sumaLista(l1)
print(sum1)
sum2=sumaLista(l2)
print(sum2)
if sum1>sum2:
    print ("la lista es mayor")
elif sum1==sum2:
    print ("la listas son iguales")
else:
    print("la lista2 es mayor")
    
if sum1<sum2:
    print ("la lista es menor")
elif sum1==sum2:
    print ("la listas son iguales")
else:
    print("la lista2 es menor")


def mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
            return mayor
def menor(lista):
    menor=0
    for i in lista:
        if i<menor:
            return menor 
        
def promedioLista(lista,lista2): 
    sumaLista(lista)/len(lista2)
    return promedioLista

print(round(promedioLista(l1),l2))

"""print(sumaLista(l1))
print(sumaLista(l2))
print(round(promedioLista(l1),l2))
"""
