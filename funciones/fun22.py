
import random
def llenarLista(tam,rango):  
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista    
def llenarLista2(tam,rango): 
    lista2=[random.randrange(rango) for i in range(tam)]    
    return lista2  

    
l1=llenarLista(10,30)
print(l1)
l2=llenarLista2(10,30)
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
print("el promedio conjunto es:")        
def promedioconjun(lista1,lista2): 
    sumaLista(lista1)/len(lista2)
    suma=0
    for s in lista1:
        suma+=s
        for s in lista2:
            suma+=s
            promedio=suma/(len(lista1)+(len(lista2)))
            return promedio 
        print(promedio)

def promedio(lista):
    suma=0
    for s in lista:
        suma+=s
    promedio= suma/(len(lista))
    return promedio

def promedioLista(lista1,lista2):
    promediocojun= promediocojun(lista1,lista2)
    promedio1=promedio(lista1)
    if promedio1>promedioconjun:
        return f"el promedio es mayor de promedio conjunto"
    elif promedio1<promedioconjun:
        return f"el promedio es menor del promedio conjunto"
    else:
        return f"el promedio es igual "
print(sumaLista(l1))
print(sumaLista(l2))
print()

