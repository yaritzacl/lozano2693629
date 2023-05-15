#tamaño lista 10 y 1519
#datos dentro de la lista 0y9  
#buscar un numero ingresado por teclado en la lista  
#decir si esta 
# decir si esta repetidos
#decir si esta repetidos, cuantas veces esta
#diga las posiciones donde las encontro

import random
tam=random.randint(10,20)
lista=[(random.randrange(9)) for i in range(tam)]
print(lista)


num= input('ingrese un numero')
help(lista.index) 
print("numero esta en la lista")
cont=(lista.index)
print("el numero se repite")  
    