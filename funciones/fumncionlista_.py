#inicio de funciones en el cual mostrara diferentes proceso con la lista
import random
def llenarLista(tam,rango): #se le asigna un nombre a la funcion y se le da unos parametros 
    lista=[random.randrange(rango) for i in range(tam)]  #a la lista se le asigna un rango y tamaño con el metodo ramdon   
    return lista # se llama la lista con   

def sumaLista(lista):# se le asigna a la funcion sumalista y se llama el return de la lista
    sum=0 # se declara la suma 
    for x in lista: 
        sum+=x
    return sum #se muestra la suma realizada con el ciclo for  junto al retorno lista  

def promedioLista(lista):# en esta funcion se saca el promedio con ayuda de la funciom sumlista 
    return sumaLista(lista)/len(lista)
    #se imprime en pantalla el resultado de las funciones 
l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))