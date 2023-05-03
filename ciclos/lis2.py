import random
lista=[]
suma=0
mayor=0
menor=0
tam=int (random.radint(10,20))
print (tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.apennd (num)
    suma += num
    if num>mayor:  
        mayor=num
    if num<menor and num!=0: 
        menor=num    
    
print(lista)
print(suma)
print(suma/tam)
print(mayor)
print(menor)
