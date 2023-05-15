import random
def areglo (tam,rango):
        lista=[(random.randrange(rango)) for i in range(tam)]     
        return lista

def sumareglo(lista):
        sum=0 
        for l in lista: 
                sum+=l
                return sum
lisq=areglo(4,10)
print(lisq)
print (sumareglo(lisq))     