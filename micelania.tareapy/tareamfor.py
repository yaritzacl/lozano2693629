def impri_tabla_multi(num, limi):
    for i in range(1, limi + 1):
        resultado = num * i
        print(num, "x", i, "=", resultado)

num = int(input("Ingrese un número: "))
limi = int(input("Ingrese un límite: "))

impri_tabla_multi(num, limi)