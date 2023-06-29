class persona:
    def __init__(self,nombre,documento):
        #print('se instancio un objeto')
        self.__nombre = nombre
        self.__documento = documento
        #self__telefono
        self.__cursos=[]
        
class Persona:
    def __init__(self,nombre,documento):
        #print('Se instancio un objeto')
        self.__nombre=nombre
        self.__documento=documento
        #self.__telefono
        self.__cursos=[]
        
        def setNombre(self,nombre):
            self.__nombre = nombre
        def getNombre(self):
            return self.__nombre
            
        def setDocumento(self,documento):
            self.__documento = documento
        def getDocumento(self):
            return self.__documento
        
        def consultar(self,):
            def setingresecurso(self,curso):
                if curso not in self.__cursos:
                    self.__cursos.append(curso)
                
                        
        def seteliminarcurso(self,eliminar):
            self.__eliminarcurso = eliminar
