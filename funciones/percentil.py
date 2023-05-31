import random
def llenarLista(tamaño,rango):
     tamñ=random.randint(15,tamaño)
     while tamñ==tamñ:
          tama=random.randint(15,tamaño)
          if tamñ%5==0:
               lista=float[round(random)(1.50,rango)] 
               return lista
def quintil(lista):
     quintil=len(lista)/5
     menor=int(quintil-5)
     mayor=int(quintil)
     if len(lista)>quintil:
          listaquinti=lista[menor:mayor]
          return listaquinti
     else:
          return f"no se encuentra el quintil" 
lista=llenarLista(100,179  )
print(len(lista))

z=abs(int(input("ingrese el quintel que quieres saber:")))
print(quintil(llenarLista))
