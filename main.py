from sys  import path
path.append('..\\lozano2693629\\modulos')

import SLZ.slzlista.listas as slzlista
import SLZ.slzdici.diccionarios as slzdici
print (slzlista.llenarLista(10,20))

dicci={}
w= input('digita la palabra clave:')
y= input('digita el valor:')
print (slzdici.updateIngles(dicci,w,y))