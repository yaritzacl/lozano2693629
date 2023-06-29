from Book import *
from account import *


class User:
    def _init_(self, Name:str, ID:int):
        self.__name = Name
        self.__id = ID
        account._init(self,self.name, self._id)

    def setNombre (self, Nombre:str):
        self.__name = Nombre
    
    def setID (self, ID:int):
        self.__id = ID


    def getNombre (self):
        return self.__name
    

    def getID (self):
        return self.__id
    
    def verify (self, Nombre, Documento):
        if Nombre == self._name and Documento == self._id:
            return "Verificado"
        else: 
            print("No estas verificado")
    
    def CheckAcount (self, Nombre , Documento):
        if User.verify (self , Nombre , Documento) == "Verificado":
            self.__reservado.append("ingrese los libros reservados:")
            self.__devueltos.append("ingrese los libros devueltos:")
            self.__perdidos.append("ingrese los libros perdidos:")
            print(account.getLibros_Prestados)
            print(account.getLibros_Reservados)
            print(account.getLibros_Devueltos)
            print(account.getLibros_Perdidos)
            print(account.calculate_fine)

    def renw_info (self, Titulo):
        Book.renw_info (self, Titulo)
