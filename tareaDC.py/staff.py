from User import *

class Staff(User):
    def _init_ (self, Departamento:str):
        self.__departamento = Departamento

    def setDept (self , Departamento:str):
        self.__departamento = Departamento
    
    property
    def getDept (self):
        return self.__departamento

class Staff(User):
    def _init_ (self, Departamento:str):
        self.__departamento = Departamento

    def setDept (self , Departamento:str):
        self.__departamento = Departamento
    
    
    def getDept (self):
        return self.__departamento