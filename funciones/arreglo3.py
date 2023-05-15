def fibona(lista,x):
    a=0
    b=0
    for i in range(x):
        c=a+b
        a=b
        b=c
        lista.append(b)
        return lista
g=abs(int(input("ingrese la cantidad de valores:")))
lista=[]
print(fibona(lista,g))
