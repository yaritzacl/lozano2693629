import random
def llenarLista(tam,rango):  
    lista=[random.randrange(rango) for i in range(tam)]     
    return lista 

def sumaLista(lista):
    sum=0 
    for x in lista: 
        sum+=x
    return sum   

def promedioLista(lista): 
    return sumaLista(lista)/len(lista)
    
def mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
            return mayor
        
def menor(lista):
    menor=1000000
    for i in lista:
        if i<menor:
            menor=i
            return menor
         
def ordenaAseden(lista):
    for i in range(len(lista)):
        for a in range (i+1,len(lista)):
            if lista[i]>lista[a]:
                aux=lista[i]
            lista[i]=lista[a]
            lista[a]=aux
            return lista

def orden_desenden(lista):
      for i in range(len(lista)):
        for a in range (i+1,len(lista)):
            if lista[i]<lista[a]:
                aux=lista[i]
            lista[i]=lista[a]
            lista[a]=aux
            return lista
def modaLista(lista):
    ind=0
    for i in lista:
        cont=0
        for a in lista:
            if i==a:
                cont+=1
        if cont>ind:
            ind =cont
            moda=i
            return moda
def medianaLista(lista):
    if len(lista)%2==0:
        mediana=(lista[(len(lista)//2)-1]+ lista[len(lista)//2])/2
    else:
        mediana =lista [(len(lista)//2)]
        return mediana
    
def buscarLista(lista):
    cont=0
    if a in lista:
        for i in range(len(lista)):
            if a==lista[i]:
                cont+=1
                return f"el numero existe {cont} veces"
            else:
                return "el numero no existe"
def posicionLista(lista,a):
    posicion=[]
    for i in range (len(lista)):
        if a==lista[i]:
            posicion.append(i)
            return posicion 


l1=llenarLista(3,10)
print(l1)
print(sumaLista(l1))
print(round(promedioLista(l1),2))       
print(mayor(l1))
print(menor(l1))
print(ordenaAseden(l1))
print (orden_desenden(l1))
print(modaLista(l1))
print(medianaLista(l1))
num=abs(int(input("digite un numero:")))
print (buscarLista(l1,num))
print(posicionLista(l1,num))