from sys import path


from Book import *
from User import *
from  account import *

prueba1 =Book ("El gran libro de los aceites esenciales" , "Paredes" , "765-532-533-19" , "10/2/2010", "Disponible")

prueba1.append_duet (" El gran libro de los aceites esenciales" , "Ramires")

print(prueba1.reservation_status ("El gran libro de los aceites esenciales"))

prueba1.feedback("El gran libro de los aceites esenciales")
print(prueba1.Book_request("El gran libro de los aceites esenciales"))


print(prueba1.renw_info("El gran libro de los aceites esenciales"))

prueba1 = account ("3","2" ,"5","1")
prueba1.setMulta_Cantidad(48)
prueba1.getLibros_Reservados

prueba1 = User("Zully",5 )
prueba1.verify("Zully", 14)
prueba1.CheckAcount("Zully" , 12)
print(prueba1.renw_info("El gran libro de los aceites esenciales"))