#Determinar cual y cuantos numeros perfectos hay entre 1 y 1000
def num_perfecto(a):
    suma= 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    return suma == a

    num_perfecto = []

    for i in range(1, 1001):
        if num_perfecto(i):
            num_perfecto.append(i)
            
print("hay", len("num_perfecto"), "numeros prefectos de 1 a 1000:", num_perfecto)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             