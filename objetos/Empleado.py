class Empleado:
       Counter=0 
def _init_(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        self.__Horas =0
        Empleado.counter +=1

def setNombre(self,nombre):
        self.__Nombre=nombre
def getNombre(self):
        return self.__nombre

def setcargo(self,cargo):
        self.__cargo=cargo
def getcargo(self):
        return self.__cargo

def setsalario(self,salario):
        self.__salario=salario
def getsalario(self):
        return self.__salario

def salarioHora (self):
        Hora=self._salario/(30*28/180)
        return(Hora)

def incrementoSalario (self): 
        if self.setsalario== 116000:
                ipc = 0.1312 + 0.03
                incremento =self.__salario * ipc
                totaliincremento = self.__salario + incremento 
                return(totalincremento)
        else:
                totalincremento = SelfReg.__salario * 0.1312
                return (totalincremento)

def new_func(totalincremento):
    return (totalincremento)
def HorasExtras(self,Horas=0):
        self.__Horas =Horas
        incremento =Empleado.incremetoSalario(self)
        salario= Empleado.salarioHora(self)
        extras = salario * Horas
        total = incremento + extras
        return (total)
def totalsueldo(self):
        total=Empleado.horasExtras(self, self.__horas)
        return (total)


