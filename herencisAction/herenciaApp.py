# Se hace la importacion  de las clases 

from Aprendiz import *
from curso import *
# se  hace  la iniciacion de la clase 
objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) # se declara el constructor junto a sus atributos
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico")
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())
    # se imprime el resultado de la ubicacion donde se encuentra el archivo