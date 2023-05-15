import random
lista=[]
tam=int (random.radint(5,10))
print (tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.apennd (num)

print(lista)

def moda(lista):
    moda=[]
con=0
for elemento in lista:
    if lista.count(elemento)> con:
        moda = []
        moda.append(elemento)
        con = lista.count(elemento)
