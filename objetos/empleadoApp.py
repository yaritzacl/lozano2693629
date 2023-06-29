from  Empleado import *


persona1= Empleado=("pedro","arquitecto",120000)


persona1.getNombre ("Carlos")
persona1.getcargo ("administrador")
persona1.getsalario (2000000)

print(f"Tu nombre es:{persona1.setNombre}")
print (f"Tu cargo es:{persona1.setcargo}")
print (f"Tu salario es:{persona1.setsalario}")
print (f"Tu salario por hora es :{persona1.salarioHora()}")
print(f"tu incremento del salario es:{persona1.incrementosalario}()")
print(f"tu incremento del salario porlas horas extras es de: {persona1.horaextras(1)}")
print (f"tu sueldo es de: {persona1.Totalsueldo()}")


persona2= Empleado("pedro","arquitecto",120000)

persona2.getNombre("Carlos")
persona2.getcargo("administrador")
persona2.getsalario(2000000)

print(f"Tu nombre es:{persona2.setnombre}")
print (f"Tu cargo es:{persona2.setcargo}")
print (f"Tu salario es:{persona2.setsalario}")
print (f"Tu salario por hora es :{persona2.salarioHora()}")
print(f"tu incremento del salario es:{persona2.incrementosalario}()")
print(f"tu incremento del salario porlas horas extras es de: {persona2.horaextras(1)}")
print (f"tu sueldo es de: {persona2.Totalsueldo()}")