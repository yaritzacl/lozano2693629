#llenar una lista con numeros aleatorios (reales con un decimal) que represente calificaciones de curso ,se evalua de o a 5 
#el curso puede tener entre 20 y 30 aprendices.
#hallar :
#generara lista nueva para los aprovados y los reprobados (se aprueba con 3 )
#genere listas nuevas por cada unidad .es decir , los que sacan de 0 a 1 son un grupo , los de 1 a 2 otro grupo y asi sucesivamente 
#diga cual es el promedio de los que aprueban y de los que reprueban por separado.
import random
cal=random.randint(20,30)
lista=[random.randrange(0.0,5.0) for i in range(cal)]
print(lista)
rebanada=lista[len(lista)//1:-1]
print(lista)
print(rebanada)
for i in range(cal):
    for j in range(cal):
        if lista[i]>lista[j]:
            aux=lista[i]
    lista[i]=lista[j]
    lista[j]
print(lista)
for i in range(cal):
    for j in range(i+1,cal):
        if lista[i]<lista[j]:
            lista[j]=aux
            print(lista)