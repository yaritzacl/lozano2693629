import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
rebanada=lista[len(lista)//2:-1] #muestra la lista con un indice de la mitad asta el ultimo numero 
print(lista)
print(rebanada) 
